#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef long double ld;

const ld EPS = 1e-9;

const ll llinf = 1e18 + 100;

const int maxn = 2e5 + 100, inf = 1e9 + 100;

int tst, n, p;

int q[101][101][101][101][4];

int a[4];

int main()
{
    #ifdef ONPC
    ifstream cin("a.in");
    ofstream cout("a.out");
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
	    #ifndef STR
	    //ifstream cin("a.in");
	    //ofstream cout("a.out");
	    //freopen("a.in", "r", stdin);
	    //freopen("a.out", "w", stdout);
    	    #endif // STR
    #endif // ONPC
    ios::sync_with_stdio(0);
    cin >> tst;
    for (int iter = 1; iter <= tst; iter++){
        cin >> n >> p;
        for (int i = 0; i < 101; i++)
            for (int j = 0; j < 101; j++)
            for (int k = 0; k < 101; k++)
            for (int z = 0; z < 101; z++)
            for (int f = 0; f < 4; f++)
                q[i][j][k][z][f] = 0;
        for (int i = 0; i < 4; i++)
            a[i] = 0;
        for (int i = 0; i < n; i++){
            int x;
            cin >> x;
            a[x % p]++;
        }
        q[a[0]][a[1]][a[2]][a[3]][0] = 1;
        int answer = 0;
        for (int sum = n; sum >= 0; sum--)
            for (int i0 = 0; i0 <= a[0]; i0++)
                for (int i1 = 0; i1 <= a[1] && i1 + i0 <= sum; i1++)
                for (int i2 = 0; i2 <= a[2] && i1 + i0 + i2 <= sum; i2++){
                    int i3 = sum - i1 - i2 - i0;
                    if (i3 > a[3])
                        continue;
                    for (int rem = 0; rem < p; rem++)
                        if (q[i0][i1][i2][i3][rem] > 0){
                            int val = q[i0][i1][i2][i3][rem];
                            answer = max(answer, val);
                            int s;
                            if (i0 > 0){
                                s = rem - 0;
                                if (s < 0)
                                    s += p;
                                q[i0 - 1][i1][i2][i3][s] = max(q[i0 - 1][i1][i2][i3][s], val + (rem == 0));
                            }
                            if (i1 > 0){
                                s = rem - 1;
                                if (s < 0)
                                    s += p;
                                q[i0][i1 - 1][i2][i3][s] = max(q[i0][i1 - 1][i2][i3][s], val + (rem == 0));
                            }
                            if (i2 > 0){
                                s = rem - 2;
                                if (s < 0)
                                    s += p;
                                q[i0][i1][i2 - 1][i3][s] = max(q[i0][i1][i2 - 1][i3][s], val + (rem == 0));
                            }
                            if (i3 > 0){
                                s = rem - 3;
                                if (s < 0)
                                    s += p;
                                q[i0][i1][i2][i3 - 1][s] = max(q[i0][i1][i2][i3 - 1][s], val + (rem == 0));
                            }
                        }
                }
        cout << "Case #" << iter << ": " << answer - 1 << '\n';
    }
}
