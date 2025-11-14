## Introduction
A Python package for implementing the encoding and decoding of SL-V2X-Preconfiguration-r14, using  [asn1tools](https://github.com/eerimoq/asn1tools).

SL-V2X-Preconfiguration-r14 is the physical layer configuration definition in LTE-V2X communication technology, described using ASN.1 language. The complete definition file v2x_r14_preconfig.asn is included in this project, and there is no need to specify an additional ASN.1 file.

## Supported Encoding Rules
- XML Encoding Rules (XER)
- JSON Encoding Rules (JER)
- Generic String Encoding Rules (GSER)
- Unaligned Packed Encoding Rules (UPER)

> UPER is binary data, which cannot be directly modified and is typically used in devices in this format (binary data or hex characters). 
>
> The other three encoding rules are for text data, which can be directly modified and typically converted to UPER after modification for use in devices.

## Installation Requirements
- python >= 3.6

## Command Line Parameters
This project provides a command line tool to implement encoding and decoding.

```
Usage: v2xpreconfig [Options] <infile> [outfile]

Options:
  -h, --help            show this help message and exit
  -i IN_RULE, --in-rule=IN_RULE
                        Specifie the input file encoding rules. Options: uper,
                        xer, jer, gser. default: uper.
  -o OUT_RULE, --out-rule=OUT_RULE
                        Specifie the output file encoding rules. Options:
                        uper, xer, jer, gser. default: xer.
  --indent=INDENT       Specifie the amount of indent of the text of output
                        file. Options: 0, 2, 4. default: 2.
  --r15                 Use SL_V2X_Preconfiguration.asn (R15) instead of
                        default R14.
  -v, --version         Show version information
```

## Example
```bash
# To convert a binary UPER encoded file to a text XML encoded file.
v2xpreconfig -i uper -o xer input.uper output.xml
# To convert a text XML encoded file to a binary UPER encoded file.
v2xpreconfig -i xer -o uper input.xml output.uper

# To convert a UPER encoded (in hex string format) file to a text XML encoded file
v2xpreconfig -i uper -o xer ${HEX} output.xml
# To convert a text XML encoded file to a binary UPER encoded file, and output the file to a standard device in hex string format.
v2xpreconfig -i xer -o uper input.xml
```