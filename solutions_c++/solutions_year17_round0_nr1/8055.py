#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	int t; cin>>t;
	for (int i = 0; i < t; i += 1)
	{
		int f[1005];
		memset(f, 0, sizeof f);
		ll sol = 0;
		string s; int k; cin>>s>>k;
		
		int n = s.length();
		for (int j = 0; j < n; j += 1)
		{
			if(s[j] == '-') f[j] = 0;
			else f[j] = 1;
		}
		bool flag = false;
		for (int j = 0; j <= n - k; j += 1)
		{
			if(f[j] != 1){
				for (int kk = 0; kk < k; kk += 1)
				{
					int c = j + kk;
					f[c] ^= 1;
				}
				++sol;
			}
		}
		for (int j = 0; j < n; j += 1)
		{
			//cout<<f[j];
			if(f[j] == 0) {flag = true; break;}
		}
		//cout<<endl;
		cout<<"Case #"<<(i+1)<<": ";
		if(flag) cout<<"IMPOSSIBLE\n";
		else cout<<sol<<"\n";
	}
	return 0;
}
