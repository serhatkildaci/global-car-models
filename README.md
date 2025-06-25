# Global Vehicle Models List

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub contributors](https://img.shields.io/github/contributors/yourusername/global-car-models.svg)](https://github.com/yourusername/global-car-models/graphs/contributors)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/global-car-models.svg)](https://github.com/yourusername/global-car-models/stargazers)

This repository contains a comprehensive list of vehicle models, organized by brand. The data is available in three formats: CSV, JSON, and YAML.

## 🚗 Features

- **Comprehensive Data**: Extensive list of vehicle models from various manufacturers
- **Multiple Formats**: Available in JSON, CSV, and YAML formats
- **Auto-Sync**: GitHub Actions automatically keeps all formats synchronized
- **Open Source**: MIT licensed and community-driven
- **Easy Integration**: Simple data formats for easy integration into projects

## Automation

This repository is fully automated using GitHub Actions. When you update and push a change to any of the data files (`data/models.json`, `data/models.csv`, or `data/models.yaml`), a workflow is triggered to automatically update the other two formats.

This ensures that all three data files remain in sync.

## Data Formats

### JSON (`data/models.json`)

The JSON file is structured as a dictionary where each key is a vehicle brand and the value is a list of models for that brand.

```json
{
    "Abarth": [
        "124 Spider",
        "500",
        "595",
        "695",
        "Punto Evo"
    ],
    "Acura": [
        "CL",
        "CSX",
        ...
    ]
}
```

### CSV (`data/models.csv`)

The CSV file contains two columns: `brand` and `model`.

```csv
brand,model
Abarth,124 Spider
Abarth,500
...
```

### YAML (`data/models.yaml`)

The YAML file has a structure similar to the JSON file.

```yaml
Abarth:
- 124 Spider
- 500
...
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to add new vehicle models or brands.

To add a new vehicle model or brand, you can edit any of the three data files and submit a pull request. The automation will take care of updating the other files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you find this project useful, please consider giving it a ⭐ on GitHub!
