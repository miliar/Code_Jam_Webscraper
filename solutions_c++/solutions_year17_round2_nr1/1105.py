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
        long long D, N;
        cin >> D >> N;
        vector<long long> K(N), S(N);
        for(int j=0; j<N; j++) cin >> K[j] >> S[j];
        double time = 0;
        for(int j=0; j<N; j++)
            time = max(time, static_cast<double>(D-K[j]) / S[j]);
        double ans = D / time;

        cout << "Case #" << i+1 << ": " << fixed << setprecision(12) << ans << endl;
    }

    return 0;
}
