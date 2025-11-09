# Elegant Petal Design Studio (petal.py)

An interactive Python application that creates beautiful, customizable flower patterns using the turtle graphics library. Create and save stunning petal designs with various patterns, color schemes, and special effects.

## Requirements

- Python 3.6+ (the `turtle` module is part of the Python standard library)
- A graphical environment (local desktop). The script opens a GUI window and will not display in headless environments.

## Quick Start

1. Open a terminal/PowerShell in the project folder
2. Run the script:
```powershell
python petal.py
```
3. Press 'h' to see the help menu with all controls

## Features

### Multiple Petal Patterns
- **Classic (A)**: Elegant curved petals with intricate detail lines
- **Curved (B)**: Flowing, nature-inspired design with overlapping curves
- **Pointed (C)**: Sophisticated pattern combining sharp points with elegant curves
- **Spiral (D)**: Intricate spiral design with varying thickness and decorative elements

### Color Schemes
1. **Rainbow**: Classic rainbow colors (red, orange, yellow, green, blue, indigo, violet)
2. **Sunset**: Warm, vibrant colors (coral, salmon, gold, orange-red)
3. **Ocean**: Cool blue tones (cyan, turquoise, sea green)
4. **Forest**: Natural green variations (forest green, lime, mint)

### Interactive Controls
| Key | Function |
|-----|----------|
| `h` | Show help menu |
| `1-4` | Switch color schemes |
| `a-d` | Change petal patterns |
| `+/-` | Adjust petal size |
| `</>`| Change number of petals |
| `g` | Toggle glitter effect |
| `s` | Save current design |
| `q` | Quit program |

## Design Tips

- Start with the classic pattern (press 'a') to get familiar with the controls
- Try different combinations:
  - Ocean colors (3) with spiral pattern (d) for a mesmerizing water-like effect
  - Sunset colors (2) with curved petals (b) for a tropical flower look
  - Forest scheme (4) with pointed petals (c) for a star-like leaf pattern
- Use smaller petal counts (12-24) for detailed patterns
- Use larger petal counts (36-48) for more intricate overall designs
- Add glitter effect as a final touch to add depth

## Saving Your Designs
When you press 's', your design will be saved as a PostScript file with a timestamp:
```
petal_design_YYYYMMDD_HHMMSS.ps
```

## Troubleshooting

- **Blank/No window**: Ensure you're running locally with a desktop session
- **"No module named turtle"**: Install a standard CPython distribution from python.org
- **File name conflicts**: Don't name your script `turtle.py` as it would conflict with the standard library

## License & Credits

This project is free to use and modify. Feel free to fork and add your own patterns, color schemes, or features!
