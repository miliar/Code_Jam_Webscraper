#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
using namespace std;

ofstream out("tttt");

const int N = 104;

int d[N][N][N];
int n, x[4], p;

int ver(int a, int b, int c) {
    if((a + 2 * b + 3 * c) % p == 0)
        return 1;
    return 0;
}

void sol() {
    cin >> n >> p;

    x[0] = x[1] = x[2] = x[3] = 0;

    for(int i = 1; i <= n; ++i) {
        int a;
        cin >> a;
        x[a%p]++;
    }

    for(int i = 0; i <= x[1]; ++i) {
        for(int j = 0; j <= x[2]; ++j) {
            for(int k = 0; k <= x[3]; ++k) {
                if(!i && !j && !k) {
                    d[i][j][k] = x[0];
                    continue;
                }

                int t = 0;
                if(i)
                    t = max(t, d[i - 1][j][k] + ver(i - 1, j, k));
                if(j)
                    t = max(t, d[i][j - 1][k] + ver(i, j - 1, k));
                if(k)
                    t = max(t, d[i][j][k - 1] + ver(i, j, k - 1));

                d[i][j][k] = t;
            }
        }
    }
    out << d[x[1]][x[2]][x[3]];
}

int main() {
    freopen("ttt", "r", stdin);
    //freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        out << "Case #" << a << ": ";
        sol();
		out << "\n";

        printf("Test %d\n", a);
    }

    return 0;
}
