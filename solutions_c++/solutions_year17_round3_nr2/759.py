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
		int C, J;
		int sum[2] = {};
		vector<pair<int, pii> > v;

		cin >> C >> J;
		int N = C + J;
		rep(i,N){
			int a, b;
			cin >> a >> b;
			sum[i<C] += b - a;
			v.emplace_back( a, pii(b, i<C) );
		}
		sort( all(v) );
		int sc = v[0].Y.Y;
		if( C == 0 || J == 0 ){
			int b = 0;
			vector<pii> vs;
			rep(i,v.size()){
				vs.emplace_back(v[i].X - b, i);
				b = v[i].Y.X;
			}
			vs.emplace_back( 1440 - b, -1 );
			sort( all(vs) );
			if( vs[ vs.size()-1 ].Y == -1 ){
				sc = -1;
			}else{
				int x = v[ vs[ vs.size()-1 ].Y ].X;
				rep( i, vs[ vs.size()-1 ].Y ){
					v[i].X   += 1440;
					v[i].Y.X += 1440;
				}
				sc = -1;
			}
		}
		sort( all(v) );
		rep(i,v.size()){
			if( sc == v[i].Y.Y ){
				v[i].X   += 1440;
				v[i].Y.X += 1440;
			}else{
				int x = v[i].X;
				v.emplace_back( x, pii(x,-1) );
				v.emplace_back( x+1440, pii(x+1440, 99) );
				break;
			}
		}
		sort( all(v) );

		vector<int> diff[2];
		vector<int> lest;
		int diff_sum[2] = {}, lest_sum = 0;
		rep(i,v.size()) if( i > 0 ){
			if( v[i].Y.Y == v[i-1].Y.Y ){
				int c = v[i].Y.Y;
				diff[c].emplace_back( v[i].X - v[i-1].Y.X );
				diff_sum[c] += v[i].X - v[i-1].Y.X;
			}else{
				lest.push_back( v[i].X - v[i-1].Y.X );
				lest_sum += v[i].X - v[i-1].Y.X;
			}
		}
		sort( all(diff[0]) );
		sort( all(diff[1]) );

		int _ans[2], s[2];
		_ans[0] = J*2;
		_ans[1] = C*2;
		s[0] = sum[0];
		s[1] = sum[1];
		rep(k,2) rep(i,diff[k].size()){
			if( s[k] + diff[k][i] <= 720 ){
				_ans[k] -= 2;
			}
			s[k] += diff[k][i];
		}
		//cout << _ans[0] << " " << _ans[1] << endl;
		//cout << "s:  " << s[0] << " " << s[1] << endl;
		rep(k,2){
			s[k] += lest_sum;
			rrep(i,diff[k^1].size()){
				if( s[k] + diff[k^1][i] <= 720 ){
					_ans[k] += 2;
				}
				s[k] += diff[k^1][i];
			}
		}
		//cout << _ans[0] << " " << _ans[1] << endl;
		//cout << "s:  " << s[0] << " " << s[1] << endl;
		//if( v[1].Y.Y == v[v.size()-2].Y.Y ) _ans[ v[1].Y.Y ] -= 2;
		int ans = max( _ans[0], _ans[1] );

		cout << "Case #" << kase << ": ";
		cout << ans << endl;
	}

	return 0;
}
