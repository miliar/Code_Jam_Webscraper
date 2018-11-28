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

const int N = 1010;

int n, c, m, tmin;
int nr[N], s[N];

int ver(int r, int cc) {
    int i, last = 0, elm = 0;

    for(i = n; i; --i) {
        if(nr[i] > r) {
            last += nr[i] - r;

            elm += nr[i] - r;
        }
        else {
            last = max(0, last - (r - nr[i]));
        }
    }

    if(cc)
        return elm;

    return !last;
}

void sol() {
    int i, j, k;

    tmin = 0;
    memset(s, 0, sizeof(s));
    memset(nr, 0, sizeof(nr));

    cin >> n >> c >> m;

    for(i = 1; i <= m; ++i) {
        int a, b;
        cin >> a >> b;

        s[b]++;
        nr[a]++;
        tmin = max(tmin, s[b]);
    }

    int pas = 1024;
    --tmin;

    for(; pas; pas /= 2)
        if(!ver(tmin + pas, 0))
            tmin += pas;

    out << tmin + 1 << " " << ver(tmin + 1, 1);
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
