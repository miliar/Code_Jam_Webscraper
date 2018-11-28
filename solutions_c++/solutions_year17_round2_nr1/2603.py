//
//  main.cpp
//  Cruise Control
//
//  Created by Bill Zeng on 2017-04-22.
//  Copyright © 2017 Bill Zeng. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int t;
int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    fin >> t;
    for(int q = 1; q <= t; q++){
        int d, n;
        double m = 0;
        fin >> d >> n;
        while(n--){
            double a, b;
            fin >> a >> b;
            a = d - a;
            m = max(m, a/b);
        }
        fout << "Case #" << q << ": " << setprecision(6) << fixed << d/m << "\n";
    }
    return 0;
}
