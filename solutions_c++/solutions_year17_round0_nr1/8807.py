#include<bits/stdc++.h>
#define maxn 2005
using namespace std;
string s;
int K;
int kase = 1;
bool dp[maxn]; 
inline void solve()
{
	memset(dp,false,sizeof(dp));
	bool state = false;
	int ans = 0;
	for(int i=0;i+K-1<s.size();i++)
	{
		if(dp[i])    state = !state;
		if( (s[i] == '+' && state) || (s[i] == '-' && !state) )
		{
			ans++;
			state = !state;
			dp[i+K] = true;
		}
	}
	bool flag = true;
	for(int i=max(0,(int)(s.size()-K+1));i<s.size();i++)
	{
		if(dp[i])    state = !state;
		if( (s[i] == '+' && state) || (s[i] == '-' && !state) ) 
		    flag = false;
	}
	cout << "Case #" << kase++ << ": ";
	if(flag)
	    cout << ans << endl;
	else  
	    cout << "IMPOSSIBLE" << endl; 
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
	cin >> t;
	while(t--)
	{
		cin >> s >> K;
		solve(); 
	} 
    return 0;
}

