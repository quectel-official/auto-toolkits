## 简要介绍
一个用于实现 SL-V2X-Preconfiguration-r14 编解码的 Python 包，使用 [asn1tools](https://github.com/eerimoq/asn1tools) 实现编解码操作。

SL-V2X-Preconfiguration-r14 是 LTE-V2X 通信技术中物理层配置定义信息，使用 asn1 语言进行描述，在本项目中内置了完整的定义文件 v2x_r14_preconfig.asn，不需要额外指定 asn1 文件。

## 支持的编码规则:
- XML Encoding Rules (XER)
- JSON Encoding Rules (JER)
- Generic String Encoding Rules (GSER)
- Unaligned Packed Encoding Rules (UPER)

> UPER 为 二进制 数据，无法直接修改，通常设备内使用这种格式的数据（二进制数据或者hex字符）
>
> 另外三种编码规则为 文本 数据，可以直接修改，通常在修改完成后转换为 UPER 编码，供设备内使用。

## 安装要求
- python >= 3.6

## 命令行参数
本项目提供一个命令行工具，实现编解码功能

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
  --r15                 Use v2x_r15_preconfig.asn (R15) instead of
                        default R14.
  -v, --version         Show version information
```

## 示例
```bash
# 将 二进制 的 uper 编码文件转换为 文本 的 xml 编码文件
v2xpreconfig -i uper -o xer input.uper output.xml
# 将 文本 的 xml 编码文件转换为 二进制 的 uper 编码文件
v2xpreconfig -i xer -o uper input.xml output.uper

# 将 二进制 的 uper 编码数据(hex 字符格式)转换为 文本 的 xml 编码文件
v2xpreconfig -i uper -o xer ${HEX} output.xml
# 将 文本 的 xml 编码文件转换为 二进制 的 uper 编码格式，以 hex 字符串格式输出到 标准设备
v2xpreconfig -i xer -o uper input.xml
```