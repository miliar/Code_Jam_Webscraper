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
	int T, ans=0;

	cin >> T;
	for(int kase=1; kase <= T; kase++){
		int N, R, O, Y, G, B, V;
		string ans;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		vector< pair<int,string> > v;
		v.emplace_back( R, "R" );
		v.emplace_back( Y, "Y" );
		v.emplace_back( B, "B" );
		sort( all(v) );
		//rep(i,3) cout << v[i].X << " "; cout << endl;
		//cout << v.back().X << endl;

		int mx = v.back().X;
		int sum = R + Y + B;
		if( sum >= mx * 2 ){
			auto mxC = v.back().Y;
			int sel = 0;
			while( v[0].X + v[1].X > v[2].X ){
				v[sel].X--;
				ans += v[sel].Y;
				sel ^= 1;
			}
			while( v[0].X + v[1].X + v[2].X > 0 ){
				if( v[sel].X == 0 ) sel ^= 1;
				v[sel].X--;
				ans += v[sel].Y;
				v[2].X--;
				ans += v[2].Y;
			}
		}else{
			ans = "IMPOSSIBLE";
		}

		cout << "Case #" << kase << ": ";
		cout << ans << endl;
	}

	return 0;
}
