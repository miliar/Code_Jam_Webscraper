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

int main() {
    int T;
    cin>>T;
    for(int i = 0; i<T;++i){
        int K;
        string a;
        cin >> a >> K;

        for(int j=0;j<a.size();++j){
            if(a[j]=='+')a[j]=0;
            else a[j]=1;
        }

        const int N = a.size();

        vector<char> f(N, 0);

        std::fill(f.begin(), f.end(), 0);
        int sum = 0;
        int ans = 0;
        if (a[0] == 1) {
            f[0] = 1;
            ++ans;
        }

        for (int j = 1; j < N - K + 1; ++j) {
            sum += f[j - 1];
            if (j >= K)sum -= f[j - K];
            if ((a[j] + sum) % 2 != 0) {
                f[j] = 1;
                ++ans;
            }
        }
        for (int j = N - K + 1; j < N; ++j) {
            sum += f[j - 1];
            if (j >= K)sum -= f[j - K];
            if ((a[j] + sum) % 2 == 0)continue;
            else {
                ans = INT_MAX;
                break;
            }
        }

        cout<<"Case #"<<i+1<<": ";
        if(ans == INT_MAX)cout << "IMPOSSIBLE\n";
        else cout<< ans << '\n';
    }
    return 0;
}