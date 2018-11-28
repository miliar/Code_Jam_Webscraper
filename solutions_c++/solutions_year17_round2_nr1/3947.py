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
#define eps 1e-9
using namespace std;
typedef long long ll;
typedef long double ld;

ld v[1003], s[1003];
ll d, n;
int ind[1003];
bool cmp(int a, int b){
    if (s[a] == s[b]) return v[a] > v[b];
    return s[a] < s[b];
}
bool chega(int a, int b){
    if (s[a] == s[b]) return true;
    if (v[a] == v[b]) return false;
    ld t = -(s[a] - s[b]) / (v[a] - v[b]);
    ld ss = s[a] + v[a] * t;
    return ss < d - eps;
}
int main(){
    ios::sync_with_stdio(false);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);

    int te;
    cin >> te;
    cout << setprecision(12);
    cout << fixed;
    int caso = 1;
    while (te--){
        cin >> d >> n;

        for (int i = 0; i < n; i++){
            cin >> s[i] >> v[i];
            ind[i] = i;
        }
        sort(ind, ind + n, cmp);
        int atual = ind[0];

        for (int i = 1; i < n; i++){
            if (chega(atual, ind[i])){
                atual = ind[i];
            }
        }

        ld tempo = (d - s[atual]) / v[atual];
        cout << "Case #" << caso << ": " << d / tempo << endl;
        caso++;
    }
    return 0;
}

