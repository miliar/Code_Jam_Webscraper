#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<ll, ll> pll;
typedef pair<int,int> pii;
typedef vector<pll> vll;
typedef vector<pii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define TRvi(c, it) for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) for (msi::iterator it = (c).begin(); it != (c).end(); it++)


#define pb push_back
#define mp make_pair
#define fab(i,a,b) for(int i=a;i<=b;i++)
#define f(i,a,b) for(int i=a;i<b;i++)

const int mod = 1e9 + 7;
const ld PI = 3.14159265358979323846;

ll mul(ll a,ll b,ll m=mod){ll x=a*1ll*b;x%=m;if(x<0)x+=m;return x;}

int main(){
	ios_base::sync_with_stdio(0);
	 freopen("A-l-practice.in", "r", stdin);
	freopen("t1l.txt", "w", stdout);
	int t;
	cin >> t;
	fab(zz,1,t){
		int r,c;
		int lr=-1;
		vi emp;
		cin>>r>>c;
		char ar[r][c],las_char;
		f(i,0,r){
			int lchar=-1;
			f(j,0,c){
				int tmp;
				cin>>ar[i][j];
				if(ar[i][j]>='A' && ar[i][j]<='Z'){
					// if(lchar!=-1){

						las_char=ar[i][j];
						lr=i;
						for(int k=j;k>lchar;k--){
							ar[i][k]=las_char;
						}
					// }
						lchar=j;
				}
				else if(j==c-1 && lchar!=-1){
					for(int k=j;k>lchar;k--){
						ar[i][k]=las_char;
					}
				}
			}
			if(lchar==-1 && lr==-1){
				emp.pb(i);
			}
			if(lchar==-1 && lr!=-1){
					int a=i;
					f(z,0,c){
						ar[a][z]=ar[lr][z];
					}
					// emp.pop_back();
			}
			if(!emp.empty() && lr!=-1){
				// cout << "hi";
								while(!emp.empty()){
					int a=emp.back();
					f(z,0,c){
						ar[a][z]=ar[lr][z];
					}
					emp.pop_back();
				}
			}
		}
		cout << "Case #"<<zz<<":"<<endl;
		f(i,0,r){
			f(j,0,c){
				cout << ar[i][j];
			}
			cout << endl;
		}
	}
return 0;
}
