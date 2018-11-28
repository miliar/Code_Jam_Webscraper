//
//  main.cpp
//  CodeJam-qr-03
//
//  Created by 张云尧 on 2017/4/8.
//  Copyright © 2017年 张云尧. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in("C-large.in");
    ofstream out("C-large.out");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        long long n, k;
        in >> n >> k;
        while (k != 1) {
            --n;
            --k;
            n = n / 2 + n % 2 * k % 2;
            k = k / 2 + k % 2;
        }
        --n;
        out << "Case #" << i + 1 << ": " << n - n / 2 << " " << n / 2 << endl;
        
    }
    return 0;
}
