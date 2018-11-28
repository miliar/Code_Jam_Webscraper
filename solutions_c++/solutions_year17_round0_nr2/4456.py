#include<bits/stdc++.h>
using namespace std;
typedef  long long ll;
vector<ll> ans;
ll a[30];
map<ll,ll> maa;
void solve(ll index,ll limit)
{
	if(index>limit)
	return ;
	ll i=0;
	ll cnt=0;
	string s;
	for(i=1;i<index;i++)
	{
		cnt=cnt*10+a[i];
		char p=a[i]+48;
		s=s+p;
	}
	if(cnt!=0)
	{
		bool f=true;
		for(ll j=0;j<s.size()-1;j++)
		{
			if(s[j]>s[j+1])
			{
				f=false;
				break;
			}
		}
		if(f)
		{
			if(maa.find(cnt)==maa.end())
			{
			ans.push_back(cnt);
			maa[cnt]=1;
			}
		}
	}
	s.clear();
	for(i=0;i<=9;i++){
		if(i>=a[index-1])
		{
			a[index]=i;
		solve(index+1,limit);
		}
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("ans2.txt","w",stdout);
	memset(a,0,sizeof(a));
	a[0]=-1;
	solve(1,19);
	ll t;
	cin>>t;
	ll kase=1;
	sort(ans.begin(),ans.end());
	while(t--)
	{
		ll n;
		cin>>n;
		ll m=n;
		string s;
		while(m)
		{
			char p=(m%10)+48;
			s=s+p;
			m=m/10;
		}
		reverse(s.begin(),s.end());
		bool f=true;
		for(ll j=0;j<s.size()-1;j++)
		{
			if(s[j]>s[j+1])
			{
				f=false;
				break;
			}
		}
		cout<<"Case #"<<kase<<": ";
		if(f)
		{
			cout<<n<<endl;
		//	continue;
		}
		else
		{
			ll ele=lower_bound(ans.begin(),ans.end(),n)-ans.begin();
		cout<<ans[ele-1]<<endl;
		
		}
		kase++;
	}
}
