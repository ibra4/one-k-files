# Group files into sub folders

This is a simple script which groups files into subfolders by language name

### Usage

```
python3 group.py [input_path] [output_path] [--verbose]
```

### options

- **input_path:**<em>(optional)</em>: input folder which contains all languages files. **default: ./files**
- **output_path**<em>(optional)</em>: output folder which will contain all languages folders. **default: ./output**
- **--verbose:**<em>(optional)</em>: Specifies that you want to display detailed processing information

## Example

```sh
python3 group.py ./files ./output --verbose
```

```
python3 group.py
```
