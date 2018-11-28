#include <iostream>
#include <list>
#include <iomanip>
#include <set>
#include <vector>
#include <cstring>
#include <algorithm>
#include <complex>
#include <map>
#include <queue>
#include <stack>
#include <functional>
#include <unordered_set>
#include <unordered_map>
#include <float.h>

using namespace std;
const int MAX = 5 * 10000;
const long long MOD = 1e9 + 7;
const double PI = 3.141592653589793238462643383279502884;
const double EPS = 1e-9;



double dist_stand(double x1, double y1, double x2, double y2){
    return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}
int dist_man(int x1, int y1, int x2, int y2){
    return (abs(x1 - x2) + abs(y1 - y2));
}



int main()
{
    int t;
    cin >> t;
    for(int it = 0;it<t;it++){
        int n,k;
        cin >> n >> k;
        long long r[1001];
        long long h[1001];
        for(int i = 0;i<n;i++){
            cin >> r[i] >> h[i];
        }

        double ans = 0.0;
        for(int i = 0;i<n;i++){
            double cur_ans = 0.0;
            double sums = 0.0;
            vector<long long> hr;
            long long maxs = r[i];
            for(int l = 0;l<n;l++){
                if(r[l] <= r[i] and l!=i){
                    hr.push_back(h[l]*r[l]);
                }
            }
            if(hr.size()>=k-1){
                sort(hr.begin(),hr.end());
                for(int l = 0;l<k-1;l++){
                    sums+=hr[hr.size()-1-l];
                }

                cur_ans = sums*2*PI+PI*maxs*maxs + 2*PI*r[i]*h[i];
                if(cur_ans>ans){
                    ans = cur_ans;
                }
            }

        }


        //cin >> l >> r;

        cout << fixed<< setprecision(10)<< "Case #" << (it+1) << ": " << ans << endl;
    }


    //cout << endl;
    return 0;
}