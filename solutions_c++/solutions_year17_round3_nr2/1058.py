#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;
typedef unsigned long long ull;
typedef pair<ull, ull> ii;
int T, N, M;
ii nn[101], mm[101];
int main() {
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cin >> N >> M;
        for(int i = 0; i < N; ++i) {
            cin >> nn[i].first >> nn[i].second;
        }
        for(int i = 0; i < M; ++i)
            cin >> mm[i].first >> mm[i].second;

        int n = N, m = M;
        if(N > M)
            swap(N, M);
        int ans;
        if(N == 0 && M == 1) {
            ans = 2;
        }
        else if(N == 1 && M == 1) {
            ans = 2;
        }
        else {
            if(n == 2) {
                sort(nn, nn + 2);
                if(nn[1].second - nn[0].first > 720 && nn[1].first - nn[0].second < 720)
                    ans = 4;
                else
                    ans = 2;
            }
            else {

                sort(mm, mm + 2);
                if(mm[1].second - mm[0].first > 720 && mm[1].first - mm[0].second < 720)
                    ans = 4;
                else
                    ans = 2;
            }
        }


        printf("Case #%d: %d\n", test, ans);

    }
    return 0;
}