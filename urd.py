#!/usr/bin/env python3

''' upload - run - download '''

from pathlib import Path
import subprocess
import sys
import shlex


def main():
    [machine, *args] = sys.argv[1:]
    dirname = Path.cwd().name

    print('*' * 20, 'uploading ...')
    subprocess.check_call([
        'rsync',
        '-avzc',
        '--filter', ':- .gitignore',
        '.',
        machine + ':' + dirname,
    ])

    if args:
        args = [shlex.quote(a) for a in args]
        print('*' * 20, 'running', ' '.join(args), '...')
        p = subprocess.run([
            'ssh',
            '-t',
            machine,
            '. .profile; cd ' + dirname + ' && ' + ' '.join(args),
        ])
        if p.returncode:
            print(p)
            sys.exit(1)

    d = Path('.urd_download')
    if d.exists():
        print('*' * 20, 'downloading ...')
        subprocess.check_call([
            'rsync',
            '-avzL',
            '--filter', '.+ ' + str(d),
            '--filter', '- /*',
            machine + ':' + dirname + '/',
            '.',
        ])


if __name__ == '__main__':
    main()
