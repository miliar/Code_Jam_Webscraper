#include<bits/stdc++.h>

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define len(s) s.length()
#define forp(i,a,b) for( i=a;i<=b;i++)
#define rep(i,n)    for( i=0;i<n;i++)
#define ren(i,n)    for( i=n-1;i>=0;i--)
#define forn(i,a,b) for( i=a;i>=b;i--)
#define all(v) v.begin(),v.end()
#define b(v) v.begin()
#define e(v) v.end()
#define mem(n,m) memset(n,m,sizeof(n))
#define lb lower_bound
#define ub upper_bound
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>
#define gl(cin,s)  getline(cin,s);
#define bitc(n) __builtin_popcountll(n)
#define present(s,x) (s.find(x) != s.end()) 
#define cpresent(s,x) (find(all(s),x) != s.end()) 
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++) 

#define boost ios_base::sync_with_stdio(0)
#define MOD 1000000007
#define EPSILON 1e-9
#define PI 3.14159265358979323846
#define SIZE 51

typedef long long  ll;
typedef unsigned long long ull;
typedef long double  ldo;
typedef double  db ;
using namespace std;
char ch[SIZE][SIZE];
int main()
{  	
	/* #ifndef ONLINE_JUDGE
	freopen(fi, "r", stdin);
	#endif */
	freopen("route.in","r",stdin);
	freopen("route.out","w",stdout);
	//cin.ignore();
	//cin.clear();
	boost;
	//cin.tie(0);
	//cout<<"Case "<<tt<<": ";
	int i,j,n,m,t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		cin>>n>>m;
		forp(i,1,n){
			forp(j,1,m){
				cin>>ch[i][j];
			}
		}
		forp(i,1,n){
			int cnt=0;
			forp(j,1,m){
				if(ch[i][j]=='?'){
					cnt++;
				}
				else
				break;
			}
			if(cnt!=m){
				int idx = 1;
				char temp = ch[i][j];
				ch[i][j]='?';
				while(idx<=m){
					while(idx<=m and ch[i][idx]=='?'){
						ch[i][idx]=temp;
						idx++;
					}
					if(idx>m)
					break;
					temp = ch[i][idx];
					idx++;
				}
			}
		}
		forp(i,2,n){
			forp(j,1,m){
				if(ch[i][j]=='?' and ch[i-1][j]!='?'){
					ch[i][j]=ch[i-1][j];
				}
			}
		}
		forn(i,n-1,1){
			forp(j,1,m){
				if(ch[i][j]=='?' and ch[i+1][j]!='?'){
					ch[i][j]=ch[i+1][j];
				}
			}
		}
		cout<<"Case #"<<tt<<":"<<endl;;
		forp(i,1,n){
			forp(j,1,m){
				cout<<ch[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}
