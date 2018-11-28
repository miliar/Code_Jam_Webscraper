#include<bits/stdc++.h>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.txt","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
# define test(c) ini(c);while(c--)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
	rf;
	wf;
	int tt;
	cin>>tt;
	for(int ct=1;ct<=tt;ct++)
	{
		int n;
		int r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		int a[3];
		int k;
		a[0]=r;a[1]=y;a[2]=b;
		sort(a,a+3);
		if(a[2]<=(a[0]+a[1])){
			n=n;
			k=a[1]-(a[2]-a[0]);
			cout<<"Case #"<<ct<<": ";
			if(y==a[1]){
				if(r==a[2]){
				for(int i=1;i<=a[0];i++)
				{
					if(k){
						cout<<"RBY";
						k--;
					}
					else{
					cout<<"RB";
				}
				}
				for(int i=1;i<=(a[2]-a[0]);i++)
				{
					cout<<"RY";
				}
			}
			else{
				for(int i=1;i<=a[0];i++)
				{
					if(k){
						cout<<"BRY";
						k--;
					}
					else
					cout<<"BR";
				}
				for(int i=1;i<=(a[2]-a[0]);i++)
				{
					cout<<"BY";
				}

			}
			}
			else if(r==a[1]){
				if(y==a[2]){
				for(int i=1;i<=a[0];i++)
				{
					if(k){
						cout<<"YBR";
						k--;
					}
					else
					cout<<"YB";
				}
				for(int i=1;i<=(a[2]-a[0]);i++)
				{
					cout<<"YR";
				}
			}
			else{
				for(int i=1;i<=a[0];i++)
				{
					if(k){
						cout<<"BYR";
						k--;
					}
					else
					cout<<"BY";
				}
				for(int i=1;i<=(a[2]-a[0]);i++)
				{
					cout<<"BR";
				}

			}
			}
			else if(b==a[1]){
				if(r==a[2]){
				for(int i=1;i<=a[0];i++)
				{
					if(k){
						cout<<"RYB";
						k--;
					}
					else
					cout<<"RY";
				}
				for(int i=1;i<=(a[2]-a[0]);i++)
				{
					cout<<"RB";
				}
			}
			else{
				for(int i=1;i<=a[0];i++)
				{
					if(k){
						cout<<"YRB";
						k--;
					}
					else
					cout<<"YR";
				}
				for(int i=1;i<=(a[2]-a[0]);i++)
				{
					cout<<"YB";
				}

			}
			}




			cout<<endl;
		}
		else{
			cout<<"Case #"<<ct<<": IMPOSSIBLE"<<endl;
		}
	}
	
}
