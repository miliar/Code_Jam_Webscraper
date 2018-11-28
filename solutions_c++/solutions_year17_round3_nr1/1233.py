#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <unordered_map>

using namespace std;

struct Pan{
    long long R;
    long long H;
};

constexpr double pi = 3.141592653589793;

int main() {
    int T;
    cin >> T;

    cout << fixed << setprecision(10);
    for (int I = 0; I < T; ++I) {
        int N,K;
        cin>>N>>K;

        vector<Pan> Pans(N);
        for(auto& val: Pans){
            cin>>val.R>>val.H;
        }

        sort(begin(Pans), end(Pans), [](auto x, auto y)->bool{return x.R>y.R;});

        vector<vector<long long>> dp(N, vector<long long>(K,0));

        for(int i=0;i<N;++i) {
            dp[i][0]=Pans[i].R*Pans[i].R+2*Pans[i].R*Pans[i].H;
        }

        for(int j=1;j<K;++j){
            long long cache = dp[j-1][j-1];
            for(int i=j;i<N;++i){
                dp[i][j]+=2*Pans[i].R*Pans[i].H+cache;
                cache = max(cache, dp[i][j-1]);
            }
        }

        long long ans=0;
        for(int i=K-1;i<N;++i){
            ans=max(ans,dp[i][K-1]);
        }


        cout << "Case #" << I + 1 << ": "<<(double)(ans)*pi<<'\n';
    }
    return 0;
}