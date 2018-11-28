#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#define INF 1791791791
using namespace std;


int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int t;
    in >> t;
    out.precision(30);
    for (int i = 0; i < t; ++i) {
        int d, n;
        in >> d >> n;
        double mh = 0;
        for (int i = 0; i < n; ++i) {
            int k, s;
            in >> k >> s;
            mh = max(mh, (d - k) * 1. / s);
        }
        out << "Case #" << i + 1 << ": " << d / mh << '\n';
    }
}
