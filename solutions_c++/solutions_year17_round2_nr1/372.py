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

double x[N], v[N];
int d, n;

bool ver(double s) {

    for(int i = 1; i <= n; ++i) {
        if(v[i] >= s)
            continue;

        double t = x[i] / (s - v[i]);
        double p = t * s;

        if(p < d)
            return 0;
    }

    return 1;
}

void sol() {
    double r;

    cin >> d >> n;
    for(int i = 1; i <= n; ++i)
        cin >> x[i] >> v[i];

    double st = 0, dr = 1e13;

    for(int i = 1; i <= 200; ++i) {
        double mid = (st + dr) / 2;
        if(ver(mid))
            st = mid;
        else
            dr = mid;
    }

    out << fixed << setprecision(10) << st;
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
