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

/*
 One line with two integers: N, the number of cities with horses, and Q, the number of pairs of stops we are interested in. Cities are numbered from 1 to N.
N lines, each containing two integers Ei, the maximum total distance, in kilometers, the horse in the i-th city can go and Si, the constant speed, in kilometers per hour, at which the horse travels.
N lines, each containing N integers. The j-th integer on the i-th of these lines, Dij, is -1 if there is no direct route from the i-th to the j-th city, and the length of that route in kilometers otherwise.
Q lines containing two integers Uk and Vk, the starting and destination point, respectively, of the k-th pair of cities we want to investigate.
 */

int n, q;
int e[110]; // Total distanc horce can go
int s[110]; // Horse speed
int d[110][110];
int u[110];
int v[110];

double minTime;

bool back(int i, double hDist, double hSpeed, double time) {
    if(hDist < 0)
        return false;

    if(i == n-1) {
        if(minTime > time || minTime == -1) {
            minTime = time;
        }
        return true;
    }
    if((hDist != e[i] || hSpeed != s[i]) && back(i, e[i], s[i], time));
    return back(i+1, hDist - d[i][i+1], hSpeed, time + (double)d[i][i+1]/hSpeed);
}

double solve() {
    minTime = -1;
    back(0, 0, 0, 0);
    return minTime;
}

int main() {
    string ans;
    long long i, j, t, tt;
    fin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        fin >> n >> q;
        for(i=0; i<n; ++i)
            fin >> e[i] >> s[i];
        for(i=0; i<n; ++i)
            for(j=0; j<n; ++j)
                fin >> d[i][j];
        for(i=0; i<q; ++i)
            fin >> u[i] >> v[i];
        fout << fixed << setprecision(8);
        fout << "Case #" << tt << ": " << solve() << endl;
    }
    return 0;
}