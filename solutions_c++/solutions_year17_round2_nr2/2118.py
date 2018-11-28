#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long int ll;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define present(c,e) ((c).find(e) != (c).end())
#define cpresent(c,e) (find(all(c),e) != (c).end())
#define REP(i,a,b) for(int i=int(a); i<=int(b); i++)
#define mp make_pair
#define ff first
#define ss second

int main() {
	int T;
	cin >> T;
	REP(caseno, 1, T) {
		cout << "Case #" << caseno << ": ";
		int R, Y, B, O, G, V;
		int N;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		vector<int> table(N);
		vector<pair<pair<int, int>, pair<int, int> > >colors(3);
		REP(i, 0, 2) {
			colors[i].ss.ff =  colors[i].ss.ss = i;
		}
		colors[0].ff.ff = colors[0].ff.ss = R;
		colors[1].ff.ff = colors[1].ff.ss = Y;
		colors[2].ff.ff = colors[2].ff.ss = B;

		int last_color = -1;
		REP(i, 0, N-1) {
			sort(all(colors));
			int this_color, this_index = 2;
			if (last_color == colors[this_index].ss.ss) {
				this_index = 1;
			}
			this_color = colors[this_index].ss.ss;
			// out << "i = " << i << " : " << colors[2].ss.ss << " ";
			if (colors[this_index].ff.ff <= 0) this_color = -1;
			colors[this_index].ff.ff--;
			table[i] = this_color;
			last_color = this_color;
		}

		bool flag = false;
		REP(i, 1, N-1) {
			if (table[i] == table[i-1] || table[i] == -1) {
				flag = true;
				break;
			}
		}
		if (table[0] == table[N-1] || table[0] == -1) flag = true;
		if (flag) cout << "IMPOSSIBLE\n";
		else {
			REP(i, 0, N-1) {
				switch(table[i]) {
					case 0: cout << 'R';
					break;
					case 1: cout << 'Y';
					break;
					case 2: cout << 'B';
				}
			}
			cout << '\n';
		}
	}
	return 0;
}