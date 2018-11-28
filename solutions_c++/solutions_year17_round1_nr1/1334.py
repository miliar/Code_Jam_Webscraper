#include <bits/stdc++.h>

#define FOR(i, a, n) for(int i = (int)(a); i < (int)(n); ++i)
#define REP(i, n) FOR(i, 0, n)
#define all(a) a.begin(),a.end()
#define pb push_back
#define LSOne(S) (S & (-S))
#define dbg(x) cerr << ">>>> " << x << endl;
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second
#define ii pair<int,int>
#define maxn 111111

typedef unsigned long long llu;
typedef long long int ll;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const double EPS = 1e-6;

using namespace std;

int main(){
	int t,r,c;
	scanf("%d", &t);
	for(int caso = 1; caso <= t; caso++){
		scanf("%d %d%*c", &r, &c);
		string mat[r];
		REP(i,r) getline(cin,mat[i]);
		REP(i,r){
			for(int j = 1; j < c; j++){
				if(mat[i][j] == '?' && mat[i][j-1] != '?'){
					mat[i][j] = mat[i][j-1];
				}
			}
		}
		REP(i,r){
			for(int j = c-2; j >= 0; j--){
				if(mat[i][j] == '?' && mat[i][j+1] != '?'){
					mat[i][j] = mat[i][j+1];
				}
			}
		}
		REP(j,c){
			for(int i = 1; i < r; i++){
				if(mat[i][j] == '?' && mat[i-1][j] != '?'){
					mat[i][j] = mat[i-1][j];
				}
			}
		}
		REP(j,c){
			for(int i = r-2; i >= 0; i--){
				if(mat[i][j] == '?' && mat[i+1][j] != '?'){
					mat[i][j] = mat[i+1][j];
				}
			}
		}
		printf("Case #%d:\n", caso);
		REP(i,r) cout << mat[i] << endl;
	}
	return 0;
}

































