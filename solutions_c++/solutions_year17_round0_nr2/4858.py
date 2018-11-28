#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cmath>
using namespace std;

string imprimirNueves (int x) {
    string res = "";
    for (int i = 0; i < x; i++) {
        res += '9';
    }
    return res;
}

int main () {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int t;
    cin >> t;
    
    string n;
    for (int tc = 1; tc <= t; tc++) {
        cin >> n;
        int len = n.size();
        
        cout << "Case #" << tc << ": ";
        
        // obtengo el k, tal que n[k] es el primero n[k] > n[k+1]
        int k = -1;
        for (int i = 0; i < len - 1; i++) {
            if (n[i] > n[i+1]) {
                k = i;
                break;
            }
        }
        
        // si nunca encontre un k, el string original estaba bien
        if (k == -1) {
            cout << n << endl;
            continue;
        }
        
        // busco j tal que n[j+1] = ... = n[k], y n[j] != n[k] (o j = -1)
        int j = k - 1;
        while (j >= 0 && n[j] == n[k]) {
            j--;
        }
        
        if (j == -1) {
            // son todos iguales hasta el k-ésimo, y después baja
            if (n[0] == '1') {
                cout << imprimirNueves(n.size() - 1) << endl;
            }
            else {
                cout << (char) (n[0] - 1) << imprimirNueves(len - 1) << endl;
            }
        }
        else {
            // 0..j , j+1, j+2 .. len-1 ---> len-1 - j-2 +1 = len-j-2
            cout << n.substr(0,j+1) << (char) (n[j+1] - 1) << imprimirNueves(len-j-2) << endl;
        }
    }
}

