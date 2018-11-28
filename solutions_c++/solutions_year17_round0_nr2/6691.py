#include<bits/stdc++.h>
using namespace std;

#define ff first
#define ss second
#define m_p make_pair
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define ll long long
#define l_b lower_bound
#define u_b upper_bound
string s;
int dp[22][12][2];
int solve(int pos, int last, bool fl)
{
	if (pos == s.size()) return 1;
	if (dp[pos][last][fl] != -1) return dp[pos][last][fl];
	int lim = s[pos] - '0';
	if (fl) lim = 9;
	int ans = 0;
	for (int i = 0; i <= lim; i++)
	{
		if (i < last) continue;
		ans |= solve(pos + 1, i, fl || i != lim);
	}
	return dp[pos][last][fl] = ans;
}
string ans;
void print(int pos, int last, bool fl)
{
	if (pos == s.size()) return;
	int lim = s[pos] - '0';
	if (fl) lim = 9;
	for (int i = lim; i >= 0; i--)
	{
		if (i < last) continue;
		if ( solve(pos + 1, i, fl || i != lim) == 1)
		{
			print(pos + 1, i, fl || i != lim);
			ans += (i + '0');
			//cout<<pos<<" --> "<<i<<endl;
			break;
		}
	}

}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("secondout.out","w",stdout);
	int ks, kase;
	cin >> kase;
	for (ks = 1; ks <= kase; ks++)
	{
		cin >> s;
		memset(dp, -1, sizeof(dp));
		solve(0, 0, 0);
		ans="";
		print(0, 0, 0);
		int cnt=ans.size()-1;
		for(int i=ans.size()-1;i>=0;i--)
		{
			if(ans[i]!='0') break;
			cnt--;
		}//cout<<cnt<<endl;
		cout << "Case #" << ks << ": " ;
		for(int i=cnt;i>=0;i--) cout<<ans[i];
			cout<<endl;
	}
}