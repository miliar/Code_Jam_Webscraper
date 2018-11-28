#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void compute(ll N, ll cur, vector<ll>& res) {
    if(cur > N)
        return;
    if(cur > 0)
        res.push_back(cur);

    int digit = cur % 10;
    for(int i=digit;i<=9;++i)
        if(cur != cur * 10 +i)
            compute(N, cur * 10 + i, res);
}

ll solve(ll N, const vector<ll>& allTidy) {
    auto ansIter = lower_bound(allTidy.begin(), allTidy.end(), N);
    ll ans = *ansIter;
    if(*ansIter > N) {
        ans = *(ansIter-1);
    }
    return ans;
}

int main() {
    vector<ll> allTidy;
    compute(1e18, 0, allTidy);
    sort(allTidy.begin(), allTidy.end());

    int tc;
    cin >> tc;
    for(int ii=1;ii<=tc;++ii) {
        ll N;
        cin >> N;

        cout << "Case #" << ii << ": " << solve(N, allTidy) << endl;
    }
    return 0;
}
