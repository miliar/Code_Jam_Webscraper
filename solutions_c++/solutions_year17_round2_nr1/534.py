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

ifstream fin ("Alarge.in");
ofstream fout ("Alarge.out");

int main() {
    ios_base::sync_with_stdio(false);
    fout << setprecision(12) << fixed;

    int T; fin >> T;
    REP(t,1,T+1) {
        int D, N;
        fin >> D >> N;

        double latest = 0;

        REP(i,0,N) {
            int pos, speed;
            fin >> pos >> speed;
            double arrival = 1.0d * (D - pos) / speed;
            latest = max(latest, arrival);
        }

        fout << "Case #" << t << ": " << D / latest << endl;

/*        vector<PII> ks(N+1);
        REP(i,0,N) {
            fin >> ks[i].first >> ks[i].second;


        }
        ks[N].first = D;
        sort(ks.begin(), ks.end());

        vector<double> ts(N+1);
        int pos = ks[1].first;
        double speed = ks[0].second;
        double time = (pos - ks[0].first) / speed;
        double maxspeed = pos / time;

        REP(i,1,N) {
            int dist = ks[i + 1].first - ks[i].first;
            double timea = time + dist / speed;
            double timeb = dist / ks[i].second;
            if (timeb <= timea)
            time = max(timea, timeb);
            maxspeed = min(maxspeed, ks[i + 1].first/time);
        }*/

//        fout << "Case #" << t << ": " << maxspeed << endl;
    }

	return 0;
}
