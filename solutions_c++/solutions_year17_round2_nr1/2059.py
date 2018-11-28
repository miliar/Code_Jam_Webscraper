#include <iostream>
#include <algorithm>
#include <fstream>
#include <iomanip>
#define MOD 1000000007
#define DN 16
#define LL long long
using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int main(){
    int tst, d, n, k, v;
    double tmax;
    freopen("input.txt","r",stdin);
    fin >> tst;
    for(int T = 1; T <= tst; ++T) {
        fin >> d >> n;
        tmax = 0;
        for (int i = 0; i < n; ++i) {
            fin >> k >> v;
            tmax = max(tmax, (d - k) / (1.0 * v));
        }
        fout << "Case #" << T << ": ";
        fout << fixed << setprecision(6) << d / tmax << '\n';
    }
}