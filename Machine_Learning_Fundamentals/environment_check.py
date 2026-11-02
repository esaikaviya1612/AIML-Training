import sys
import importlib

print("=" * 55)
print("MACHINE LEARNING ENVIRONMENT CHECK")
print("=" * 55)

print(f"\nPython Version:\n{sys.version}")
print(f"\nPython Executable:\n{sys.executable}")

libraries = {
    "NumPy": "numpy",
    "Pandas": "pandas",
    "Matplotlib": "matplotlib",
    "Seaborn": "seaborn",
    "Scikit-learn": "sklearn",
}

print("\nCHECKING REQUIRED LIBRARIES")
print("-" * 55)

all_available = True

for library_name, module_name in libraries.items():
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "Unknown")

        print(f"[OK] {library_name}")
        print(f"     Version: {version}")

    except ImportError:
        print(f"[ERROR] {library_name} is not available")
        all_available = False

print("-" * 55)

if all_available:
    print("STATUS: ENVIRONMENT READY")
else:
    print("STATUS: ENVIRONMENT CHECK FAILED")

print("=" * 55)