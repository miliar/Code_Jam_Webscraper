#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

#define MAXV 100001
#define mod 1000000007

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair < int, int > ii;
typedef pair < int, ii > iii;

const ll LINF = 1LL<<58;

ll pd[20][12][2];
string num;

ll solve(int i, int last, int p){
	
	if(i==num.size()){
		if(p) return 0;
		return -LINF;
	}
	if(pd[i][last][p]!=-1) return pd[i][last][p];
	
	ll pot=ll(num.size()-1)-i;
	pot=pow(10LL, pot);
	ll ret=-LINF;
	
	if(p){
		rep(k, last, 10){
			ret=max(ret, pot*k+solve(i+1, k, p));
		}
	}else{
		rep(k, last, num[i]-'0'+1){
			ret=max(ret, pot*k+solve(i+1, k, k!=num[i]-'0'));
		}
	}
	
	return pd[i][last][p]=ret;
}


int main()
{
	
	freopen("B.in", "r", stdin);
	freopen("B.sol", "w", stdout);
	
	int T, z=1; cin >> T;
	ll n;
	
	while(T--){
		
		cin >> n; n++; num.clear();
		while(n){
			num.pb(n%10+'0');
			n/=10;
		}	reverse(num.begin(), num.end());
		
		memset(pd, -1, sizeof pd);
		printf("Case #%d: %lld\n", z++, solve(0, 0, 0));
		
	}
	
	return 0;
	
}
