#include <bits/stdc++.h>

using namespace std;

string s[25];

void rec(int i1, int j1, int i2, int j2){
    int i, j, count = 0;
    int posx1, posy1, posx2, posy2;
    char symb1, symb2;
    for (i = i1; i <= i2; i++){
        for (j = j1; j <= j2; j++){
            if (s[i][j] >= 'A' && s[i][j] <= 'Z' && count == 0){
                count = 1;
                symb1 = s[i][j];
                posx1 = i;
                posy1 = j;
            } else
            if (s[i][j] >= 'A' && s[i][j] <= 'Z' && count == 1){
                count = 2;
                symb2 = s[i][j];
                posx2 = i;
                posy2 = j;
            }
        }
    }
    if (count == 1){
        for (i = i1; i <= i2; i++){
            for (j = j1; j <= j2; j++){
                s[i][j] = symb1;
            }
        }    
        return;
    } else
    {
        if (posx1 < posx2){
            rec(i1, j1, posx1, j2);
            rec(posx1 + 1, j1, i2, j2);
        } else
        if (posy1 < posy2){
            rec(i1, j1, i2, posy1);
            rec(i1, posy1 + 1, i2, j2);
        }
    }
    return;
}

int main(){
    long long i,j,k,l,m,n,test,t;
    cin >> test;
    for (t = 0; t < test; t++){
        cin >> n >> m;
        cout << "Case #" << t + 1 << ":\n";
        for (i = 0; i < n; i++){
            cin >> s[i];
        }
        rec(0, 0, n - 1, m - 1);
        for (i = 0; i < n; i++){
            cout << s[i] << "\n";
        }
    }
    return 0;
}
