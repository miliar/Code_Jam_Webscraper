
#include <bits/stdc++.h>
using namespace std;

#define wl(n) while(n--)
#define fr(i,a,b) for(i=a;i<b;i++)

#define bitcnt(x) __builtin_popcount(x)
#define mem(a,i) memset(a,i,sizeof(a))
typedef pair<int,int> ii;
#define mp make_pair
#define ll long long
#define MOD 1000000007
#define pb push_back
#define nl printf("\n")
#define INF (1LL<<52)

bool debug = false;
int main()
{
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);

	int t,T,i,j,x;
	ll n,m;
	cin>>T;
	fr(t,1,T+1)
	{
		vector<int>v;

		cin>>n;

	     m = n;
		while(m > 0)
		{
			x = m%10;
			v.pb(x);
			m /= 10;
		}

		reverse(v.begin(),v.end());
		if(debug)
		{
			fr(i,0,v.size())
			  cout<<v[i]<<" ";
			  nl;
		}

		int prev = 0;

		fr(i,1,v.size())
		{
			if(v[i] < v[prev])
			{
				while(prev-1 >= 0 && v[prev]-1 < v[prev-1])
				{
					prev--;
				}
			 if(debug)
			 	cout<<"idx : "<<prev<<endl;

			 v[prev]--;
			 
			 	fr(j,prev+1,v.size())
			 	{
			 		v[j] = 9;
			 	}
			}
			prev = i;
		}

		cout<<"Case #"<<t<<": ";
		//if(debug)
		{
			
			int st;
			fr(i,0,v.size())
			{
				if(v[i] != 0)
				{
					st = i;
					break;
				}
			}
			fr(i,st,v.size())
			{
				
				cout<<v[i];
			}
			nl;
		}
	}
	return 0;
}

