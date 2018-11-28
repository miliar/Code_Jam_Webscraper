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

int n;
double d;
double k[1100]; // position
double s[1100]; // speed

double solve() {
    double time=0;
    int i;
    for(i=n-1; i>=0; --i) {
        double newTime = (d - k[i]) / s[i];
        if(newTime > time)
            time = newTime;
    }
    return d/time;
}

int main() {
    string ans;
    long long i, t, tt;
    fin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        fin >> d >> n;
        for(i=0; i<n; ++i)
        {
            fin >> k[i] >> s[i];
        }
        fout << fixed << setprecision(7);
        fout << "Case #" << tt << ": " << solve() << endl;
    }
    return 0;
}