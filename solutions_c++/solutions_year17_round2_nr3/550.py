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

ifstream fin ("C-large.in");
ofstream fout ("C-large.out");

int main() {
    ios_base::sync_with_stdio(false);
    fout.setf(ios::fixed);
    fout << setprecision(12) << fixed;

    int T; fin >> T;
    REP(t,1,T+1) {
        int N, Q;
        fin >> N >> Q;
        vector<ll> Es(N), Ss(N);
        REP(i,0,N)
            fin >> Es[i] >> Ss[i];

        vector<vector<ll> > dists(N, vector<ll>(N));
        REP(i,0,N)
            REP(j,0,N) {
                fin >> dists[i][j];
                if (dists[i][j] == -1)
                    dists[i][j] = 1ll << 40;
            }

        REP(i,0,N)
            REP(j,0,N)
                REP(k,0,N)
                    dists[j][k]= min(dists[j][k], dists[j][i] + dists[i][k]);

        vector<vector<double> > tdists(N, vector<double>(N));

        REP(i,0,N)
            REP(j,0,N) {
//                cout << "dist[" << i << "][" << j << "]: " << dists[i][j] << endl;
                if (dists[i][j] <= Es[i])
                    tdists[i][j] = 1.0 * dists[i][j] / Ss[i];
                else
                    tdists[i][j] = std::numeric_limits<double>::infinity();
//                cout << "tdist[" << i << "][" << j << "]: " << dists[i][j] << endl;
            }


        REP(i,0,N)
            REP(j,0,N)
                REP(k,0,N)
                    tdists[j][k]= min(tdists[j][k], tdists[j][i] + tdists[i][k]);


        fout << "Case #" << t << ":";
        REP(i,0,Q) {
            int u, v;
            fin >> u >> v;
            u--;v--;
            fout << " " << tdists[u][v];
        }
        fout << endl;
    }

	return 0;
}
