#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

#define F first
#define S second
#define inf INT_MAX
#define INF LONG_LONG_MAX
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()

string flip(string s, int start, int k){
    for(int i = start; i < start+k; i++){
        if(s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
    }
    return s;
}

bool check(string s){
    for(int i=0; i < s.size(); i++){
        if(s[i]=='-')
            return 0;
    }
    return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cnt = 1;
    cin >> t;
    while(t--){
        int k;
        string s;
        cin >> s >> k;
        int ans = 0;
        for(int i = 0; i < s.size(); i++){
            if(s[i]=='-'&& s.size()-i>=k)
                s=flip(s, i, k), ans++;
        }
        if(check(s))
            cout << "Case #" << cnt++ << ": " << ans << endl;
        else
            cout << "Case #" << cnt++ << ": IMPOSSIBLE"<< endl;
    }
    return 0;
}
