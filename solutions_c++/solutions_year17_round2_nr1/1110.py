#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

ifstream input("/Users/dwang/Downloads/A-large.in");

int n;
vector<double> k;
vector<double> s;
int D;
int N;

void init() {
    input >> D >> N;
    k.clear();
    s.clear();
    double kk, ss;
    for (int i = 0; i < N; ++i) {
        input >> kk >> ss;
        k.push_back(kk);
        s.push_back(ss);
    }
}

double solve() {
    double ans = D / (D - k[0]) * s[0];
    for (int i = 0; i < N; ++i) {
        if (D / (D - k[i]) * s[i] < ans) {
            ans = D / (D - k[i]) * s[i];
        }
    }
    return ans;
}

int main() {
    freopen("/Users/dwang/Documents/test/test/out2.txt", "w", stdout);
    int T;
    
    input >> T;
    for (int i = 0; i < T; ++i) {
        init();
        printf("Case #%d: %.8f\n", i + 1, solve());
    }
    input.close();
    return 0;
}
