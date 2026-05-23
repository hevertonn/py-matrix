# PyMatrix

Python script for manipulating images in **PBM** format using basic matrix operations.

> Project developed as part of the **Analytic Geometry and Vector Calculus** course in the **Computer Science - UESB** program.

---

## Objective

From an image in **PBM** format, this script applies transformations that reorganize pixel positions through the following matrix operations:

- **Transposition**
- **Row permutation**
- **Column permutation**

Combinations of these operations are also used.

After execution, **8 distinct images** will be created in the `output/` folder, located in the same directory as the script.

---

## How to Run

> Requirements: Python 3.9+ and `pip`

1. **Clone the repository:**
``` bash
git clone https://github.com/hevertonn/matrix-script.git
cd matrix-script
```

2. **Install the dependencies:**
``` bash
pip install -r requirements.txt
```

3. **Run the script:**
``` bash
python main.py path/to/your/image.pbm
```

---

## License
This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
