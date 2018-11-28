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

long long dp[1010];
double arr[1100][2];

int main()
{
  int t;
  cin>>t;
  for (int I = 1; I<=t; I++)
	{
	  int n,k,i,j,r,h;
	  cin>>n>>k;

	  multimap <int, int> dat;
	  
	  rep(i,0,n)
		{
		  arr[i][0] = arr[i][1] = 0;
		  cin>>r>>h;
		  dat.insert(make_pair(-1*r,-1*h));
		}
	  //cout<<"input completed"<<endl;
	  multimap <int, int> :: iterator itr = dat.begin();
	  i = 0;
	  while(itr != dat.end())
		{
		  arr[i][0] = -1*(*itr).fi;
		  arr[i][1] = -1*(*itr).se;
		  //cout<<"r = "<<arr[i][0]<<" h = "<<arr[i][1]<<endl;
		  itr++;
		  i++;
		}
	  
	  for (i = 0; i<n+10; i++)
		dp[(int)i] = -1;
	  
	  rep(i,0,n)
		{
		  multiset<long long> s;
		  
		  rep(j,i+1,n)
			s.insert(-1*(2*arr[j][0]*arr[j][1]));
		  
		  multiset <ll> :: iterator itr1 = s.begin();

		  dp[i] = arr[i][0]*(arr[i][0] + 2*arr[i][1]);
		  
		  int cou = 0;
		  while(itr1 != s.end())
			{
			  cou++;
			  //cout<<"cou "<<cou<<" k "<<k<<endl;
			  if (cou >= k)
				break;
			  dp[i] += -1*(*itr1);
			  //			  cout<<"i "<<i<<" dp "<<dp[i]<<endl;
			  itr1++;
			}
		}
	  double ans = -100000;
	  rep(i,0,n-k+1)
		ans = max(ans, (double)dp[i]);
	  cout<<"Case #"<<I<<": ";
	  cout<<setprecision(50)<<((double)M_PI)*ans<<endl;
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
