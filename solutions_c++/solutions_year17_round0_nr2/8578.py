#include <bits/stdc++.h>
using namespace std;
#define int long long
int answ[10000000];
int32_t main() {
    int t;
    cin >> t;
    vector<int> queries;
    for (int tt = 1; tt <= t; tt++) {
        int k;
        cin >> k;
        queries.push_back(k);
    }
    int k = *max_element(queries.begin(), queries.end());
    cerr << k << endl;

    for (int nn = 1; nn <= k; nn++) {
        int n = nn;
        vector<int> digits;
        while (n > 0) {
            digits.push_back(n%10);
            n/=10;
        }
        reverse(digits.begin(), digits.end());
        answ[nn]=answ[nn - 1];
        if (is_sorted(digits.begin(), digits.end())) 
            answ[nn]	 =nn;
    }
    for (int i = 0; i < queries.size(); i++) {

        cout << "Case #" << 1+i << ": " << answ[queries[i]] << endl;
    }

}
