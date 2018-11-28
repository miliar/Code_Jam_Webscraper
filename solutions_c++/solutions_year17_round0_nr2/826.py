#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll n, t;

bool comp(vector<ll> a, vector<ll> b) {
    assert(a.size() == b.size());
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] == b[i])
            continue;
        if (a[i] < b[i])
            return 1;
        if (a[i] > b[i])
            return 0;
    }
    return 1;
}

void prt(vector<ll> a) {
    ll x = 0;
    for (int i = 0; i < a.size(); ++i)
        x = 10*x + a[i];
    cout << x << endl;
}

void doit(int abc) {
    cout << "Case #" << abc+1 << ": ";
    cin >> n;
    vector<ll> v;
    while (n != 0) {
        v.push_back(n%10);
        n /= 10;
    }
    reverse(v.begin(), v.end());
    vector<ll> w = v;
    for (int i = 0; i < v.size(); ++i) {
        for (int j = i; j < v.size(); ++j)
            w[j] = v[i];
        if (comp(w, v))
            continue;
        else {
            w[i] = v[i]-1;
            for (int j = i+1; j < v.size(); ++j)
                w[j] = 9;
            break;
        }
    }

    prt(w);
}

int main() {
    cin >> t;
    for (int i = 0; i < t; ++i)
        doit(i);
}