// Problem A - Oversized Pancake Flipper
// Google Code Jam 2017 - Fase classificatória
//
// Estratégia: algoritmo guloso no uso do "pancake flipper"

#include <iostream>
#include <vector>

#define DEBUG false 
void pancake_flipper(int test_num);

using namespace std;

int main(void) {
    // Le numero de testes
    int num_tests;
    cin >> num_tests;
    if (DEBUG) {
        cout << "Número de testes: " << num_tests << endl;
    }

    for (int i = 0; i < num_tests; i++) {
        pancake_flipper(i+1);
    }
    return 0;
}

void pancake_flipper(int test_num) {
    // Le entrada do Problema
    int pancake;
    vector<bool> pancakes;    // Convencao: true == happy_side; false == blank
    string case_num = "Case #" + to_string(test_num) + ": ";
    if (DEBUG) cout << case_num << endl;
    do {
        pancake = getchar();
        if (pancake == '+') pancakes.push_back(true);
        else if (pancake == '-') pancakes.push_back(false);
    } while (pancake != ' ');
    if (DEBUG) {
      cout << "Panquecas: ";
      for (int i = 0; i < pancakes.size(); i++) {
          cout << pancakes[i] << " ";
      }
      cout << endl;
    }
    int K_flipper_size;
    cin >> K_flipper_size;
    if (DEBUG) cout << "Tamanho da pa: " << K_flipper_size << endl;

    // A cada panqueca blank, aplica flip desta panqueca até ela + K
    int pancakes_limit = pancakes.size() - K_flipper_size;
    int num_flips = 0;
    for (int i = 0; i <= pancakes_limit; i++) {
        // Se a panqueca é blank, aplica flip nas próximas K pankecas
        if (pancakes[i] == false) {
            num_flips++;
            for (int j = i; j < i + K_flipper_size; j++) {
                pancakes[j] = !pancakes[j];
            }
        }
    }
    if (DEBUG) {
        cout << "Panquecas flip: ";
        for (int i = 0; i < pancakes.size(); i++)
            cout << pancakes[i];
        cout << endl;
    }
    // Se alguma das panquecas de pancakes_limit até o final de pancakes
    // for falsa, então é impossível
    for (int i = pancakes_limit; i < pancakes.size(); i++) {
        if (pancakes[i] == false) {
            cout << case_num << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << case_num << num_flips << endl;

    return;
}
