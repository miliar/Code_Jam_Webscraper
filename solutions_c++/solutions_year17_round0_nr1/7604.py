#include <bits/stdc++.h>

using namespace std;

#define mi 1000000007
#define rep(i,a,b) for(i=a;i<b;i++)
#define repd(i,a,b,d) for (i=a;i<b;i+=d)
#define repv(i,a,b) for(i=b-1;i>=a;i--)
#define vi vector<int>
#define vl vector<long long int>
#define vvi vector <vector <int> >
#define vvii vector <vector <pair<int,int> > >
#define vvil vector <vector <pair<int,ll> > >
#define ll long long int
#define ld long double
#define fi first
#define se second
#define pb push_back
ll paw(ll a,ll b);


int main()
{
  int T,I;
  cin>>T;
  for (I = 1; I <= T; I++)
	{
	  string str;
	  int k, i, j, si, count = 0, fl=0;
	  cin>>str>>k;
	  si = str.size();
	  for (i = 0; i + k - 1 < si ; i++)
		{
		  if (str[i] == '-')
			{
			  for ( j = 0; j<k; j++)
				{
				  if (str[i+j] == '+') str[i+j] = '-';
				  else str[i+j] = '+';
				}
			  count ++;
			}
		}
	  for (i = 0; i<si; i++)
		if (str[i] != '+')
		  fl = 1;
	  cout<<"Case #"<<I<<": ";
	  if (fl == 1)
		cout<<"IMPOSSIBLE";
	  else
		cout<<count;
	  cout<<endl;
	}

  return 0;
}


ll paw(ll a, ll b)
{
  ll x=((a)%mi),ans=1;
  while(b>0)
    {
      if (b&1)
	ans=(ans*x)%mi;
      x=(x*x)%mi;
      b>>=1;
    }
  return ans;
}
