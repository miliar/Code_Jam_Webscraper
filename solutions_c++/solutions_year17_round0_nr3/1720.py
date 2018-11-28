#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        long long n, k;
        in >> n >> k;
        long long a = n;
        long long ca = 1, cb = 0;
        while (ca + cb < k) {
            k -= ca + cb;
            if (a % 2 == 0) {
                cb = cb * 2 + ca;
            }
            else {
                ca = ca * 2 + cb;
            }
            a /= 2;
        }
        long long x, y;
        if (ca >= k) {
            x = a / 2;
            y = (a - 1) / 2;
        }
        else {
            x = (a - 1) / 2;
            y = (a - 2) / 2;
        }
        out << "Case #" << i + 1 << ": " << x << ' ' << y << '\n';
    }
}
