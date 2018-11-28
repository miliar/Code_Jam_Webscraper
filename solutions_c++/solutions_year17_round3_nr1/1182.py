#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <unordered_map>

using namespace std;

typedef pair<int, int> P;

const double pi = acos(-1.0);
int N, K;
ofstream fout;

void solve(int tc){
    fout << "Case #" << tc << ": ";
    printf("Case #%d: ", tc);    
    cin >> N >> K;
    vector<P> pans(N);
    for(int i = 0; i < N; i++){
        int R, H;
        cin >> R >> H;
        pans[i] = P(R, H);
    }
    sort(pans.rbegin(), pans.rend());
    
    vector<double> dp(N + 5, 0.);
    for(int i = 0; i < N; i++){
        double area = pi * pans[i].first * (pans[i].first + 2 * pans[i].second);
        double surface = pi * pans[i].first * pans[i].first;
        for(int j = i + 1; j > 1; j--){
            dp[j] = max(dp[j], dp[j - 1] + area - surface);
        }
        dp[1] = max(dp[1], area);
    }
    fout << fixed << dp[K] << endl;
    printf("%.8f\n", dp[K]);
}

int main(){
    int T;
    cin >> T;
    fout.open("A.out");
    for(int tc = 1; tc <= T; tc++){
        solve(tc);
    }
    fout.close();
    return 0;
}

