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
        /*int ac,aj;
        int c[101],d[101];
        int j[101],k[101];
        for(int i = 0;i<ac;i++){
            cin >> c[i] >> d[i];
        }
        for(int i = 0;i<aj;i++){
            cin >> j[i] >> k[i];
        }

        int ans = 0;
        */
        int n,k;
        cin >> n >> k;
        double u;
        cin >> u;
        vector<double> p;
        vector<double> ud(n,0);
        for(int i = 0;i<n;i++){
            double x;
            cin >> x;
            p.push_back(x);
        }
        sort(p.begin(),p.end());
        int ind = 0;
        while(u>0 and ind < n){
            double diff = 1-p[ind];
            if(u>diff){
                ud[ind] = 1-p[ind];
                u-=diff;
            }
            else{
                ud[ind] = u;
                u = 0;
                break;
            }
            ind+=1;

        }
        double ans = 1;
        for(int i = 0;i<n;i++){
            ans = ans*(p[i]+ud[i]);
        }
        double prev_ans = 1;
        while(abs(ans-prev_ans)>1e-7){
            for(int i = 0;i<n;i++){
                for(int j = 0;j<n;j++){
                    double us = ud[i]+ud[j];
                    if(p[i]>p[j]){
                        if(p[i]>=p[j]+us){
                            ud[j] = us;
                            ud[i] = 0;
                        }
                        else{
                            ud[j] = p[i]-p[j];
                            us-=ud[j];
                            ud[j]+=us/2.0;
                            ud[i] = us/2.0;
                        }
                    }
                    else if(p[i]==p[j]){
                        ud[j] =us/2.0;
                        ud[i] = us/2.0;
                    }
                }
            }
            prev_ans = ans;
            ans = 1;
            for(int i = 0;i<n;i++){
                ans = ans*(p[i]+ud[i]);
            }
        }


        cout << fixed<< setprecision(10)<< "Case #" << (it+1) << ": " << ans << endl;
    }


    //cout << endl;
    return 0;
}