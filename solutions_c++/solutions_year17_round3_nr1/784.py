#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
#include <cmath>
using namespace std;

double solve(int N, int K, vector<pair<long long, long long>> &RH){
    sort(RH.begin(), RH.end(), greater<pair<long long, long long>>());

    double ans = 0.0;
    for(int i=0; i<=N-K; i++){
        long long tmp = RH[i].first;

        vector<long long> v;
        for(int j=i+1; j<N; j++)
            v.push_back(RH[j].first * RH[j].second);
        sort(v.begin(), v.end(), greater<long long>());
        long long tmp2 = RH[i].first * RH[i].second;
        for(int j=0; j<K-1; j++)
            tmp2 += v[j];

        double area = M_PI * (tmp * tmp + tmp2 * 2.0);
        ans = max(ans, area);
    }
    return ans;
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N, K;
        cin >> N >> K;
        vector<pair<long long, long long>> RH(N);
        for(int i=0; i<N; i++) cin >> RH[i].first >> RH[i].second;

        cout << "Case #" << i+1 << ": ";
        cout << fixed << setprecision(30) << solve(N, K, RH) << endl;
    }

    return 0;
}
