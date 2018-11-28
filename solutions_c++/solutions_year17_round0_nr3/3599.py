#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#define ll long long int
#define mod 1000000007
#define pii pair<int, int>
#define fr(n) for (int i = 0; i < n; i++)
#define fr1(n) for (int i = 1; i <= n; i++)
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int T;
    in >> T;
    for (int U = 1; U <= T; U++) {
        out << "Case #" << U << ": ";
        int n, k;
        in >> n >> k;
        priority_queue<int> q;
        q.push(n);
        fr(k) {
            int m = q.top();
            q.pop();
            m--;
            if (i == k - 1) out << m - m / 2 << ' ' << m / 2 << '\n';
            if (m) q.push(m - m / 2);
            if (m) q.push(m / 2);
        }
    }
}
