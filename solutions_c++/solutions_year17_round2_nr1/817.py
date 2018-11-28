#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e5 + 10;

long double dist;
int n;

void sol(int cs) {
    double n, m;
    vector <pair <long double, long double> > v;
    cin >> dist >> n;
    for(int i = 1; i <= n; i++) {
        long double a, b;
        cin >> a >> b;
        v.push_back(make_pair(a, b));
    }
    sort(v.begin(), v.end());
    long double l = 0, r = 1000000000000000;
    while(r - l >= 0.000001) {
        long double mid = (l + r) / 2;
        int q = 0;
        long double tim = dist / mid;
        for(int i = 0; i < n; i++) {
            if(tim * v[i].S + v[i].F < dist) q = 1;
        }
        if(q) {
            r = mid;
        } else {
            l = mid;
        }
    }
    cout << "Case #" << cs << ": ";
    printf("%.7Lf", l);
    cout << endl;
}

main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    //ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        sol(i);
    }
}
