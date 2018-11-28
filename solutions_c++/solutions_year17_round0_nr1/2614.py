#include <iostream>
#include <string>
using namespace std;

int tcase;
string cakes;
int k;

int main () {
    cin >> tcase;
    for (int t=0;t<tcase;t++)
    {
        int counter = 0;
        bool solveable = true;
        cin >> cakes;
        cin >> k;
        for (int i=0;i<cakes.length()-k+1;i++) {
            if (cakes[i] != '+') {
                counter++;
                for (int j=0;j<k;j++) {
                    if (cakes[i+j] == '+') {
                        cakes[i+j] = '-';
                    } else {
                        cakes[i+j] = '+';
                    }
                }
            }
        }
        for (int i=cakes.length()-k;i<cakes.length();i++) {
            if (cakes[i] == '-') {
                solveable = false;
                break;
            }
        }
        cout << "Case #" << t+1 << ": ";
        if (solveable) {
            cout << counter << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}