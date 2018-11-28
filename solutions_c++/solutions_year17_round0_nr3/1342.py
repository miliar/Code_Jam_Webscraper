#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define reps(i,x,n) for(int i=x; i<(n); i++)
#define rrep(i,n) for(int i=(n)-1; i>=0; i--)
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second
#define pb push_back
#define eb emplace_back

using namespace std;
typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }

template<class A, size_t N, class T> void Fill(A (&a)[N], const T &v){ fill( (T*)a, (T*)(a+N), v ); }

const ll INF = 0x3fffffff;


int main(){
	//ios_base::sync_with_stdio(0);
	int T;

	cin >> T;
	for(int kase=1; kase<=T; kase++){
		ll N, K, ans = 0;
		map<ll,ll> mp;

		cin >> N >> K;

		mp[N] = 1;
		ll l, r;
		while( K > 0 && mp.size() ){
			auto it = mp.end();
			it--;
			ll n = it->X;
			ll k = it->Y;
			mp.erase( it );
			l = max<ll>(0, n/2 - ((n+1)%2));
			r = n/2;
			mp[ l ] += k;
			mp[ r ] += k;
			K -= k;
		}

		cout << "Case #" << kase << ": ";
		cout << max(l,r) << " " << min(l,r) << endl;
	}

	return 0;
}
