// SH-RaOne //

#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ull unsigned long long int
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
const long double PI = atan(1.0)*4.0;

const ll MOD = 1e9+7;
const ll INF = 1e9;
#define N 55

ld p[N],u,nxt;
int n,k;

void solve(){
	sort(p,p+n);
	int f;
	int end=0;
	ld ans;
	while(!end){
		// loop(int,i,0,n-1)
		// 	cout<<p[i]<<" ";
		// 	cout<<endl;
		nxt=1;
		f = 0;
		loop(int,i,0,n-1){
			if(p[i]==p[0]){
				f++;
			}
			else{
				nxt = p[i];
				break;
			}
		}
		ld req = (nxt-p[0])*f;
		if(req<=u)
		{
			u-=req;
			loop(int,i,0,f-1){
				p[i]=nxt;
			}
			if(u==0)
				end=1;
		}
		else{
			ld x = u/f;
			loop(int,i,0,f-1){
				p[i]+=x;
			}
			u = 0;
			end=1;	
		}
		ans=1;
		loop(int,i,0,n-1)
			ans*=p[i];
		if(ans==1)
			end=1;
	}
	ans=1;
		loop(int,i,0,n-1)
			ans*=p[i];
	cout<<fixed<<setprecision(9)<<ans<<endl;
}

int main()
{	
	int t;
	cin>>t;
	loop(int,T,1,t){
		cout<<"Case #"<<T<<": "; 
		cin>>n>>k;
		cin>>u;
		loop(int,i,0,n-1)
			cin>>p[i];
		solve();
	}
	return 0;
}

