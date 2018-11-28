#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long ll;

int count(int n) {
    int ans = 0;
    while (n) {
        ans += n&1;
        n >>= 1;
    }
    return ans;
}

double pi = acos(-1.0);

int main() {
    int T;  cin>>T;
    for (int t = 1; t <= T; ++t) {
        int N, K;   cin>>N>>K;
        vector<pair<int, int> > pancakes;
        for (int i = 0; i < N; ++i) {
            int R, H;    cin>>R>>H;
            pancakes.push_back({R, H});
        }
        
        sort(pancakes.rbegin(), pancakes.rend());
        
        double ans = 0;
        for (int i = 0; i < (1<<N); ++i) {
            //cout<<i<<" "<<count(i)<<endl;
            if (count(i) == K) {
                double temp = 0;
                bool first = true;
                for (int j = 0; j < N; ++j) {
                    if (i & (1 << j)) {
                        temp += 2*(pi)*pancakes[j].first*pancakes[j].second;
                        if (first) {
                            first = false;
                            temp += (pi)*pancakes[j].first*pancakes[j].first;
                        }
                    }
                }
                ans = max(ans, temp);
            }
        }
        
        printf("Case #%d: %.9lf\n", t, ans);
    }
      
    return 0;
}
