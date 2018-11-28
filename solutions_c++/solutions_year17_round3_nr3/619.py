#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;


int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N, K;
        cin >> N >> K;
        double U;
        cin >> U;
        vector<double> P(N);
        for(int i=0; i<N; i++) cin >> P[i];

        sort(P.begin(), P.end());
        for(int i=0; i<N-1; i++){
            double diff = P[i+1] - P[i];
            int num = i + 1;
            double div = U / num;
            div = min(div, diff);
            U -= div * num;
            for(int j=0; j<=i; j++)
                P[j] += div;
        }


        double div = U / N;
        for(int i=0; i<N; i++)
            P[i] = min(1.0, P[i] + div);

        double ans = 1.0;
        for(int i=0; i<N; i++) ans *= P[i];

        cout << "Case #" << i+1 << ": " << fixed << setprecision(16) << ans << endl;
    }

    return 0;
}
