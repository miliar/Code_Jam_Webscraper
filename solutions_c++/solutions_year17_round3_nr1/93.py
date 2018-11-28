#include <bits/stdc++.h>
using namespace std;
        
# define M_PI           3.14159265358979323846

struct S{
    long long r, h;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, K;
        cin >> N >> K;
        vector<S> v(N);
        for (int idx = 0; idx < N; idx++)
            cin >> v[idx].r >> v[idx].h;

        sort(v.begin(), v.end(), [](auto x, auto y){ 
                return x.h*x.r > y.h*y.r;
        });

        long long best = 0;
        for (int i = 0; i < N; i++) {
            auto ground = v[i];
            long long cur = ground.r * ground.r;
            cur += 2*ground.r*ground.h;

            int k = K - 1;
            for (int j = 0; j < N; j++) {
                if (i != j && v[j].r <= ground.r && k > 0) {
                    cur += 2*v[j].r*v[j].h;
                    k--;
                }
            }

            if (cur > best)
                best = cur;
        }

        cout.precision(10);
        cout << fixed;
        
        cout << "Case #" << t << ": " << best * M_PI;
        cout << '\n';
    }
}
