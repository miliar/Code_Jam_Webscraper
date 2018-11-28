#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <list>
#include <limits>
#include <algorithm>
#include <utility>
#include <array>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef long long ull;

ifstream inputStream;

int t;

double d;
int n;

array<double, 1000> k;
array<double, 1000> s;

void solve(int t) {
    inputStream >> d >> n;
    for(int i=0; i<n; i++) {
        inputStream >> k[i] >> s[i];
    }
    double best = (d - k[0]) / s[0];
    for(int i=0; i<n; i++) {
        double arrival = (d - k[i]) / s[i];
        if(arrival > best) {
            best = arrival;
        }
    }
    double speed = d / best;
    cout << setprecision(10) << fixed << "Case #" << t << ": " << speed << endl;
}

int main(int argc, char** argv) {

    if(argc == 1) {

    } else {
        inputStream = ifstream(argv[1]);
        inputStream >> t;
    }

    for(int i=0; i<t; i++) {
        solve(i+1);
    }

}