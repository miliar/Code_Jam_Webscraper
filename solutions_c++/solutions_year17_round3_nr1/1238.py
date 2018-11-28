#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;
typedef unsigned long long ull;
typedef pair<ull, ull> ii;
int T, N, K;
ull sum, ans;
ii arr[1005];;
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        cin >> N >> K;
        sum = ans = 0;
        for(int i = 0; i < N; ++i) {
            cin >> arr[i].first >> arr[i].second;
        }
        sort(arr, arr + N, [](ii a, ii b){
            ull aa = a.first * 2 * a.second;
            ull bb = b.first * 2 * b.second;
            return aa > bb;
        });

        for(int i = 0; i < N; ++i) {
            ull circle = arr[i].first * arr[i].first + arr[i].first * 2 * arr[i].second;
            int cnt = 1;
            sum = 0;
            for(int j = 0; j < N && cnt < K; ++j) {
                if(i == j)
                    continue;
                if(arr[j].first <= arr[i].first) {
                    sum += arr[j].first * 2 * arr[j].second;
                    cnt++;
                }
            }

            if(cnt == K && ans < circle + sum) {
                ans = circle + sum;
            }
        }
        printf("Case #%d: %lf\n", test, ans * 3.14159265359);
    }
    return 0;
}