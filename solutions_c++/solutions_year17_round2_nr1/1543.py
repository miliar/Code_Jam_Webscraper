#include <bits/stdc++.h>
using namespace std;

#define ing long long

#undef int
int main()
{
#define int long long
    int T;
    cin >> T;
    int kase = 0;
    while (T--) {
        cout << "Case #" << ++kase << ": ";
        int D, N;
        cin >> D >> N;
        pair<int, int> horse[1001];
        for (int i = 0; i < N; i++) {
            cin >> horse[i].first >> horse[i].second;
        }
        sort(horse, horse + N);
        auto FH = horse[0];
        double d = D;
        double used_time = (d - horse[N - 1].first) / horse[N - 1].second;
        double long_used = (d - horse[0].first) / horse[0].second;
        double dis = horse[0].first;
        for (int i = 1; i < N; i++) {
            double used = (d - horse[i].first) / horse[i].second;
            long_used = max(used, long_used);
        }
        printf("%.7f\n", d / long_used);
    }
    return 0;
}
