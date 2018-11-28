#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 0; t1 < t; ++t1) {
        cout << "Case #" << t1 + 1 << ": ";
        long long n, k;
        cin >> n >> k;
        long long two = 1;
        long long big = n;
        pair <long long, long long> sz;
        sz.first = 1;
        sz.second = 0;
        while (k - two > 0) {
            k -= two;
            two <<= 1;
            long long cb = 0, cs = 0;
            if (big % 2 == 0) {
                cb += sz.first;
                cs += sz.first;
                cs += 2 * sz.second;
            } else {
                cb += 2 * sz.first;
                cb += sz.second;
                cs += sz.second;
            }
            sz = make_pair(cb, cs);
            big /= 2;
        }
        if (k > sz.first)
        --big;
        long long l = (big - 1) / 2;
        cout << big - 1 - l << " " << l << endl;
    }
}
