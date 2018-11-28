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
/*codejam_2017_B_Q*/

int main() {
	FASTIO;
	int t;
	cin >> t;
	REP(c, t) {
		string s;
		cin >> s;
		int i = 1;
		while (i < sz(s)) {
			if (s[i] >= s[i - 1])
				i++;
			else {
				FOR(j, i, sz(s)) {
					s[j] = '9';
				}
				int c = 1;
				i--;
				while (i > 0 and c == 1) {
					if (s[i] == '1' or s[i] == '0') {
						s[i] = '9';
						c = 1;
					}
					else {
						s[i]--;
						c = 0;
						if(s[i] < s[i-1]){
							c = 1;
							s[i] = '9';
						}
					}
					i--;
				}
				if (i == 0 and c == 1) {
					if (s[i] == '1')
						s[i] = '0';
					else
						s[i]--;
				}
				break;
			}
		}
		cout << "Case #" << c + 1 << ": ";
		i = 0;
		while (s[i] == '0')	i++;
		while (i < sz(s))
			cout << s[i++];
		cout << endl;
	}
}
