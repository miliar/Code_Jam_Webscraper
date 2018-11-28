/// In the name of God
#include <bits/stdc++.h>
//#define int long long
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define y1 def1
#define X first
#define Y second
#define endl '\n'
#define all(o) o.begin(), o.end()
#define IOS ios::sync_with_stdio(0), cin.tie(0)

main(){
    IOS;
    freopen("AL.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int it=0; it<T; it++){
        cout << "Case #" << it+1 << ": ";
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        int n = s.size();
        string pat = string(n, '+');
        for(int i=0; i+k<=n; i++)
            if(s[i] != pat[i]){
                for(int j=i; j<i+k; j++)
                    s[j] = (s[j] == '+' ? '-' : '+');
                ans++;
            }
        if(s == pat)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}
