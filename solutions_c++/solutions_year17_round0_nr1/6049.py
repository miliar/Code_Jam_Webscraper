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
	freopen("A-large-practice.in", "r", stdin);
	freopen("tt.txt", "w", stdout);
	string s;
	int t,k;
	cin >> t;
	fab(z,1,t){
		bool flag=0;
		cin>>s>>k;
		int n=s.size(),cnt=0;
		f(i,0,n){
			if(s[i]=='-' && i+k<=n){
				cnt++;
				f(j,i,k+i){
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
				// cout << i<<" "<<s << "str" << endl;
			}
			else if(s[i]=='-' && i+k>n){
				// cout << i << " " << i+k << " " << n <<endl;
				cout <<"Case #" << z << ": IMPOSSIBLE"<<endl;
				flag=1;
				break;
			}
		}
		if(!flag){
			cout <<"Case #" << z << ": "<<cnt<<endl;
		}
		// cout <<s << endl;
	}
return 0;
}
