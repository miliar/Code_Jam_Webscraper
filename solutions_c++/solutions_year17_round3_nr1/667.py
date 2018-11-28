#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
//#include "utils/haha.h"
//#include "utils/max_flow.h"
using namespace std;
typedef pair<int, int> PII;
typedef pair<string, string> PSS;
typedef pair<int, PII> PIP;
typedef long long ll;
typedef pair<ll, ll> PLL;
typedef pair<double, double> PDD;
typedef pair<ll, PII> PLP;
#define CLS(x, v) (memset((x), (v), sizeof((x))))
const double pi = acos(-1);

int N, K;
double area1(PII &p) {
    return pi * p.first *2.0* p.second;
}
void solve(int ncase) {
    cout << "Case #" << ncase << ": ";
    cin >> N >> K;
    vector<PII> p(N);
    for(int i = 0; i < N; i++) {
        cin >> p[i].first >> p[i].second;
    }
    sort(p.begin(), p.end());
    double ans = 0;
    priority_queue<double, vector<double>, greater<double>> pq;
    double sum = 0;
    for(int i = 0; i < K-1; i++) {
        double x = area1(p[i]);
        sum += x;
        pq.push(x);
    }
    for(int i = K - 1; i < N; i++) {
        double tmp = pi * p[i].first *1.0* p[i].first + area1(p[i]);
        //cout << sum/pi << " " << tmp/pi << " " << (tmp + sum)/pi << endl;
        ans = max(tmp + sum, ans);
        double x = area1(p[i]);
        pq.push(x);
        sum += x;
        sum -= pq.top();
        pq.pop();
    }
    cout << ans << endl;
}


int main() {
    //ios::sync_with_stdio(false);
    cout << std::fixed;
    cout << setprecision(16);
#ifdef _zzz_
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
#endif
    //precalc();
    int T = 1;
    scanf("%d", &T);
    //cin >> T;
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
