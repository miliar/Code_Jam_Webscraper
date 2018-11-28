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
        int d,n;
        cin >> d >> n;
        double s[1001];
        double k[1001];
        for(int i = 0;i<n;i++){
            cin >> k[i] >> s[i];
        }
        double max_v = 1e30;
        for(int i = 0;i<n;i++){
            double ost_d = d-k[i];
            double time = ost_d/s[i];
            double v = d/time;
            max_v = min(v,max_v);

        }


        cout << std::fixed << setprecision(8) << "Case #"<< (ti+1) <<": " << max_v;


        cout << endl;
    }

    return 0;
}