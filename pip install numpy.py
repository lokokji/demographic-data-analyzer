pip install numpy
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
import numpy as np

def calculate(numbers):
    # Step 1: Periksa apakah list memiliki 9 elemen
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Step 2: Konversi list menjadi matriks 3x3 menggunakan numpy
    matrix = np.array(numbers).reshape(3, 3)
    
    # Step 3: Hitung statistik
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    max_vals = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    min_vals = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    sum_vals = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    
    # Step 4: Kembalikan hasil dalam format dictionary
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_vals,
        'min': min_vals,
        'sum': sum_vals
    }
python3 main.py


