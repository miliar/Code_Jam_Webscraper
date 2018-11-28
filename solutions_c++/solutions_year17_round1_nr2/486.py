#include <bits/stdc++.h>
#define fin(i, n) for (int i = 0; i < n; i++)
#define fin2(i, a, b) for (int i = a; i < b; i++)
#define ll long long

using namespace std;

int main() {
    int T;
    cin >> T;
    fin(I, T) {
        cout << "Case #" << I + 1 << ": ";
        cerr << "Case #" << I + 1 << ": " << endl;
        int n, p;
        cin >> n >> p;
        vector<int> r(n);
        fin(i, n) cin >> r[i];
        vector<vector<int>> q(n, vector<int>(p));
        fin(i, n) fin(j, p) cin >> q[i][j];
        priority_queue<tuple<int, int, bool>> pq;
        fin(i, n) fin(j, p) {
            int deb = ceil(((double)(100 * q[i][j])) / ((double)(110 * r[i])));
            int fin = floor(((double)(100 * q[i][j])) / ((double)(90 * r[i])));
            pq.push(make_tuple(-deb, i, true));
            pq.push(make_tuple(-fin - 1, i, false));
        }
        int nb = 0;
        vector<int> wait(n, 0);
        vector<int> count(n, 0);
        int cur = -1;
        while (pq.size() > 0) {
            while (pq.size() > 0 && get<0>(pq.top()) == cur) {
                tuple<int, int, bool> t = pq.top();
                pq.pop();
                int time = -get<0>(t);
                int i = get<1>(t);
                bool ev = get<2>(t);
                //cerr << "# " << time << " " << i << " " << ev << endl;
                if (!ev) {
                    if (wait[i] > 0) wait[i]--;
                    else count[i]--;
                }
                else count[i]++;
            }
            int nb_poss = 1000000;
            fin(i, n) nb_poss = min(nb_poss, count[i]);
            nb += nb_poss;
            fin(i, n) count[i] -= nb_poss;
            fin(i, n) wait[i] += nb_poss;
            if (pq.size() > 0) cur = get<0>(pq.top());
        }
        cout << nb << endl;
    }
}
