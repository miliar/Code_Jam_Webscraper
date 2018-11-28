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
    for(int ti = 0;ti<t;ti++){
        int n,q;
        cin >> n >> q;
        double e[101],s[101];
        for(int i = 0;i<n;i++){
            cin >> e[i] >> s[i];
        }
        int d[101][101];
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                cin >> d[i][j];
            }
        }
        double d2[101];
        d2[0] = 0;
        for(int i = 1;i<n;i++){
            d2[i] = d2[i-1]+d[i-1][i];
        }
        int u,v;
        cin >> u >> v;

        double y = 0.0;

        double z[101];
        z[0] = 0.0;
        for(int i = 1;i<n;i++){
            double mins_time = DBL_MAX;
            for(int j = 0;j<i;j++){
                double times = z[j];
                if(e[j]>=d2[i]-d2[j]){
                    times+= (d2[i]-d2[j])/s[j];
                    mins_time = min(mins_time,times);
                }
            }
            z[i] = mins_time;
        }


        cout << "Case #"<< (ti+1) <<": ";
        cout << fixed<< setprecision(8) << z[n-1];
        cout << endl;
    }

    return 0;
}