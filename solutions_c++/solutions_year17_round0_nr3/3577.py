#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

std::priority_queue<int> q;
int ans1, ans2;

void solve(int n, int s) {
    q = std::priority_queue<int>();
    q.push(n);
    for(int i=1; i<=s; ++i) {
        int l = q.top();
        q.pop();
        --l;
        int lr = l/2;
        int ls = l - lr;
        q.push(lr);
        q.push(ls);
        ans1 = min(lr, ls);
        ans2 = max(lr, ls);
    }
}

int main() {
    int t, n, s, tt;
    fin >> t;
    for(int tt = 1; tt <= t; ++tt) {
        fin >> n >> s;
        solve(n, s);
        fout << "Case #" << tt << ": " << ans2 << ' ' << ans1 << endl;
    }
    return 0;
}