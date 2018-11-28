#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <istream>
#include <ostream>

#include <cstdlib>
#include <cmath>
#include <cstdio>

using namespace std;

#define fi first
#define se second
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define rep(i,n) for(ll i=0; i < (n); ++i)
#define rrep(i,n) for(ll i=((n)-1); i >= 0; --i)

#define OPLT(T) bool operator<(const T & lop_, const T & rop_)
#define OPEQ(T) bool operator==(const T & lop_, const T & rop_)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

istream& operator>>(istream& istr, __float128& obj) { double d; istr >> d; obj = d; return istr; };
ostream& operator<<(ostream& ostr, __float128& obj) { ostr << static_cast<double>(obj); return ostr; };

int main() {
	int T;
	cin >> T;
	rep(t,T) {
		int N, M;
		cin >> N >> M;
		vector<string> A(N,string(N,'.')), B(N,string(N,'.'));
		vector<string> ini(N,string(N,'.'));
		rep(i,M) {
			char type;
			int R, C;
			cin >> type >> R >> C;
			R--; C--;
			ini[R][C] = type;
			if(type == 'o') {
				A[R][C] = '+';
				B[R][C] = 'x';
			}
			else if(type == '+') {
				A[R][C] = '+';
			}
			else {
				B[R][C] = 'x';
			}
		}
		rep(i,N) {
			rep(j,N) {
				bool f = true;
				rep(k,N) if(B[i][k] == 'x') f = false;
				rep(k,N) if(B[k][j] == 'x') f = false;
				if(f)
					B[i][j] = 'x';
			}
		}

		vector<string> Asub = A;
		vector<pair<int,vector<string> > > diag;
		rep(i,2) {
			int cnt = 0;
			A = Asub;
			rep(j,N) {
				if(i) {
					bool f = true;
					rep(k,N) {
						if(j-k >= 0 && A[k][j-k] == '+') f = false;
						if(j+k < N && A[k][j+k] == '+') f = false;
					}
					if(f) {
						cnt++;
						A[0][j] = '+';
					}
					f = true;
					rep(k,N) {
						if(j-k >= 0 && A[N-1-k][j-k] == '+') f = false;
						if(j+k < N && A[N-1-k][j+k] == '+') f = false;
					}
					if(f) {
						cnt++;
						A[N-1][j] = '+';
					}
				}
				else {
					bool f = true;
					rep(k,N) {
						if(j-k >= 0 && A[j-k][k] == '+') f = false;
						if(j+k < N && A[j+k][k] == '+') f = false;
					}
					if(f) {
						cnt++;
						A[j][0] = '+';
					}
					f = true;
					rep(k,N) {
						if(j-k >= 0 && A[j-k][N-1-k] == '+') f = false;
						if(j+k < N && A[j+k][N-1-k] == '+') f = false;
					}
					if(f) {
						cnt++;
						A[j][N-1] = '+';
					}
				}
			}
			diag.push_back(pair<int,vector<string> >(cnt,A));
		}
		if(diag[0].fi < diag[1].fi) {
			A = diag[1].se;
		}
		else {
			A = diag[0].se;
		}

		int score = 0;
		vector<pair<char,pii> > op;
		rep(i,N) {
			rep(j,N) {
				char c = '.';
				if(A[i][j] == '+' && B[i][j] == 'x') c = 'o';
				else if(A[i][j] == '+') c = '+';
				else if(B[i][j] == 'x') c = 'x';

				if(c == 'o') score += 2;
				else if(c == '.');
				else score += 1;

				if(ini[i][j] != c) {
					op.push_back(pair<char,pii>(c,pii(i+1,j+1)));
				}
			}
		}
		cout << "Case #" << t+1 << ": ";
		cout << score << " " << op.size() << endl;
		rep(i,op.size()) {
			cout << op[i].fi << " " << op[i].se.fi << " " << op[i].se.se << endl;
		}
	}
	return 0;
}
