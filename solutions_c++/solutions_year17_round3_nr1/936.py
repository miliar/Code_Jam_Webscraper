#include <bits/stdc++.h>
using namespace std;
#define int long long
#undef int
int main()
{
#define int long long
    int T;
    cin >> T;
    for (int I = 1; I <= T; I++) {
        cout << "Case #" << I << ": ";
        int N, K;
        cin >> N >> K;
        vector<pair<int, int> > v;
        for (int i = 0; i < N; i++) {
            int r, h;
            cin >> r >> h;
            v.push_back({ r, h });
        }
        double PI = acos(-1.0);
        sort(v.rbegin(), v.rend());
        double Ans = 0;
        for (int i = 0; i < N; i++) {
            if (i + K > N)
                break;
            double ans = PI * v[i].first * v[i].first;
            ans += 2 * PI * v[i].first * v[i].second;
            vector<double> vv;
            for (int j = i + 1; j < N; j++) {
                vv.push_back((double)v[j].first * (double)v[j].second);
            }
            sort(vv.rbegin(), vv.rend());
            for (int j = 1; j < K; j++) {
                ans += 2 * PI * vv[j - 1];
            }
            Ans = max(Ans, ans);
        }
        printf("%.10f\n", Ans);
    }
    return 0;
}
