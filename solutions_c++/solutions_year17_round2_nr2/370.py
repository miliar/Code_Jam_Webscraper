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

char r[1000000];

void sol() {
    int n, x[7], p = 0;

char C[7] = {'R', 'O', 'Y', 'G', 'B', 'V'};
    cin >> n >> x[0] >> x[1] >> x[2] >> x[3] >> x[4] >> x[5];

    if(x[2] > x[0]) {
        swap(x[2], x[0]);
        swap(C[2], C[0]);
    }
    if(x[4] > x[0]) {
        swap(x[4], x[0]);
        swap(C[4], C[0]);
    }

    int l;
    while(x[0] || x[2] || x[4]) {
        if(x[0]) {
            --x[0];
            r[p++] = C[0];

            if(!x[2] && !x[4]) {
                out << "IMPOSSIBLE";
                return;
            }

            if(x[2] > x[4]) {
                --x[2];
                r[p++] = C[2];
                l = 2;
            }
            else {
                --x[4];
                r[p++] = C[4];
                l = 4;
            }
        }
        else {
            l = 6 - l;
            if(!x[l]) {
                out << "IMPOSSIBLE";
                return;
            }
            --x[l];
            r[p++] = C[l];
        }
    }
r[p] = 0;
    out << r;
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
