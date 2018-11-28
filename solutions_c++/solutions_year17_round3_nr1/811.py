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
#define N 1010

long double ans,ans2,mx,x,y;
int n,k;
vector<pair< ld,ld> > rh;

void solve(){
	sort(rh.begin(),rh.end());
	mx = 0;
	loop(int,i,k-1,n-1){
		
		ans = rh[i].X*rh[i].X;
		ans += 2*rh[i].X*rh[i].Y;
		//cout<<ans<<endl;
		vector<ld> temp;
		loop(int,j,0,i-1){
			temp.pb(rh[j].X*rh[j].Y);
		}
		ans2=0;
		int size = temp.size();
		//cout<<size<<" "<<k<<endl;
		if(size!=0){
			sort(all(temp));
			loop(int,j,size-k+1,size-1){
				ans2 += temp[j];
			}
			ans2*=2;
		}
		ans+= ans2;
		mx = max(mx,ans);	
	}
	cout<<fixed<<setprecision(9)<<mx*PI<<endl;
}

int main()
{	
	int t;
	cin>>t;
	loop(int,T,1,t){
		cout<<"Case #"<<T<<": "; 
		cin>>n>>k;
		//n=1000;
		//k=10;
		rh.clear();
		loop(int,i,0,n-1){
			cin>>x>>y;
			//x=100; y=100;
			rh.pb({x,y});
		}
		solve();
	}
	//cout<<xx<<endl;
	return 0;
}

