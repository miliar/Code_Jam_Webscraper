#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <fstream>
#include <cmath>
# define M_PI           3.14159265358979323846

using namespace std;

ifstream in("A.in");
ofstream out("A.out");

bool cmp(pair <long double, long double> a, pair <long double, long double> b){
    return a.second * a.first > b.first * b.second;
}

int main(){
    int t, n, k;
    in >> t;
    for (int q = 0; q < t; q++){
        in >> n >> k;
        int indmax = 0;
        vector <pair <long double, long double> > a(n);
        for (int i = 0; i < n; i++){
            in >> a[i].second >> a[i].first;
            if (a[indmax].second < a[i].second || (a[indmax].second == a[i].second && a[indmax].first < a[i].first)){
                indmax = i;
            }
        }
        long double r = a[indmax].second;
        long double d = a[indmax].first;
        a[indmax].first = 0;
        a[indmax].second = 0;
        sort(a.begin(), a.end(), cmp);
        long double res = 0;
        long double maxr = a[k - 1].second;
        for (int i = 0; i < k - 1; i++){
            res += a[i].second * a[i].first * M_PI * 2;
            maxr = max(maxr, a[i].second);
        }
        res += max(maxr * maxr * M_PI + a[k - 1].first * a[k - 1].second * M_PI * 2, r * r * M_PI + r * d * 2 * M_PI);
        out << fixed << setprecision(10) << "Case #" << q + 1 << ": " << res << endl;
    }
}
