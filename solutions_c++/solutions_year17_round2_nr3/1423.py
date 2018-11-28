#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

#define EPS 1e-9

ld arr[105][2];
ld adjmatrix[105][105];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int T, N, Q, A, B;
    cin >> T;
    for (int i = 1; i <= T; ++i){
        cin >> N >> Q;
        for (int j = 1; j <= N; ++j){
            cin >> arr[j][0] >> arr[j][1];
        }
        for (int j = 1; j <= N; ++j){
            for (int k = 1; k <= N; ++k){
                cin >> adjmatrix[j][k];
            }
        }
        cin >> A >> B;
        ld min_taime = 0;
        deque<pair<pair<ld,ld>,ld> > V;
        //V.push_back(make_pair(make_pair(arr[1][0],arr[1][1]),0));
        for (int j = 1; j < N; ++j){
            int sz = V.size();
            for (int k = 0; k < sz; ++k){
                min_taime = min(min_taime,V[0].second);
                if (V[0].first.first - adjmatrix[j][j+1] > -EPS){
                    V.push_back(make_pair(make_pair(V[0].first.first-adjmatrix[j][j+1],V[0].first.second),V[0].second+(adjmatrix[j][j+1]/V[0].first.second)));
                }
                V.pop_front();
            }
            if (arr[j][0] - adjmatrix[j][j+1] > -EPS){
                V.push_back(make_pair(make_pair(arr[j][0]-adjmatrix[j][j+1],arr[j][1]),min_taime+(adjmatrix[j][j+1]/arr[j][1])));
            }
            min_taime = 1e17;
        }
        int sz = V.size();
        min_taime = 1e17;
        for (int k = 0; k < sz; ++k){
            min_taime = min(min_taime,V[0].second);
            V.pop_front();
        }
        cout << "Case #" << i << ": ";
        cout << fixed << setprecision(9) << min_taime << '\n';
    }
}
