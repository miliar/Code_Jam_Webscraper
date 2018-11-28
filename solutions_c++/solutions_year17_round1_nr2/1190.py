#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define min(x,y) ((x < y) ? (x) : (y))
#define max(x,y) ((x > y) ? (x) : (y))

bool exists(vector<vector<pair<int, int> > >& Qb, int nmin, int nmax,
            vector<int>& inds, int i, int N)
{
    if (i == N) return true;
    for (int j = inds[i]; j < Qb[i].size(); j++) {
        int tmin = Qb[i][j].first, tmax = Qb[i][j].second;
        int nnmin = max(nmin, tmin), nnmax = min(nmax, tmax);
        if (tmin > nmax) inds[i]++;
        else if (tmax < nmin) return false;
        else if (exists(Qb, nnmin, nnmax, inds, i+1, N)) return true;
    }
    return false;
}

int main()
{
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        int N, P;
        cin >> N >> P;
        vector<int> R(N);
        vector<vector<int> > Q(N, vector<int>(P));
        vector<vector<pair<int, int> > > Qb;

        for (int i = 0; i < N; i++)
            cin >> R[i];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < P; j++)
                cin >> Q[i][j];
            sort(Q[i].begin(), Q[i].end(), greater<int>());
        }
        for (int i = 0; i < N; i++) {
            Qb.push_back(vector<pair<int,int> >());
            for (int j = 0; j < P; j++) {
                double Qij = Q[i][j], Ri = R[i];
                int nmin = Qij/(1.1*Ri), nmax = Qij/(0.9*Ri);
                if (1.1*nmin*Ri < Qij) nmin++;
                if (nmax >= nmin) Qb[i].push_back(make_pair(nmin, nmax));
            }
        }

        int cnt = 0;
        for (int j = 0; j < Qb[0].size(); j++) {
            vector<int> inds(N, 0);
            if (exists(Qb, Qb[0][j].first, Qb[0][j].second, inds, 1, N)) {
                for (int i = 1; i < N; i++)
                    Qb[i].erase(Qb[i].begin() + inds[i]);
                cnt++;
            }
        }
        cout << "Case #" << c << ": " << cnt << endl;
    }
    return 0;
}
