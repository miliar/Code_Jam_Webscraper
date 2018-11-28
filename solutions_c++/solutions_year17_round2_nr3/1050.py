#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#define ll long long int
#define mod 1000000007
#define pii pair<int, int>
#define fr(n) for (int i = 0; i < n; i++)
#define fr1(n) for (int i = 1; i <= n; i++)
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int T;
    in >> T;
    for (int U = 1; U <= T; U++) {
        out << "Case #" << U << ": ";
        ll n, d[102][102] = {}, e[102] = {}, s[102] = {}, c[102] = {};
        long double z[102] = {};
        fr(102) z[i] = (ll)mod * mod;
        in >> n >> e[0];
        fr1(n) in >> e[i] >> s[i];
        fr1(n) for (int j = 1; j <= n; j++) in >> d[i][j];
        in >> e[0] >> s[0];
        fr1(n - 1) c[i + 1] = c[i] + d[i][i + 1];
        //fr1(n) cout << c[i] << '\n';
        z[1] = 0;
        fr1(n) for (int j = 1; j < i; j++) {
            if (c[i] - c[j] > e[j]) continue;
            z[i] = min(z[i], z[j] + (long double)(c[i] - c[j]) / s[j]);
        }
        //fr1(n) cout << z[i] << ' ';
        out << fixed << setprecision(13) << z[n] << '\n';
    }
}
