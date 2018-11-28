#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int tcase;
int n,k;
vector < pair <double,double> > v;
double dp[1010][1010];


double solve(int pos, int rem){
    if (pos >= n || rem >= k) {
        return 0;
    }
    if (dp[pos][rem] != 0) {
        return dp[pos][rem];
    }
    double hArea = 2*M_PI*v[pos].first*v[pos].second;
    double tArea = M_PI*v[pos].first*v[pos].first;
    if (rem == 0){
        dp[pos][rem] = max(solve(pos+1,rem+1)+hArea+tArea, solve(pos+1,rem));
    } else {
        dp[pos][rem] = max(solve(pos+1,rem+1)+hArea, solve(pos+1,rem));
    }
    return dp[pos][rem];
}

int main(){
    cin >> tcase;
    for (int t=0;t<tcase;t++){
        v.clear();
        fill(&dp[0][0], &dp[1010][0], 0);
        cin >> n >> k;
        double r, h;
        for (int i=0;i<n;i++){
            cin >> r >> h;
            v.push_back(make_pair(r,h));
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        double ans = solve(0, 0);
        cout << "Case #" << t+1 << ": " << fixed << setprecision(9) << ans << endl;
    }
}