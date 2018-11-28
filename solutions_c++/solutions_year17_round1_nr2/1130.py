#include <iostream>
#include <utility>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
using namespace std;


int R[50];

typedef pair <int, int> pii;
typedef pair <pii, int> ppii;


int main(int argc, char const* argv[])
{
    int T;
    cin >> T;
    for (int ic = 0; ic < T; ic++) {
        int N, P;
        cin >> N >> P;
        for (int i = 0; i < N; i++) {
            cin >> R[i];
        }
        vector<ppii> l;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < P; j++) {
                double q;
                cin >> q;
                int lb = ceil(q/(1.10*R[i]));
                int ub = floor(q/(0.90*R[i]));
                if (lb > ub) {
                    continue;
                }
                l.push_back(ppii(pii(lb, ub), i));
            }
        }
        sort(l.begin(), l.end());
        vector<bool> used(l.size());
        fill(used.begin(), used.end(), false);
        int n = 0;
        vector<int> choice(N);
        for (int i = 0; i < l.size(); i++) {
            if (used[i]) {
                continue;
            }
            for (int k =0;k<N;k++){
                choice[k] = -1;
            }
            int lmax = l[i].first.second;
            choice[l[i].second] = i;
            for (int j = i+1; j < l.size(); j++) {
                int mi = l[j].first.first;
                int ii = l[j].second;
                if (!used[j] && choice[ii] == -1 && mi <= lmax) {
                    choice[ii] = j;
                }
            }
            bool ok = true;
            for (int k =0;k<N;k++){
                if (choice[k] == -1){
                    ok = false;
                }
            }
            if (ok) {
                n++;
                for (int k =0;k<N;k++){
                    used[choice[k]] = true;
                }
            }
            used[i] = true;
        }


        cout << "Case #" << ic+1 << ": " << n << endl;
    }
    return 0;
}
