#include <iostream>
#include <fstream>
#include <map>
#include <cstdio>

using namespace std;

ifstream in("A-large.in");
//ofstream out("A-small-attempt0.out");
FILE *file = fopen("A-large.out", "w");

//#define out cout

int main()
{
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        long long d, n;
        in >> d >> n;
        long long k[n], s[n];
        double ans = 1000000000000000.0;
        for (int j = 0; j < n; ++j) {
            in >> k[j] >> s[j];
            double m = (double) d * (double) s[j] / (double) (d - k[j]);
            if (m < ans) ans = m;
        }
        fprintf(file, "Case #%d: %6f\n", i+1, ans);
        //out << "Case #" << i + 1 << ": " << ans << '\n';
    }
    return 0;
}
