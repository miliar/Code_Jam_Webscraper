#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>

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

int N, C, M;
int check(int m, vector<int> &v){
	ll left = 0;
	int ret = 0;
	rep(i,N){
		int t = m - v[i];
		left += t;
		if( left < 0 ) return -1;
		if( t < 0 ) ret += -t;
	}
	return ret;
}

int main(){
	//ios_base::sync_with_stdio(0);
	int T;

	cin >> T;
	for(int kase=1; kase <= T; kase++){
		int cnt[1005]={}, cmax=0;
		vector<int> v(1005);

		cin >> N >> C >> M;
		rep(i,M){
			int P, B;
			cin >> P >> B;
			P--; B--;
			cnt[B]++;
			chmax(cmax, cnt[B]);
			v[P]++;
		}

		int l=cmax, r=M;
		while(r-l>1){
			int m = (r+l)/2;
			if( check(m,v) >= 0 ){
				r = m;
			}else{
				l = m;
			}
		}
		int ans_y = l;
		if( check(l,v) < 0 ) ans_y = r;
		int ans_z = check(ans_y,v);

		cout << "Case #" << kase << ": ";
		cout << ans_y << " " << ans_z << endl;
	}

	return 0;
}
