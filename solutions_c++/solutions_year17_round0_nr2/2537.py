//
//  tidy.cpp
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

typedef vector<long> VL;

string f(long n) {
    char buf[20];
    sprintf(buf, "%ld", n);
    string s = buf;
    string t = s;
    int nd = s.size();
    for (int i = 0; i < nd; ++i) {
        string u(nd - i, s[i]);
        if (s.substr(i, nd - i) >= u)
            t[i] = s[i];
        else {
            t[i] = s[i] - 1;
            for (int j = i + 1; j < nd; ++j)
                t[j] = '9';
            if (t[0] == '0')
                t = t.substr(1, nd - 1);
            return t;
        }
    }
    return t;
}

int main() {
    int n_cases;
    cin >> n_cases;
    for (int i = 1; i <= n_cases; ++i) {
        long n;
        cin >> n;
        string m = f(n);
        cout << "case #" << i << ": " << m << '\n';
    }
    return 0;
}
