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
ll pd[723][723][3][2];
ll t[1500];
ll solve(int a, int b, int quem, int comeca){
    if (a > 720) return inf;
    if (b > 720) return inf;
    if (a == 720 && b == 720){
        return comeca != quem;
    }

    ll &ret = pd[a][b][quem][comeca];
    if (ret != -1) return ret;

    ret = inf;
    if (t[a + b] != 1) ret = min(ret, solve(a + 1, b, 0, comeca) + (quem == 1));
    if (t[a + b] != 2) ret = min(ret, solve(a, b + 1, 1, comeca) + (quem == 0));
    return ret;
}
int main(){
    ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("ou", "w", stdout);

    int te;
    cin >> te;
    int caso = 1;
    while(te--){
        memset(t, 0, sizeof(t));
        int ac, aj;
        cin >> ac >> aj;
        int c, d;
        for (int i = 0; i < ac; i++){
            cin >> c >> d;
            for (int j = c; j < d; j++){
                t[j] = 1;
            }
        }
        for (int i = 0; i < aj; i++){
            cin >> c >> d;
            for (int j = c; j < d; j++){
                t[j] = 2;
            }
        }
        memset(pd, -1, sizeof(pd));
        ll r1 = inf, r2 = inf;
        if (t[0] != 1) r1 = solve(1, 0, 0, 0);
        if (t[0] != 2) r2 = solve(0, 1, 1, 1);
        cout << "Case #" << caso << ": " << min(r1, r2) << endl;
        caso++;
    }
    return 0;
}

