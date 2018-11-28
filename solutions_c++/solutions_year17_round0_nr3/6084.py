#include <bits/stdc++.h>

using namespace std;

#define FROM_FILE freopen("input.txt", "r", stdin)
#define TO_FILE freopen("output.txt", "w", stdout)

#define ull unsigned long long
#define ll long long

#define pb push_back
#define mp make_pair

#define PI 3.1415926535
#define INF 1e9
#define EPS 1e-6
#define prv(v) for (int iqiq = 0; iqiq < v.size(); iqiq++) cout << v[iqiq] << " "; cout << "\n"


pair<ll,ll> solve(ll n, ll k)
{
    vector<ll> hp = { n };
    make_heap(hp.begin(), hp.end());
    while (k-- > 1) {
        ll cur = hp.front();
        pop_heap(hp.begin(), hp.end());
        hp.pop_back();

        if (cur % 2)
            hp.push_back(cur / 2);
        else
            hp.push_back(cur / 2 - 1);
        push_heap(hp.begin(), hp.end());
        hp.push_back(cur / 2);
        push_heap(hp.begin(), hp.end());
    }

    ll res = hp.front();
    ll right = res / 2;
    ll left = res / 2;
    if (res % 2 == 0)
        left -= 1;
    return { max(left, right), min(left, right) };
}

int main()
{
    FROM_FILE;
    TO_FILE;

    int tt;
    cin >> tt;
    for (int Case = 1; Case <= tt; Case++) {
        ll n, k;
        cin >> n >> k;
        pair<ll,ll> pr = solve(n, k);
        cout << "Case #" << Case << ": " << pr.first << " " << pr.second << "\n";
    }

    return 0;
}
