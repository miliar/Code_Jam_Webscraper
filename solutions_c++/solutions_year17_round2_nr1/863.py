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
#define N 1010

#define EPS 0.000000001

ld p[N],s[N];
int n;
ld d;

bool verify(ld speed){
	loop(int,i,0,n-1){
		ld dist = p[i]*speed/(speed-s[i]);
		if(dist<d && speed>s[i])
			return 1;
	}
	return 0;
}

int main()
{	
	int t;
	cin>>t;
	loop(int,T,0,t-1){
		cin>>d>>n;
		cout<<"Case #"<<T+1<<": ";
		loop(int,i,0,n-1){
			cin>>p[i]>>s[i];
		}
		// ld l=0;
		// ld h=1e9;
		// //cout<<verify(1)<<endl;
		// while((h-l)>=EPS){
		// 	ld m = (l+h)/2;
		// 	//cout<<m<<" "<<verify(m)<<endl;
		// 	if(verify(m)){
		// 		h=m;
		// 	}
		// 	else{
		// 		l=m;
		// 	}
		// }
		ld ans = 1e18;
		loop(int,i,0,n-1){
			ld x = (d*s[i])/((d-p[i]));
			ans = min(ans,x);
		}
		cout<<fixed<<setprecision(9)<<ans<<endl;
	}
	return 0;	
}

