#include <iostream>
#define ll long long
using namespace std;





ll DIG[20];
ll MEMO[20][10];
ll N;

int dig(int k)
{
	return DIG[k];
}

ll pow10(int k)
{
	if(k==0)return 1LL;
	ll res = pow10(k/2);
	res = res*res;
	if(k%2)res*=10;
	return res; 
}

ll dp(int k, int d)
{
	int ak = dig(k);
	if(ak < d)return 0;
	if(k==0)return ak;
	if(MEMO[k][d]!=-1)return MEMO[k][d];
	if(dp(k-1, ak) > 0)return dp(k-1, ak) + pow10(k)*ak;

	if(ak==d)return 0;
	ll ans = 9;
	for(int i=1;i<=k-1;i++)
		ans*=10,ans+=9;
	ans = pow10(k)*(ak-1)+ans;
	return MEMO[k][d] = ans;
}

ll f()
{
	memset(MEMO,-1,sizeof MEMO);
	ll x=N;int k=0;
	while(x>0)DIG[k++]=x%10,x/=10;
	k-=1;

	ll ans1 = pow10(k)*(dig(k))-1;
	return max(ans1, dp(k,1));
}





int main()
{
	freopen ("B-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++)
	{
		cerr<<"Case #"<<i<<"...\n";
		cin>>N;
		cout<<"Case #"<<i<<": "<<f()<<endl;
	}
}