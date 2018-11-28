#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

const double pi = acos(-1.0);
struct pancake{
    double r;
    double h;
    double get_nyam_with_rad_hight(){
        return pi*r*r+2*pi*r*h;
    }
    double get_nyam_with_hight(){
        return 2*pi*r*h;
    }
};

bool cmp(pancake a, pancake b){
    return a.r > b.r;
}
double solve(vector<pancake>& pnc, int k){
    int  n = pnc.size();
    vector< vector<double> > dp(n+1, vector<double>(n+1,-1.0));
    sort(pnc.begin(), pnc.end(),cmp);
    for(int i=0; i<n; ++i){
        dp[1][i] = pnc[i].get_nyam_with_rad_hight();
    }
    for(int i=2; i<=k;++i){
        for(int j=0; j<n;++j){
            for(int t = 0; t<j; ++t){
                if(dp[i-1][t] < 0) continue;
                dp[i][j] = max(dp[i][j], dp[i-1][t]+pnc[j].get_nyam_with_hight());
            }
        }
    }
    double ans = -1.0;
    for(int i=0; i<n;++i){
        ans= max(ans, dp[k][i]);
    }
    return ans;
}

int main(){
    ios_base::sync_with_stdio(0);
    freopen("/Users/kasparyanm/Downloads/A-large.in","rt",stdin);
    freopen("/Users/kasparyanm/Downloads/A-large.out","wt",stdout);
    int t;
    cin >> t;
    int text_num = 0;
    while(t){
        ++text_num;
        --t;
        int n,k;
        cin >> n >> k;
        vector<pancake> pnc(n);
        for(int i=0; i<n; ++i){
            cin >>pnc[i].r >> pnc[i].h;
        }
        cout.setf(ios::fixed);
        cout.precision(8);
        cout << "Case #"<<text_num<<": "<<solve(pnc, k)<<endl;
        
    }
    return 0;
}
