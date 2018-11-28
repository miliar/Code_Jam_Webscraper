#include <bits/stdc++.h>
using namespace std;

int t, K, dir[1005], f[1005];
string s;

int calc(int K)
{
    memset(f, 0, sizeof(f));
    int res=0, sum=0;
    for(int i=0; i+K<=s.length(); i++) {
        if((dir[i]+sum)%2 != 0) {
            res++;
            f[i] = 1;
        }
        sum += f[i];
        if(i-K+i>=0) sum -= f[i-K+1];
    }

    for(int i=s.length()-K+1; i<s.length(); i++) {
        if((dir[i]+sum)%2 != 0) return -1;
        if(i-K+1>=0) sum -= f[i-K+1];
    }

    return res;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    ifstream cin("C:\\Users\\Jeremy\\Desktop\\Input.in");
    ofstream cout("C:\\Users\\Jeremy\\Desktop\\Output.txt");
    cin >> t;
    for(int i=1; i<=t; i++) {
        cin >> s;
        for(int i=0; i<s.length(); i++) dir[i] = (s[i]=='+') ? 0 : 1;
        cin >> K;
        int ans = calc(K);
        if(ans>=0) cout << "Case #" << i << ": " << ans << '\n';
        else cout << "Case #" << i << ": IMPOSSIBLE" << '\n';
    }

    return 0;
}
