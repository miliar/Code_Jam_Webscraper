#include <iostream>

using namespace std;

//ifstream cin ("B.in");
//ofstream cout ("B.out");

const int CIFMAX = 20;
int T;
long long N;
int v[CIFMAX], cif;

int main () {
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> N;
        cif = 0;
        while (N) {
            v[++cif] = N % 10;
            N /= 10;
        }

        int flag = 0;
        for (int i = cif; i >= 2 && !flag; i--) {
            if (v[i] > v[i - 1]) {
                flag = 1;
                if (v[i] - 1 >= v[i + 1]) {
                    v[i]--;
                    if (i == cif && v[i] == 0) cif--;
                    for (int j = i - 1; j >= 0; j--) {
                        v[j] = 9;
                    }
                }
                else {
                    int j = i + 1;
                    while (j < cif && v[j] == v[j + 1]) {
                        j++;
                    }
                    if (j > cif) {
                        j = cif;
                    }
                    v[j]--;
                    if (j == cif && v[j] == 0) cif--;
                    i = j;
                    for (int j = i - 1; j > 0; j--) {
                        v[j] = 9;
                    }
                }
            }
        }

        cout << "Case #" << t << ": ";
        for (int i = cif; i > 0; i--) {
            cout << v[i];
        }
        cout << '\n';
    }

    return 0;
}
