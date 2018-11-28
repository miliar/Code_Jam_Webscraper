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

int n,q;

int main()
{	
	int t;
	cin>>t;
	ld x,mn,disthere;
	ld dist[110];
	ld d[110],s[110];
	loop(int,T,0,t-1){
		cout<<"Case #"<<T+1<<": ";
		cin>>n>>q;
		loop(int,i,0,n-1){
			cin>>d[i]>>s[i];
		}
		loop(int,i,0,n-1){
			loop(int,j,0,n-1){
				cin>>x;
				if(x!=-1)
					dist[i]=x;
			}
		}
		cin>>x;
		cin>>x;
		ld dp[110];
		dp[n-1]=0;
		rloop(int,i,n-2,0){
			mn = 1e18;
			disthere = dist[i];
			for(int j=i+1;j<n && disthere<=d[i] ;j++){
				mn=min(mn,dp[j]+(disthere/s[i]));
				disthere += dist[j]; 
			}
			dp[i] = mn;
			//cout<<dp[i]<<endl;
		}
		cout<<fixed<<setprecision(9)<<dp[0]<<endl;
	}
	return 0;	
}



// #include <bits/stdc++.h>
// using namespace std;

// #define ll long long int
// #define ld long double
// #define vi vector<int> 
// #define ii pair<int,int>
// #define vii vector<ii>
// #define loop(x,i,a,b) for(x i=a;i<=b;i++)
// #define loopi(i,a,b) for(int i=a;i<=b;i++)
// #define loop2(i,a,b) for(i=a;i<=b;i++)  
// #define rloop(x,i,a,b) for(x i=a;i>=b;i--)
// #define rloopi(i,a,b) for(int i=a;i>=b;i--)
// #define rloop2(i,a,b) for(i=a;i>=b;i--)  
// #define X first
// #define Y second 
// //#define fill(a,x) memset(a,x,sizeof(a))
// #define pb push_back
// #define mp make_pair
// #define all(v) v.begin(),v.end()
// //#define DEBUG
// const long double pi = atan(1.0)*4.0;
// const ll mod = 1e9+7;
// const ll INF = 1e18;

// #ifdef DEBUG
// #define dout(x) cout<<x;
// #define douttb(x) cout<<x<<" ";
// #define doutln(x) cout<<x<<endl;
// #else
// #define dout(x)
// #define douttb(x)
// #define doutln(x)
// #endif
// #define N 1010

// #define EPS 0.000000001


// int n,r,o,y,g,b,v;
// int r2,y2,b2;
// bool verify(vi a1){
// 	int y1=0,r1=0,b1=0;
// 	loop(int,i,0,a1.size()-1){
// 		int j= ((i+1)%(a1.size()));
// 		if(a1[i]==a1[j])
// 			return 0;
// 		if(a1[i]=='R')
// 			r1++;
// 		if(a1[i]=='Y')
// 			y1++;
// 		if(a1[i]=='B')
// 			b1++;
// 	}
// 	cout<<b1<<" "<<b2<<endl;
// 	if(r1!=r2 || b1!=b2 || y1!=y2)
// 		return 0;
// 	return 1;
// }

// int main()
// {	
// 	int t;
	
// 	cin>>t;
// 	char c[3];
// 	int ans[5000];
// 	int a[3];
// 	loop(int,T,0,t-1){
// 		cout<<"Case #"<<T+1<<": ";
// 		cin>>n>>r>>o>>y>>g>>b>>v;
// 		r2=r;
// 		y2=y;
// 		b2=b;
// 		a[0]=r;
// 		a[1]=y;
// 		a[2]=b;
// 		sort(a,a+3);
// 		loop(int,i,0,2){
// 			if(a[i]==r){
// 				c[i]='R';
// 				r=-1;
// 			}
// 			else if(a[i]==y){
// 				c[i]='Y';
// 				y=-1;
// 			}
// 			else{
// 				c[i]='B';
// 			}
// 		}
// 		if(a[2]>(a[1]+a[0]))
// 		{
// 			cout<<"IMPOSSIBLE"<<endl;
// 			continue;
// 		}
// 		fill(ans,ans+5000,-1);
// 		loop(int,i,0,a[2]-1){
// 			ans[i*3]=2;
// 		}
// 		loop(int,i,0,a[2]-1){
// 			if(a[1]!=0){
// 				a[1]--;
// 				ans[i*3+1]=1;
// 			}
// 			else{
// 				ans[i*3+1]=0;
// 				a[0]--;
// 			}
// 		}
// 		loop(int,i,0,a[0]-1){
// 			ans[i*3+2]=0;
// 		}
		
// 		vi a1;
// 		loop(int,i,0,4999){
// 			if(ans[i]!=-1)
// 				cout<<c[ans[i]];
// 		}
// 		//cout<<verify(a1);
// 		cout<<endl;
// 	}
// 	return 0;	
// }

