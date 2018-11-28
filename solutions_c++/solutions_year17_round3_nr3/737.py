#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

ifstream in("C.in");
ofstream out("C.out");

int main(){
    int t;
    in >> t;
    for (int q = 0; q < t; q++){
        int n, k;
        long double u;
        in >> n >> k >> u;
        vector <long double> a(n);
        for (int i = 0; i < n; i++){
            in >> a[i];
        }
        sort(a.begin(), a.end());
        long double sum1 = u + a[0];
        int up = n;
        for (int i = 1; i < n; i++){
            if (sum1 / i < a[i]){
                up = i;
                break;
            }
            sum1 += a[i];
        }
        long double res = 1;
        for (int i = 0; i < up; i++){
            res *= min((long double)1.0, sum1 / up);
        }
        for (int i = up; i < n; i++){
            res *= a[i];
        }
        out << fixed << setprecision(10) << "Case #" << q + 1 << ": " << res << endl;
    }
}
