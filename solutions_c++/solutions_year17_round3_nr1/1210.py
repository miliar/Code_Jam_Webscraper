#include <bits/stdc++.h>

#define LL long long
#define ii pair<LL, LL>

using namespace std;

void _solve() {
    int n, k;
    scanf("%d %d", &n, &k);

    long double pi = atan(1) * 4;
    long double res = 0;

    vector<ii> data(n);
    for(int i = 0; i < n; i++) {
        scanf("%lld %lld", &data[i].first, &data[i].second);
    }

    int j = max_element(data.begin(), data.end()) - data.begin();
    ii mR = data[j];

    res += (long double) mR.first * mR.first * pi; 
    res += (long double) 2 * mR.first * mR.second * pi;

    vector<LL> data2(n);
    for(int i = 0; i < n; i++) {
        if(i != j)
            data2.push_back(data[i].first * data[i].second * 2);
    }
    
    sort(data2.begin(), data2.end());
    reverse(data2.begin(), data2.end());
    for(int i = 0; i < k - 1; i++) {
        res += (long double) data2[i] * pi;
    }

    long double res2 = 0;
    vector<ii> data3(n);
    for(int i = 0; i < n; i++) {
        data3.push_back({data[i].first * data[i].second * 2, i});
    }

    sort(data3.begin(), data3.end());
    reverse(data3.begin(), data3.end());   
    vector<LL> data4;
    for(int i = 0; i < k; i++) {
        data4.push_back(data[data3[i].second].first);
        res2 += (long double) data3[i].first * pi;
    }
    
    long double a = (long double) *max_element(data4.begin(), data4.end());
    res2 += a * a * pi;
    
    printf("%.10LF\n", max(res, res2));
}

int main() {
    int t;
    scanf("%d", &t);

    for(int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        _solve();
    }
    return 0;
}