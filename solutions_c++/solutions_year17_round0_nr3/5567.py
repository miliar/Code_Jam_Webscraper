//Author:- IITian_Sujal
//let's keep it simple and easy....
#include<bits/stdc++.h>
#define ll          long long int
#define mp          make_pair
#define pii         pair<int,int>
#define pb          push_back
#define vi          vector<int>
#define Max(a,b)    ((a)>(b)?(a):(b))
#define Min(a,b)    ((a)<(b)?(a):(b))
#define rep(i,a,b)  for (__typeof((b)) i=(a);i<(b);i+=1)
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define mod	        1000000007
#define endl        '\n'
using namespace std;
class comp
{
	public:
		bool operator()(const ll & l,const ll & h)
		{
			return l<h;
		}
};
int main()
{
	int t;
	freopen("1.txt","r",stdin);
	freopen("a.out","w",stdout);
	cin >>t;
	rep(y,1,t+1)
	{
		ll n,k;
		cin >>n>>k;
		priority_queue<ll,vector<ll>,comp> q;
		//cout<<n<<" "<<k<<" ";
		while(!q.empty())
		{
			q.pop();
		}
		q.push(n);
		k-=1;
		while(k--)
		{
			if(q.size()>0)
			{
				n=q.top();
				q.pop();	
			}
			else
			{
				break;
			}
			if(n%2==0)
			{
				if((n/2)>2)
				q.push(n/2-1);
				if((n/2)>1)
				q.push(n/2);
			}
			else
			{
				if((n/2)>1)
				q.push(n/2);
				if((n/2)>1)
				q.push(n/2);
			}
		}
		if(q.size()==0)
		{
			q.push(1);
		}
		ll ans=q.top();
		cout<<"Case #"<<y<<": ";
		if(ans%2==0)
		{
			cout<<ans/2<<" "<<ans/2-(ll)1<<endl;
		}
		else
		{
			cout<<ans/2<<" "<<ans/2<<endl;
		}
	}
}
