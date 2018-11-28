#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair< ii , int > pii;
#define endl '\n'
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ll long long
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(decltype((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define FASTIO (ios_base::sync_with_stdio(0),cout.tie(0),cin.tie(0))
#define TIME_S clock_t tStart = clock()
#define TIME_E printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC)
const int INF = 1e9;
/*codejam_2017_A_1A*/

int main() {
	FASTIO;
	int t;
	cin >> t;
	REP(c, t) {
		int r, cl;
		cin >> r >>  cl;
		vector< string > in(r);
		vector<bool > status(r);
		REP(i, r) {
			cin >> in[i];
			REP(j,  cl) {
				if (in[i][j] != '?') {
					status[i] = true;
					break;
				}
			}
		}
		vector<string> ans(r);
		int i = 0, tmp;
		while (status[i] == false)	i++;
		tmp = i;
		for (; i >= 0; i--) {
			bool x = true;
			ans[i] = in[i];
			if (status[i] == false) {
				ans[i] = ans[i + 1];
			}
			else {
				int l = 0;
				REP(j,  cl) {
					if (x and in[i][j] == '?') {
						if(j == cl-1){
							for(int k = l; k < cl; k++){
								ans[i][k] = ans[i][l-1];
							}
						}
						continue;
					}
					else {
						for (int k = j; k >= l ; k--) {
							ans[i][k] = ans[i][j];
						}
						l = j+1;
					}
				}
			}
		}
		for (i = tmp + 1; i < r; i++) {
			bool x = true;
			ans[i] = in[i];
			if (status[i] == false) {
				ans[i] = ans[i - 1];
			}
			else {
				int l = 0;
				REP(j,  cl) {
					if (x and in[i][j] == '?') {
						if(j == cl-1){
							for(int k = l; k < cl; k++){
								ans[i][k] = ans[i][l-1];
							}
						}
						continue;
					}
					else {
						for (int k = j; k >= l ; k--) {
							ans[i][k] = ans[i][j];
						}
						l = j+1;
					}
				}
			}
		}
		cout << "Case #" << c + 1 << ": " << endl;
		REP(j, r) {
			cout << ans[j] << endl;
		}
	}
}
