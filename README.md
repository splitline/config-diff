# config-diff

## Usage
```
python diff.py [config file] [another config file]
```

## Diff Result
- Is there different **keys**?
  - Keys which only exist in the first file.
  - Keys which only exist in the second file.
- Is there different **values**?
  - Key exists in both files, but values between the two configs are different.