#include <bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
typedef long long ll;

const int MAX = 22;
string s;
int n;
int dp[MAX][10][2];

int solve(int i,int last,int done)
{
    if(i>=n)
        return 1;
    int& r = dp[i][last][done];
    if(r != -1) return r;
    r = 0;
    int st = (done ? 9 : (s[i] - '0'));
    for(int d=st; d >= last ; d--){
        r = r || solve(i+1, d, done || (d < s[i] - '0'));
    }
    return r;
}

string ans;

void trace(int i,int last,int done)
{
    if(i>=n) return;
    int st = (done ? 9 : (s[i] - '0'));
    for(int d=st; d >= last ; d--){
        if(solve(i+1, d, done || (d < s[i] - '0'))){
            ans += char(d + '0');
            trace(i+1, d, done || (d < s[i] - '0'));
            return;
        }
    }
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,tc(1);
	cin >> T;
	while(T--){
        cin >> s;
        n = (int) s.size();
        memset(dp,-1,sizeof dp);
        solve(0,0,0);
        ans = "";
        trace(0,0,0);
        while(ans.size() > 1 && ans[0] == '0') ans = ans.substr(1,s.size()-1);
        cout << "Case #" << tc++ << ": " << ans << endl;
	}
    return 0;
}
