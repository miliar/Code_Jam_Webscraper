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
    for(int l = 0;l<t;l++){
        long long mins,maxs;
        long long k,n;
        cin >> n >> k;
        while (k >1){
            if(n%2==1){
                n = (n-1)/2;
                k = k/2;
            }
            else{
                if(k%2==0){
                    n = (n-1)/2 + 1;
                    k = k/2;
                }
                else{
                    n = (n-1)/2;
                    k = (k-1)/2;
                }
            }
        }
        maxs = max((n-1)/2,n-1-(n-1)/2);
        mins = min((n-1)/2,n-1-(n-1)/2);

        cout << "Case #" << (l+1) << ": ";
        cout << maxs << " " << mins;
        cout << endl;
    }

    cout << endl;
    return 0;
}