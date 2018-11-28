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

const double PI = 3.14159265358979323846;

struct Blin {
    double h;
    double r;
};

bool operator<(const Blin& b1, const Blin& b2) {
    if(b1.r != b2.r)
        return b1.r > b2.r;
    return b1.h > b2.h;
}

int n,k;
Blin a[1500];

// D[i][j] took i, with j total
double D[1010][1010];

double side(int i) {
    // 2 * pi * r * h
    return a[i].r * a[i].h * PI * 2;
}

double top(int i) {
    return PI * a[i].r * a[i].r;
}

double fill() {
    int i, j;
    for(j=1; j<=k; ++j) {
        if(j==1) {
            for(i=0; i<n; ++i) {
                D[i][j] = side(i) + top(i);
            }
        }
        else {
            for(i=0; i<n; ++i) {
                for(int i1 = 0; i1<i; ++i1) {
                    if(D[i][j] < D[i1][j-1] + side(i)) {
                        D[i][j] = D[i1][j-1] + side(i);
                    }
                }
            }
        }
    }
}

double solve() {
    int i, j;
    for(i=0; i<n; ++i)
        for(j=0; j<=n; ++j) {
            D[i][j]=0;
        }
    sort(a, a + n);
    fill();
    double max = 0;
    for(i=0; i<n; ++i)
        if(D[i][k] > max)
            max = D[i][k];
    return max;
}

int main() {
    int t, tt, i;
    fin >> t;
    for(tt = 1; tt <= t; ++tt) {
        fin >> n >> k;
        for(i=0; i<n ;++i)
        {
            fin>>a[i].r >> a[i].h;
        }
        fout << fixed << setprecision(8);
        fout << "Case #" << tt << ": " << solve() << endl;
    }
    return 0;
}
