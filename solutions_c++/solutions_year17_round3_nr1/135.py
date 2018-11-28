#include <bits/stdc++.h>
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
        int n, k;
        in >> n >> k;
        ll z = 0;
        pair<ll, ll> a[1003] = {};
        fr(n) in >> a[i].first >> a[i].second;
        fr(n) {
            vector<ll> v;
            for (int j = 0; j < n; j++) if (i != j && a[j].first <= a[i].first) v.push_back(2 * a[j].first * a[j].second);
            sort(v.begin(), v.end(), greater<ll>());
            ll s = 0;
            for (int j = 0; j < min(k - 1, (int)v.size()); j++) s += v[j];
            //fr(v.size()) cout << v[i] << ' '; cout << '\n';
            //cout << a[i].first << ' ' << s << '\n';
            z = max(z, a[i].first * (a[i].first + 2 * a[i].second) + s);
        }
        out << fixed << setprecision(13) << z * 3.14159265358979 << '\n';
    }
}
