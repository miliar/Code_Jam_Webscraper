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

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		string s; cin>>s;
		int n = s.length(); int k;
		cin>>k;
		bool pos=1;
		int cnt = 0;
		for(int i = 0; i < n; i++)
		{
			if(s[i]=='-')
			{
				if(i+k-1<n)
				{
					for(int j = i; j < i + k; j++)
					{
						if(s[j]=='-') s[j]='+';
						else s[j]='-';
					}
				}
				else
				{
					pos=0;
					break;
				}
				cnt++;
			}
		}
		if(!pos) cout<<"IMPOSSIBLE\n";
		else cout<<cnt<<'\n';
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}
