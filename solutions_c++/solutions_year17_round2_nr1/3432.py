#ifdef F
#include <fstream>
std::ifstream cin("input.txt");
std::ofstream cout("output.txt");
#else
#include <iostream>
using std::cin;
using std::cout;
#endif
#include <sstream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
        long d;
        int n;
        cin >> d >> n;
        long double mt = 0;
        for (int j=0; j<n; j++) {
            long k; int s;
            cin >> k >> s;
            long double kt = ((long double)d - (long double)k)/(long double)s;
            if (kt > mt) mt = kt;
        }
        long double ss = (long double) d / mt;
        cout << "Case #" << i+1 << ": "<< setprecision (10) << ss <<"\n";
    }
    return 0;
}
