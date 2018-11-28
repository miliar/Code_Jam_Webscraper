#include <bits/stdc++.h>

#define dbg(x) cerr<<#x": "<<x<<"\n"
#define dbg_v(x, n) do{cerr<<#x"[]: ";for(int _=0;_<n;++_)cerr<<x[_]<<" ";cerr<<'\n';}while(0)
#define dbg_ok cerr<<"OK!\n"


using namespace std;

int n, k;


void solve(string s)
{
	int ans = 0;
	char c[300];
	c['-'] = 0;
	c['+'] = 1;
	int f[1022];

	memset(f, 0, sizeof f);
	int sum = 0;
	for(int i=0;i<s.size();i++)
	{
		sum += f[i];
		if((sum + c[s[i]])%2 == 0)
		{
			//dbg(i);
			if(i+k > s.size()) {
				cout << "IMPOSSIBLE";
				return;
			}
			ans++;
			f[k+i]--;
			sum++;
		}
	}
	cout << ans;// << '\n';

}

int main()
{
	string s;
	//ios_base::sync_with_stdio(0);
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> n;

	for(int i=1;i<=n;i++)
	{

		cout << "Case #" << i << ": ";
		cin >> s >> k;
		solve(s);
		cout << '\n';
	}



}

 