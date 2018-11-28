//
//  pancake.cpp
//  
//
//  Created by John Nevard on 4/8/17.
//
//

#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using std::string;
using std::cin;
using std::cout;
using std::cerr;
using std::vector;
using std::swap;

int q(string& f, int w) {
    int np = f.size();
    int nf = 0;
    for (int i = 0; i < np; ++i) {
        if (f[i] == '+') continue;
        if (i + w <= np) {
            ++nf;
            for (int j = 0; j < w; ++j)
                f[i + j] = (f[i + j] == '-' ? '+' : '-');
        } else
            return -1;
    }
    return nf;
}

int main() {
    int n_cases;
    cin >> n_cases;
    for (int i = 1; i <= n_cases; ++i) {
        string f;
        int w;
        cin >> f >> w;
        int n = q(f, w);
        cout << "case #" << i << ": ";
        if (n >= 0)
            cout << n << '\n';
        else
            cout << "IMPOSSIBLE\n";
    }
    return 0;
}
