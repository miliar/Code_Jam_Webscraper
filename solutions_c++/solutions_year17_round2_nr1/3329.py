#include <bits/stdc++.h>
using namespace std;
pair<int, int> arr [10001];
int D;
int cmp(pair<int, int> a, pair<int, int> b){
    return (double)a.second < (double)b.second;
}
int main(void)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);


    int tc;
    cin >> tc;
    for(int cs = 0;cs < tc;cs++){
        int n;
        cin >> D >> n;
        for(int i = 0;i < n;i++){
            cin >> arr[i].first >> arr[i].second;
        }
        sort(arr, arr + n, cmp);

        double min_time = -10000;
        for(int i = n - 1;i >= 0;i--){
            min_time = max(min_time, (double) (D - arr[i].first) / arr[i].second);
        }

        printf("Case #%d: %.6f\n", cs + 1, (double)D / min_time);
    }
}
