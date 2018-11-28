#include <bits/stdc++.h>
#define endl '\n';
using namespace std;
typedef long long int LL;

vector<pair<LL,LL> >v;

long double pi = M_PI;

const int N = 1005;

LL dp[N][N];

LL foo(int id,int k)
{
	if(dp[id][k]!=-1)return dp[id][k];
	LL R = v[id].first;
	LL H = v[id].second;
	if(k==0)
	{
		//cout<<R*R+2*R*H<<endl;
		return R*R+2*R*H;
	}
	vector<LL>u;
	for(int i=id+1;i<v.size();i++)
	{
	  LL r = v[i].first;
      u.push_back(R*R-r*r+foo(i,k-1));
      //cout<<u[0]+2*R*H<<endl;
	}
	sort(u.begin(),u.end());
	reverse(u.begin(),u.end());
	LL mx=0;
	if(!u.empty())
	mx =  (u[0]+2*R*H);
    mx = max(mx,R*R+2*R*H);
    dp[id][k]=mx;
    return mx;
}

bool cmp(pair<LL,LL> p1,pair<LL,LL> p2)
{
  if(p1.first>p2.first)return true;
  if(p1.first<p2.first)return false;
  return p1.second > p2.second;
}

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(0);

  freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

  int tc;cin>>tc;for(int t=1;t<=tc;t++)
  {    
     cout<<"Case #"<<t<<": ";

     v.clear();
     
     int n,k;
     cin>>n>>k;

     memset(dp,-1,sizeof(dp));

     for(int i=0;i<n;i++)
     {
     	LL r,h;
     	cin>>r>>h;
     	v.push_back(make_pair(r,h));
     }
     
     sort(v.begin(),v.end(),cmp);

     LL res = 0;
    
     for(int i=0;i<v.size();i++)
     {
     	//cout<<v[i].first<<" "<<v[i].second<<endl;
     	res=max(res,foo(i,k-1));
     	//cout<<res<<endl;
     }
    
     long double ans = pi;

     ans*=res;
 
     cout<<fixed<<setprecision(9)<<ans<<endl;
  }
          
  return 0;
}