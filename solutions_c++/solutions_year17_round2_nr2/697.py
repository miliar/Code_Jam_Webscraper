#include "bits/stdc++.h"
using namespace std;
using ll = long long;
using P = pair<int, int>;
const ll MOD = 1000000007;

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        vector<P> nums;
        nums.emplace_back(R, 0);
        nums.emplace_back(Y, 1);
        nums.emplace_back(B, 2);
        sort(nums.begin(), nums.end());
        reverse(nums.begin(), nums.end());

        vector<int> ans(N);
        ans[0] = nums[0].second;
        nums[0].first--;
        bool ok = true;
        for(int j=1;j<N;j++){
            int max_idx = -1;
            for (int i = 0; i < 3; i++){
                if (ans[j - 1] == nums[i].second) continue;
                if (nums[i].first == 0) continue;
                if (max_idx == -1 || nums[max_idx].first < nums[i].first) {
                    max_idx = i;
                }
            }
            if(max_idx == -1)
            {
                ok = false;
                break;
            }
            ans[j] = nums[max_idx].second;
            nums[max_idx].first--;
        }

        for(int j=0;j<N-1;j++)
        {
            if(ans[j] == ans[j+1])
            {
                ok = false;
                break;
            }
        }
        if (ans[0] == ans[N - 1]) ok = false;
        printf("Case #%d: ", t);
        if(ok)
        {
            for(int i=0;i<N;i++)
            {
                cout << "RYB"[ans[i]];
            }
            cout << endl;
        }else
        {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
