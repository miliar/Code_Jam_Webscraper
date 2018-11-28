#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void actualiza_ls(vector<int> &ls, vector<bool> &puertas) {
    int n = (int)puertas.size()-2;
    int ultima_ocupada = 0;
    for (int i = 1; i <= n; i++) {
        ls[i] = abs(ultima_ocupada - i) - 1;
        if (puertas[i]) {
            ultima_ocupada = i;
        }
    }
}

void actualiza_rs(vector<int> &rs, vector<bool> &puertas) {
    int n = (int)puertas.size()-2;
    int ultima_ocupada = n+1;
    for (int i = n; i >= 1; i--) {
        rs[i] = abs(i - ultima_ocupada) - 1;
        if (puertas[i]) {
            ultima_ocupada = i;
        }
    }
}

int mas_cercano(vector<int> &ls, vector<int> &rs, int i) {
    return min(ls[i], rs[i]);
}

int mas_lejano(vector<int> &ls, vector<int> &rs, int i) {
    return max(ls[i], rs[i]);
}

int main() {
    int T,  TOT;
    cin >> T;
    TOT = T;

    while (T--) {
        int n, k;
        cin >> n >> k;
        // cout << "n: " << n << "  k: " << k << "\n";
        vector<bool> puertas(n+2, false);
        puertas[0] = true;
        puertas[n+1] = true;
        
        vector<int> LS(n+2, 0);
        vector<int> RS(n+2, 0);

        actualiza_ls(LS, puertas);
        actualiza_rs(RS, puertas);

        int ultimo_lejano = 0;
        int ultimo_cercano = 0;

        int ultima_puerta = -1;

        for (int persona = 1; persona <= k; persona++) {

            int max_mascercano = -1;
            int max_maslejano = -1;
            int nueva_puerta = -1;

            // elijo la puerta en la que va a entrar la persona
            for (int puerta = 1; puerta <= n; puerta++) {

                if (puertas[puerta]) {
                    continue;
                }

                int actual_mascercano = mas_cercano(LS, RS, puerta);
                int actual_maslejano = mas_lejano(LS, RS, puerta);

                if (actual_mascercano > max_mascercano) {
                    max_mascercano = actual_mascercano;
                    max_maslejano = actual_maslejano;
                    nueva_puerta = puerta;                    
                }

                else if (actual_mascercano == max_mascercano) {
                    if (actual_maslejano > max_maslejano) {
                        max_mascercano = actual_mascercano;
                        max_maslejano = actual_maslejano;
                        nueva_puerta = puerta;
                    }
                } 

            }

            // cout << "nueva puerta: " << nueva_puerta << "\n";

            puertas[nueva_puerta] = true;    
            actualiza_ls(LS, puertas);
            actualiza_rs(RS, puertas);

            if (persona == k) {
                ultimo_cercano = mas_cercano(LS, RS, nueva_puerta);
                ultimo_lejano = mas_lejano(LS, RS, nueva_puerta);
            }

        }

        cout << "Case #" << TOT-T << ": " << ultimo_lejano << " " << ultimo_cercano << "\n";
    }





    return 0;
}