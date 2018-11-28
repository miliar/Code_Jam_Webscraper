#include <bits/stdc++.h>

using namespace std;

#define D(x)
#define REP(i,a,b) for (int i = (a); i < (b); ++i)
#define REPR(i,a,b) for (int i = (b) - 1; i >= (a); --i)
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<vector<int> > VII;

ifstream fin ("Bsmall3.in");
ofstream fout ("Bsmall3.out");

int main() {
    ios_base::sync_with_stdio(false);
    fout << setprecision(12) << fixed;

    int T; fin >> T;
    REP(t,1,T+1) {
   D(     cout << "Case #" << t << ": " << endl;)
        int N;
        fin >> N;
        vector<pair<int, char> > cs(6);
        cs[0].second = 'R';
        cs[1].second = 'O';
        cs[2].second = 'Y';
        cs[3].second = 'G';
        cs[4].second = 'B';
        cs[5].second = 'C';

        REP(i,0,6)
            fin >> cs[i].first;
        sort(cs.begin(), cs.end());

  /*      if (cs[3].first + cs[4].first < cs[5].first) {
            fout << "Case #" << t << ": IMPOSSIBLE" << endl;
            continue;
        }*/

        vector<char> sol(N, cs[5].second);
        cs[5].first--;

        bool val = true;
        REP(i,1,N) {
            int m = 0;
            int ind = -1;
            REP(j,0,6) {
                if (cs[j].first >= m && cs[j].second != sol[i-1]) {
                    ind = j;
                    m = cs[j].first;
                }
             D(   cout << "cs[" << j << "].first = " << cs[j].first << ", m = " << m << ", ind = " << ind << endl;)
            }
 D(           cout << "max: " << ind << " num: " << cs[ind].first  << " col: " << cs[ind].second << endl;)
            if (ind == -1 || cs[ind].first < 1 || cs[ind].second == sol[i-1] || (i == N-1 && cs[ind].second == sol[0])) {
                fout << "Case #" << t << ": IMPOSSIBLE" << endl;
                val = false;
                break;
            } else {
                sol[i] = cs[ind].second;
                cs[ind].first--;
            }
        }
        if (val) {
                fout << "Case #" << t << ": ";
                REP(i,0,N)
                    fout << sol[i];
                fout << endl;
        }
    }

	return 0;
}
