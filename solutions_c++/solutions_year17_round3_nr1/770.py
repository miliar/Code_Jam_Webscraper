#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <iostream>

using namespace std;

#define NMAX 1002

int N, K;
vector< pair<int, int> > v;

void solve()
{
    cin >> N >> K;

    v.clear();
    for (int i = 0; i < N; i++) {
        int R, H;
        cin >> R >> H;
        v.push_back(make_pair(R, H));
    }

    sort(v.rbegin(), v.rend());

    float sol = 0;
    for (int i = N - K; i >= 0; i--)
    {
        int R = v[i].first, H = v[i].second;
        float val = 1.0f * R * R * M_PI + 2.0f * R * M_PI * H;
        // use i as first pancake
        vector<float> heights; 
        for (int j = i + 1; j < N; j++) {
            int h = v[j].second, r = v[j].first;
            heights.push_back(2 * r * M_PI * h);
        }

        sort(heights.rbegin(), heights.rend());

        for (int j = 1; j < K; j++)
        {
            val = val + heights[j - 1];
        }

        // cout << endl << "(" << R << ")" << " AS FIRST " << val << endl;

        sol = max(sol, val);
    }

    cout << setprecision(10) << fixed << sol << endl;
}

int main()
{
    freopen("pancake.in", "r", stdin);
    freopen("pancake.out", "w", stdout);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
