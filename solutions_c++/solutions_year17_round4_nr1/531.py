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


int main(){
	//ios_base::sync_with_stdio(0);
	int T;

	cin >> T;
	for(int kase=1; kase <= T; kase++){
		int N, P, ans=0;
		int cnt[105]={};

		cin >> N >> P;
		rep(i, N){
			int G;
			cin >> G;
			int md = G % P;
			cnt[md]++;
		}

		ans += cnt[0];
		cnt[0] = 0;
		if( P == 2 ){
			ans += cnt[1] / 2;
			cnt[1] %= 2;
		}else{
			int tmp = min(cnt[1], cnt[P-1]);
			ans += tmp;
			cnt[1] -= tmp;
			cnt[P-1] -= tmp;
		}
		if( P == 3 ){
			int tmp = max(cnt[1], cnt[2]) / 3;
			ans += tmp;
			cnt[1] %= 3;
			cnt[2] %= 3;
		}
		if( P == 4 ){
			int tmp = cnt[2]/2;
			ans += tmp;
			cnt[2] -= tmp*2;

			ans += cnt[1] / 4;
			cnt[1] %= 4;
			ans += cnt[3] / 4;
			cnt[3] %= 4;
			if( cnt[2] ){
				if( cnt[1] >= 2 ){ ans++; cnt[1] -= 2; cnt[2]--;}
				if( cnt[3] >= 2 ){ ans++; cnt[3] -= 2; cnt[2]--;}
			}
		}
		rep(i,P) if(cnt[i] > 0){
			ans++;
			break;
		}

		cout << "Case #" << kase << ": ";
		cout << ans << endl;
	}

	return 0;
}
