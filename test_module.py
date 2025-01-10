import pytest
from mean_var_std import calculate

def test_calculate_valid_input():
    # Input valid untuk matriks 3x3
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = calculate(numbers)
    
    # Memastikan struktur hasilnya sesuai yang diinginkan
    assert isinstance(result, dict)
    assert 'mean' in result
    assert 'variance' in result
    assert 'standard deviation' in result
    assert 'max' in result
    assert 'min' in result
    assert 'sum' in result

    # Memastikan nilai-nilai statistik yang benar
    assert result['mean'][2] == 4.0
    assert result['variance'][2] == 6.666666666666667
    assert result['standard deviation'][2] == 2.581988897471611
    assert result['max'][2] == 8
    assert result['min'][2] == 0
    assert result['sum'][2] == 36

def test_calculate_invalid_input():
    # Input tidak valid (kurang dari 9 elemen)
    numbers = [1, 2, 3, 4, 5, 6, 7]
    with pytest.raises(ValueError):
        calculate(numbers)
        
