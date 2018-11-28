#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

void solveTaskA(string infile, string outfile) {
    ifstream in;
    in.exceptions(std::ifstream::failbit);
    in.open(infile);
    ofstream out;
    out.open(outfile);
    int ncases = 0;
    in >> ncases;
    for (int c = 1; c <= ncases; c++) {
        int n, k;
        in >> n >> k;

        uint64_t r[n];
        uint64_t h[n];

        for (int i = 0; i < n; i++) {
            in >> r[i] >> h[i];
        }

        uint64_t smax = 0;
        for (int p = 0; p < n; p++) {
            vector<uint64_t> d;
            for (int i = 0; i < n; i++)
                if (i != p && r[i] <= r[p])
                    d.push_back(r[i] * h[i]);
            if (d.size() < k - 1) continue;
            sort(d.begin(), d.end());
            uint64_t s = r[p] * r[p] + 2 * r[p] * h[p];
            for (int i = 1; i < k; i++)
                s += 2 * d[d.size() - i];
            if (s > smax) smax = s;
        }

        out << setprecision(25);
        out << "Case #" << c << ": ";
        out << M_PI * smax;
        out << endl;
    }    
    in.close();
    out.close();
}

int main()
{
    solveTaskA("A-large.in", "output.txt");
    return 0;
}
