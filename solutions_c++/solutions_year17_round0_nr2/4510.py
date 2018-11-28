using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef long long ll;
#define mx 0

void go(int MAX, int MIN, vi &digits){
	for (int i = MAX; i >= MIN;--i){
		if(digits[i]>digits[i-1]){
			
			for (int j = i-1; j >=0 ; --j){
				digits[j] = 9;
			}
			digits[i]--; 
			if(digits[i] == 0 || digits[i]<digits[i+1]){
				go(MAX, i, digits);
			}
		}
	}
}

ll calc(int MAX, vi &digits){
	ll res = 0;
	for (ll i = 0; i < MAX; ++i){
		res += (ll)pow(10, i)*digits[i];
		// printf("%d ", digits[i]);
	}
	// printf("\n");
	return res;
}
int main() {
   	ios_base::sync_with_stdio(0);cin.tie(NULL);
   	//Solution
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		
		ll N;
		scanf("%lld", &N);
		ll N10 = (ll)floor(log10(N));
		//printf("%lld\n", N10);
		ll ans = 0;
		ll i = 0;
		ll prev; 
		vi digits;
		while(N>0){
			prev = N%10;
			digits.push_back(prev);
			N/=10;
		}
		if(digits.size()==1){
			printf("Case #%lld: %lld\n", t, digits[0]);
			continue;
		}
		go(digits.size()-1, 1, digits);
		// printf("%d\n",(int)digits.size() );
		printf("Case #%d: %lld\n", t, calc(digits.size(),digits));

	}
   	
   	
   	return 0;
}


//g++-4.9 tidy.cpp -o tidy && ./tidy < tidy.in > tidy.out