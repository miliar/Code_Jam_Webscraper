#include <bits/stdc++.h>

using namespace std;

#define D(x) x
#define REP(i,a,b) for (int i = (a); i < (b); ++i)
#define REPR(i,a,b) for (int i = (b) - 1; i >= (a); --i)
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<vector<int> > VII;

ifstream fin ("A-small-attempt0.in");
ofstream fout ("A-small-attempt0.out");

int main() {
    ios_base::sync_with_stdio(false);
    fout << setprecision(12) << fixed;

    int T; fin >> T;
    REP(t,1,T+1) {
        int N, P; fin >> N >> P;
        vector<int> rem(P,0);
        REP(i,0,N) {
            int x; fin >> x;
            rem[x % P]++;
        }
        int result = rem[0];
        if (P == 2) {
            result += (rem[1] + 1) / 2;
        }
        if (P == 3) {
            int doubles = min(rem[1], rem[2]);
            rem[1] -= doubles;
            rem[2] -= doubles;
            result += doubles;
            result += rem[1] / 3;
            result += rem[2] / 3;
            rem[1] %= 3;
            rem[2] %= 3;
            result += rem[1] + rem[2] > 0;
        }

        if (P == 4) {
            int onethrees = min(rem[1], rem[3]);
            result += onethrees;
            rem[1] -= onethrees;
            rem[3] -= onethrees;

            rem[1] += rem[3];

            int onetwos = min(rem[1] / 2, rem[2]);

            result += onetwos;
            rem[1] -= 2 * onetwos;
            rem[2] -= onetwos;

            result += rem[1] / 4;
            rem[1] %= 4;
            result += rem[2] / 2;
            rem[2] %= 2;

            result += rem[1] + rem[2] > 0;
        }
        fout << "Case #" << t << ": " << result << endl;
    }

	return 0;
}
