# upload-run-download

This is a simple program that uploads current directory to a remote machine using rsync,
runs a specified command there, and downloads the results back to the local machine.

## Usage

```
urd <remote machine> <command to run there>
```

## Details

If you run it from a `my_project` directory, it will be copied to `remote_machine:~/my_project`.

Stuff in `.gitignore` will be skipped.
(This relies on the property that rsync filter syntax is almost the same as gitignore syntax.)

If an optional file `.urd_download` is present,
files and directories specified there will be downloaded back to the local machine afterwards.
