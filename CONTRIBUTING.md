# Contributing to Global Vehicle Models List

Thank you for your interest in contributing to the Global Vehicle Models List! This project aims to maintain a comprehensive and up-to-date list of vehicle models organized by brand.

## How to Contribute

### Adding New Vehicle Models or Brands

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Edit any of the three data files**:
   - `data/models.json` - JSON format
   - `data/models.csv` - CSV format  
   - `data/models.yaml` - YAML format
4. **Add your changes** to any one of these files (the automation will sync the others)
5. **Commit your changes** with a descriptive message
6. **Push to your fork** and submit a pull request

### Data Format Guidelines

#### For JSON (`data/models.json`)
```json
{
    "BrandName": [
        "Model 1",
        "Model 2",
        "Model 3"
    ]
}
```

#### For CSV (`data/models.csv`)
```csv
brand,model
BrandName,Model 1
BrandName,Model 2
BrandName,Model 3
```

#### For YAML (`data/models.yaml`)
```yaml
BrandName:
- Model 1
- Model 2
- Model 3
```

### Guidelines

1. **Accuracy**: Ensure that the vehicle models you add are real and currently or previously manufactured
2. **Consistency**: Use proper capitalization and spelling for brand and model names
3. **No Duplicates**: Check that the model doesn't already exist before adding
4. **Alphabetical Order**: Try to maintain alphabetical order within brand model lists
5. **Brand Names**: Use the official brand name as it appears on the vehicles

### Automation

This repository uses GitHub Actions to automatically sync the three data formats. When you update any one of the data files, the workflow will automatically update the other two formats to keep them in sync.

### Questions or Issues?

If you have questions about contributing or notice any issues with the data, please:
1. Check existing issues first
2. Open a new issue if needed
3. Provide as much detail as possible

## Code of Conduct

Please be respectful and constructive in all interactions. This project welcomes contributions from everyone, regardless of background or experience level.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
