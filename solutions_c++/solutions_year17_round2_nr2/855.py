
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


int n,r,o,y,g,b,v;

int main()
{	
	int t;
	
	cin>>t;
	char c[3];
	int ans[5000];
	int a[3];
	loop(int,T,0,t-1){
		cout<<"Case #"<<T+1<<": ";
		cin>>n>>r>>o>>y>>g>>b>>v;

		if(r==0 && g==0 && b==0 && o==0){
			if(y!=v)
			{
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			else{
				loop(int,i,0,y-1){
					cout<<"YV";
				}
				cout<<endl;
				continue;
			}	

		}
		if(y==0 && v==0 && b==0 && o==0){
			if(r!=g)
			{
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			else{
				loop(int,i,0,r-1){
					cout<<"RG";
				}
				cout<<endl;
				continue;
			}	

		}
		if(r==0 && g==0 && y==0 && v==0){
			if(b!=o)
			{
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			else{
				loop(int,i,0,b-1){
					cout<<"BO";
				}
				cout<<endl;
				continue;
			}	

		}

		if( (r<=g  && g!=0) || (b<=o && o!=0) || (y<=v && v!=0))
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}	
		r-=g;
		b-=o;
		y-=v;
		a[0]=r;
		a[1]=y;
		a[2]=b;
		sort(a,a+3);
		loop(int,i,0,2){
			if(a[i]==r){
				c[i]='R';
				r=-1;
			}
			else if(a[i]==y){
				c[i]='Y';
				y=-1;
			}
			else{
				c[i]='B';
			}
		}
		if(a[2]>(a[1]+a[0]))
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		fill(ans,ans+5000,-1);
		loop(int,i,0,a[2]-1){
			ans[i*3]=2;
		}
		loop(int,i,0,a[2]-1){
			if(a[1]!=0){
				a[1]--;
				ans[i*3+1]=1;
			}
			else{
				ans[i*3+1]=0;
				a[0]--;
			}
		}
		loop(int,i,0,a[0]-1){
			ans[i*3+2]=0;
		}
		
		vector<char> a1,a2;
		loop(int,i,0,4999){
			if(ans[i]!=-1)
				a1.pb(c[ans[i]]);
		}
		int f1=0,f2=0,f3=0;
		loop(int,i,0,a1.size()-1){
			a2.pb(a1[i]);
			if(a1[i]=='R' && f1==0){
				loop(int,j,0,g-1){
					a2.pb('G');
					a2.pb('R');
				}
				f1=1;
			}
			if(a1[i]=='B' && f2==0){
				loop(int,j,0,o-1){
					a2.pb('O');
					a2.pb('B');
				}
				f2=1;
			}
			if(a1[i]=='Y' && f3==0){
				loop(int,j,0,v-1){
					a2.pb('V');
					a2.pb('Y');
				}
				f3=1;
			}
		}
		for(auto xx:a2)
			cout<<xx;
		//cout<<verify(a1);
		cout<<endl;
	}
	return 0;	
}

