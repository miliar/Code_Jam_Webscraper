//
//  main.cpp
//  CodeJam.0.Tidy
//
//  Created by David Song on 4/7/17.
//  Copyright © 2017 David Song. All rights reserved.
//

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int tidy(int n) {
    if (n == 1000) {
        return 999;
    }
    for (int i = n; i > 0; i--) {
        if (((i / 100) <= ((i % 100) / 10)) && (((i % 100) / 10) <= (i % 10))) {
            return i;
        }
    }
    return 0;
}

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        cout << "Case #" << i + 1 << ": " << tidy(n) << endl;
    }
}
