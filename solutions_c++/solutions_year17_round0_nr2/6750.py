// Problem B - Tidy Numbers
// Google Code Jam 2017 - Fase classificatória
//
// Estratégia: achar o digito mais significativo onde a tidyness é quebrada
// e fazer N[até este dígito] - 1

#include <iostream>
#include <cmath>

#define DEBUG false
using namespace std;

typedef unsigned long ul;
void solver(int test_num);


int main(void) {
    // Le numero de testes
    int num_tests;
    cin >> num_tests;
    if (DEBUG) {
        cout << "Número de testes: " << num_tests << endl;
    }

    for (int i = 0; i < num_tests; i++) {
        solver(i+1);
    }
    return 0;
}

ul make_it_tidy(ul N) {
    // Achar o primeiro digito que quebra a tidyness
    int m = floor(log10(N)); // Magnitude
    int last_digit = 0;
    ul tidy_number = 0;
    for (; m >= 0; m--) {
        ul base = (ul) pow10l(m);
        int digit = (N / base) - (tidy_number / base); // Divisao inteira de N pela base
        if (digit >= last_digit) {
            tidy_number += (digit * base);
            last_digit = digit;
        }
        else break;
    }
    if (DEBUG) cout << "Tidy number: " << tidy_number << endl;
    // Se p for menor que 0, então o numero original jã era tidy_number
    if (m < 0) return tidy_number;
    else return (tidy_number - 1);
}

void solver(int test_num) {
    // Le entrada do Problema
    string case_num = "Case #" + to_string(test_num) + ": ";
    ul N;
    cin >> N;
    if (DEBUG) {
        cout << case_num << endl;
        cout << "N: " << N << endl;
    }

    ul tidy_number = N;
    while(true) {
        ul new_tidy = make_it_tidy(tidy_number);
        if (tidy_number - new_tidy > 0) tidy_number = new_tidy;
        else break;
    }
    cout << case_num << tidy_number << endl;

    return;
}
