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
	freopen("B-large-practice.in", "r", stdin);
	freopen("2l.txt", "w", stdout);
	int t;
	cin >> t;
	fab(z,1,t){
		bool flag=0;
		string s;
		cin>>s;
		int n=s.size(),mini=s[0]-'0';
		f(i,0,n){
			if(s[i]-'0'<mini){
				f(k,i,n){
					s[k]='9';
				}
				// cout <<s << endl;
				for(int j=i-1;j>=0;j--){
					if(s[j]!='0'){
						s[j]--;
						s[j+1]='9';
					}
					if(s[j]>=s[j-1] && j>0){
						break;
					}
				}
				break;
			}
			else{
				mini=s[i]-'0';
			}
		}	
		cout << "Case #" << z << ": ";
		f(i,0,n){
			if(s[i]!='0'){
				flag=1;
			}
			if(flag){
				cout << s[i] ;
			}
		}
		cout << endl;
	}
return 0;
}
