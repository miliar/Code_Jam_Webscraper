#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ld long double
#define vi vector<int> 
#define ii pair<int,int>
#define vii vector<ii>
#define loop(x,i,a,b) for(x i=a;i<=b;i++)
#define loopi(i,a,b) for(int i=a;i<=b;i++)
#define loop2(i,a,b) for(i=a;i<=b;i++)  
#define rloop(x,i,a,b) for(x i=a;i>=b;i--)
#define rloopi(i,a,b) for(int i=a;i>=b;i--)
#define rloop2(i,a,b) for(i=a;i>=b;i--)  
#define X first
#define Y second 
//#define fill(a,x) memset(a,x,sizeof(a))
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
//#define DEBUG
const long double pi = atan(1.0)*4.0;
const ll mod = 1e9+7;
const ll INF = 1e18;
#ifdef DEBUG
#define dout(x) cout<<x;
#define douttb(x) cout<<x<<" ";
#define doutln(x) cout<<x<<endl;
#else
#define dout(x)
#define douttb(x)
#define doutln(x)
#endif
#define N 100001

char flip(char ch){
	if(ch=='+') return '-';
	return '+';
}
int main()
{	
	ll n,t,x,p1,p2,y;
	cin>>t;
	vector<ll> a;
	loop(ll,T,0,t-1){
		cin>>x;
		y = x;
		a.clear();
		while(x!=0){
			a.pb(x%10);
			x/=10;
		}
		a.pb(0);
		n = a.size();
		p2 = -1;
		rloop(ll,i,n-2,0){
			if(a[i]<a[i+1]){
				p2 = i+1 ;
				break; 
			}
		}
		if(p2==-1)
		{
			cout<<"Case #"<<T+1<<": "<<y<<endl;	
			continue;
		}
		loop(ll,i,p2,n-2){
			if(a[i]>a[i+1])
			{
				p1 = i;
				break;
			}
		}
		//cout<<p1<<" "<<a[p1]<<endl;
		a[p1]--;
		loop(ll,i,0,p1-1)
			a[i]=9;
		ll ans = 0 ;
		rloop(ll,i,n-2,0)
			ans = a[i]+10*ans;
		cout<<"Case #"<<T+1<<": "<<ans<<endl;		
	}
	return 0;	
}
