#include <iostream>
#include <queue>
#include <string.h>
#include <cmath>

using namespace std;

long long int v[130];

int main(){

    long long int j, p, n, k, i, l, r;
    int t, pp, ll, rr, descarte, aux;
    priority_queue<long long int> fila;
    bool first;

    cin >> t;

    for (i = 1; i <= t; i++){
        cin >> n >> k;

        memset(v, 0, sizeof(v));

        fila.push(n);
        pp = (int)log2(n) * 2 + 3;
        v[pp]++;
        aux = pp - 1;
        first = true;

        for (j = 0; j < k; ){
            p = fila.top();
            fila.pop();

            if (p == 0) break;

            l = r = p/2;
            if ((l+r) == p) l--;

            if (pp%2 == 0){
                aux -= 2;
            }
            ll = rr = aux;

            if (((pp%2) == 0 && l != r) || ((pp%2) != 0)){
                ll--;
            }
            if ((pp%2) != 0 && l == r){
                rr--;
            }
            if (p == 2){
                rr = pp - 1;
                ll = rr - 1;
            }else if (p == 1){
                ll = rr = pp - 1;
            }

            if (first && ll == rr){
                ll = rr = pp - 2;
                aux = pp - 3;
            }else
                first = false;

            //cout << "LOG de " << p << " = " << pp << endl;
            //cout << "L = " << ll << " e R = " << rr << endl;

            if (v[rr] == 0) fila.push(r);
            v[rr] += v[pp];

            if (v[ll] == 0) fila.push(l);
            v[ll] += v[pp];

            //cout << "v[l] = " << v[ll] << " e v[r] = " << v[rr] << endl;
            //cout << "Salvou: l = " << l << " e r = " << r << "\n";
            //cin >> descarte;

            j += v[pp--];
            if (first) pp--;
            //cout << "J = " << j << "\n\n";
        }

        while(!fila.empty()){
            fila.pop();
        }

        cout << "Case #" << i << ": " << r << " " << l << endl;
    }
}
