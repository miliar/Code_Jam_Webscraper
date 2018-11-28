
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

bool debug = true;
int main()
{
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	int t,i,j,k,T;
	string s;
	cin>>T;
	fr(t,1,T+1)
	{
		int cnt = 0 , f = 0;
		cin>>s>>k;
		fr(i,0,s.length())
		{
			if(s[i] == '-')
			{
				if(i+k-1 < s.length())
				{
				cnt++;
				fr(j,i,i+k)
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			  }
			  else
			  {	f = 1;
			  	break;}

			}
			

		}
		if(f)
			cout<<"Case #"<<t<<": IMPOSSIBLE\n";
		else
		cout<<"Case #"<<t<<": "<<cnt<<endl;
	}
	return 0;
}

