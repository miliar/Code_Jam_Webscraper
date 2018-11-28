#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

bool cmp(string &a, string &b) //returns true if a <= b
{
	assert(a.length()==b.length());
	for(int i = 0; i < a.length(); i++)
	{
		assert(a[i]>='0'&&a[i]<='9'&&b[i]>='0'&&b[i]<='9');
		if(a[i]<b[i]) return 1;
		else if(a[i]>b[i]) return 0;
	}
	return 1;
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		string s; cin>>s;
		string res;
		int n = s.length();
		for(int i = 0; i < n; i++)
		{
			int dig = s[i] - '0';
			string a(n-i,'0'+dig);
			string b(s,i,n-i);
			if(cmp(a,b))
			{
				res+=char('0'+dig);
			}
			else
			{
				assert(dig>0);
				res+=char('0'+dig-1);
				for(int j = i + 1; j < n; j++) res+='9';
				break;
			}
		}
		string ans;
		bool clr = 0;
		for(int i = 0; i < n; i++)
		{
			if(!clr)
			{
				if(res[i]=='0') continue;
				clr=1;
				ans+=res[i];
			}
			else
			{
				ans+=res[i];
			}
		}
		for(int i = 1; i < ans.length(); i++)
		{
			assert(ans[i]>=ans[i-1]);
		}
		cout<<ans<<'\n';
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}
