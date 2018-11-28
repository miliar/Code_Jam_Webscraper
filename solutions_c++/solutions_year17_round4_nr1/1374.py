#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"
#define cv(c) (int)(c-'a')
#define db(x) cerr << #x << ": " << x << " "
#define db2(x, y) cerr << #x << ": " << x << " " << #y << ": " << y << " "
#define bn() cerr << endl
#define sep() cerr << "-------" << endl
#define inf 1000000002
#define linf 1000000000000000002

using namespace std;
typedef long long ll;
typedef long double ld;

int v[10];
int main(){
    ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("ou", "w", stdout);

    int te;
    cin >> te;
    int caso = 1;
    while (te--){
        int n, p;

        cin >> n >> p;
        memset(v, 0, sizeof(v));
        for (int i = 0; i < n; i++){
            int a;
            cin >> a;
            v[a % p]++;
        }
        int atual = 0;
        int res = v[0];
        for (int i = 1; i < p; i++){
            if (p - i == i){
                int mn = v[i] / 2;
                res += mn;
                v[i] -= mn * 2;
                continue;
            }
            int mn = min(v[i], v[p - i]);
            res += mn;
            v[i] -= mn;
            v[p - i] -= mn;
        }
        if (p == 4){
            int sobra = v[1] + v[3];
            int sub = min(v[2], sobra / 2);
            res += sub;
            v[2] -= sub;
            v[1] = max(0, v[1] - 2 * sub);
            v[3] = max(0, v[3] - 2 * sub);
        }
        int tira = v[1] / p;
        res += tira;
        v[1] -= tira * p;
        tira = v[p - 1] / p;
        res += tira;
        v[p - 1] -= tira * p;
        int soma = 0;
        for (int i = 1; i < p; i++){
            if (v[i]) soma = 1;
        }
        res += soma;
        cout << "Case #" << caso << ": " << res << endl;
        caso++;
    }

    return 0;
}

