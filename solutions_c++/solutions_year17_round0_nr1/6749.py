#include <bits/stdc++.h>

using namespace std;
const double pi=acos(-1.0);
const double eps=1e-9;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define re return
#define vi vector <int> 
#define pii pair <int,int>
#define pll pair <long long , long long>
typedef long long ll;

int t,n,k,ans;
string s;

int main()
{
	ios:: sync_with_stdio(false);
	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
	cin >> t;
	int test = 1;
	while(t--) 
	{
		cin >> s >> k;
		n = s.size();
		ans = 0;
		for(int i=0;i + k - 1 < n;i++)
		{
			if(s[i] == '-')
			{
				for(int j=i;j<i+k;j++)
					if(s[j] == '-')s[j] ='+';else s[j]='-';
				ans++;
			}
			
		}
		for(int i=0;i<n;i++)
			if(s[i] == '-')ans = -1;
		cout << "Case #" << test << ": ";
		if(ans == -1)cout << "IMPOSSIBLE\n"; else cout << ans << "\n";
		test++;
	}
	return 0;
}
