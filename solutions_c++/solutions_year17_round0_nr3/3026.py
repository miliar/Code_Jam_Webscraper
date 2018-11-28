#include <bits/stdc++.h>

using namespace std;

map<pair<long long, long long>, pair<long long, long long>> a;

pair<long long, long long> getans(long long n, long long k){
    //cerr << n << " " << k << endl;
    if(a[make_pair(n, k)] == make_pair(0ll, 0ll)){
        if(k == 0) return {n + 1, n + 1};
        if(k == 1) return {n / 2 + 1, (n - 1) / 2 + 1};
        pair<long long, long long> lans = getans(n / 2, k / 2), rans = getans((n - 1) / 2, (k - 1) / 2);
        a[{n, k}].first = min(lans.first, rans.first);
        a[{n, k}].second = min(lans.second, rans.second);
    }
    return a[{n, k}];
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long t, n, k;
    cin >> t;
    for(int z = 0; z < t; z++){
        cin >> n >> k;
        pair<long long, long long> ans = getans(n, k);
        ans.first--, ans.second--;
        cout << "Case #" << z + 1 << ": " << ans.first << " " << ans.second << endl;
    }
    return 0;
}
