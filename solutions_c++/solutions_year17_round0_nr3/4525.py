#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define fast ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define endl '\n'
#define pb push_back
#define mp make_pair
#define full(a) a.begin(),a.end()
#define mem(a,x) memset(a,x,sizeof(a))
#define test int t;cin>>t; while(t--)
#define MOD 1000000007

using namespace std;

int main()
{
	//freopen("C-small-2-attempt2.in","r",stdin);
	//freopen("output.txt","w",stdout);
	//sfast;
	int t;
	cin>>t;
	int hmm =0;
	while(t--)
	{
		ll n,k,ans1,ans2;
		cin>>n>>k;
		cout<<"Case #"<<++hmm<<": ";
		priority_queue< ll , vector<ll> , less<ll> > q;
		q.push(n);
		for(ll i=1;i<=k;i++)
		{
			ll x= q.top();
			q.pop();
			ans1 = max(x/2,x-1-x/2);
			ans2 = min(x/2,x-1-x/2);
			q.push(ans1);
			q.push(ans2);
		}	
		cout<<ans1<<" "<<ans2<<endl;
	}
	
	
}
