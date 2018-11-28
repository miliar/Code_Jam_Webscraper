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
  for (I = 1; I<=T; I++)
	{
	  char str[20], ans[20];
	  cin>>str;
	  ans[0] = str[0];
	  int si = strlen(str),i,j,x;
	  for (x = 0; x<20; x++)
		for (i = 1; i<si; i++)
		  {
			if (str[i] < str[i-1] )
			  {
				str[i-1]--;
				for (j = i; j<si; j++)
				  str[j] = '9';
			  }
		  }

	  if (str[0] == '0')
		for (i = 0; i<20; i++)
		  str[i] = str[i+1];
	  
	  // for (i = si-2; i>=0; i--)
	  // 	{
	  // 	  if (str[i] ==  '0')
	  // 		break;
	  // 	  str[i] = min(str[i], str[i+1]);
	  // 	}
	  //cout<<str<<endl;
	  
	  cout<<"Case #"<<I<<": ";
	  cout<<str;
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
