#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N, mx;

void solve(int start, ll out, int n){
    if (n == 0){
        if(out <= N)
            mx = max(mx, out);
        return;
    }
    for (int i = start; i <= 9; i++){
        ll temp = out;
        temp = (temp*10LL) + i;
        solve(i, temp, n - 1);
    }
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t;
    cin >> t;
    for(int cs=1;cs<=t;++cs){
        cin >> N;
        mx = 0LL;
        string s = to_string(N);
        solve(0, 0, (int)s.size());
        cout << "Case #" << cs << ": " << mx << endl;
    }
    return 0;
}
