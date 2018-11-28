#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <iomanip>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int n,k;
double m;
double a[100];

double solve() {
    int i,j;
    while(m>0.000000001) {
        sort(a, a + n);
        double b = a[0];
        double d = 1;
        for(j=1; j<n; ++j)
            if(a[j] != b)
                break;
        if(j != n)
            d = a[j];
        if(j * (d-b) < m)
        {
            m -= j * (d-b);
            for(i=0; i<j; ++i)
                a[i] = d;
        }
        else {
            m /= j;
            for(i=0; i<j; ++i)
                a[i] += m;
            m = 0;
        }
    }
    double ans = 1;
    for(i=0; i<n; ++i)
        ans *= a[i];
    return ans;
}

int main() {
    int t, tt, i;
    fin >> t;
    for(tt = 1; tt <= t; ++tt) {
        fin >> n >> k;
        fin >> m;
        for(i=0; i<n; ++i)
            fin >> a[i];
        fout << fixed << setprecision(8);
        fout << "Case #" << tt << ": " << solve() << endl;
    }
    return 0;
}
