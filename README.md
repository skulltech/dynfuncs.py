# dynfuncs.py
Script for displaying global dynamic function symbols in an elf file.

That usually corresponds to 
- Dynamically linked external library functions in the case of executables.
- Exported functions in the case of shared libraries.

## Usage

```console
sumit@HAL9000:~/Coding/dynfuncs.py$ python3 dynfuncs.py --help
usage: dynfuncs.py [-h] binary

display globally bound function symbols defined in an elf binary

positional arguments:
  binary      elf binary to scan

optional arguments:
  -h, --help  show this help message and exit

sumit@HAL9000:~/Coding/dynfuncs.py$ python3 dynfuncs.py /bin/cat
Symbol table '.dynsym' contains 50 global functions:
   Num: Name
     0: free
     1: abort
     2: __errno_location
     3: strncmp
     4: _exit
     5: __fpending
     6: write
     7: textdomain
     8: fclose
     9: bindtextdomain
    10: stpcpy
    11: dcgettext
    12: __ctype_get_mb_cur_max
    13: strlen
    14: __stack_chk_fail
    15: getopt_long
    16: mbrtowc
    17: strrchr
    18: lseek
    19: memset
    20: ioctl
    21: close
    22: posix_fadvise
    23: read
    24: __libc_start_main
    25: memcmp
    26: fputs_unlocked
    27: calloc
    28: memcpy
    29: fileno
    30: malloc
    31: fflush
    32: nl_langinfo
    33: __fxstat
    34: __freading
    35: realloc
    36: setlocale
    37: __printf_chk
    38: memmove
    39: error
    40: open
    41: fseeko
    42: __cxa_atexit
    43: getpagesize
    44: exit
    45: fwrite
    46: __fprintf_chk
    47: mbsinit
    48: iswprint
    49: __ctype_b_loc
```
