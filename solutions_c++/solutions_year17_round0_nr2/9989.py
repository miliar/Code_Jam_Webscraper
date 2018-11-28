/* abhra73 */
#include <iostream>
#define sp(z) 				setprecision(z)
#define sv(z) 				sort(z.begin(),z.end())
#define F 					first
#define S 					second
#define pb 					push_back
#define mp 					make_pair
#define ll 					long long
#define ld 					long double
#define fre(y,q,s) 			for(int y=q;y>=s;y--)
#define fr(y,q,s) 			for(int y=q;y<s;y++)
#define f(y,z) 				for(int y=0;y<z;y++)
#define fe(y,z) 			for(int y=1;y<=z;y++)
#define matrix(arr,n,m)		vector<vector<ll> > arr(n,vector<ll>(m,0))
using namespace std;
ll lmin(ll a,ll b){ return (a<b)?a:b; } ll lmax(ll a,ll b){ return (a>b)?a:b; }
ld dmin(ld a,ld b){ return (a<b)?a:b; } ld dmax(ld a,ld b){ return (a>b)?a:b; }
ll gcd(ll a,ll b){ return (b==0)?a:gcd(b,a%b); } ll lcm(ll a, ll b) { return (a*b)/gcd(a,b); }
ll modpow(ll a, ll n, ll mod){ ll res=1; while(n){ if(n&1)res=(res*a)%mod; a=(a*a)%mod; n>>=1; } return res; }
ll lpow(ll a, ll n){ ll res=1; while(n){ if(n&1)res*=a; a*=a; n>>=1; } return res; }
ld dpow(ld a, ll n){ ld res=1; while(n){ if(n&1)res*=a; a*=a; n>>=1; } return res; }

/* ********************** Main Code starts from here ********************** */

bool isValid(int n) {
	string s = "";
	while(n) {
		int x = n % 10;
		s = char(x + '0') + s;
		n /= 10;
	}
	int l = s.length();
	bool res = true;
	fre(i, l - 1, 1) {
		if(s[i] < s[i - 1]) {
			res = false;
			break;
		}
	}
	return res;
}

int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	int n;
	cin >> t ;
	fe(i, t) {
		cout << "Case #" << i << ": ";
		cin >> n;
		int ans = 0;
		fe(j, n) {
			if(isValid(j)) ans = j;
		}
		cout << ans << endl;
	}

	return 0;
}