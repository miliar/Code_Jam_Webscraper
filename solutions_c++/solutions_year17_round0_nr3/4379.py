//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Bill Zeng on 2017-04-08.
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
using namespace std;
int t;

int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream fin("C-small-2-attempt0.in");
    ofstream fout("output1.txt");
    fin >> t;
    for(int q = 1; q <= t; q++){
        long long a, b;
        fin >> a >> b;
        priority_queue<long long> Q;
        Q.push(a);
        b--;
        while(b--){
            long long cur = Q.top(); Q.pop();
            cur--;
            Q.push(ceil(cur/2.0));
            Q.push(floor(cur/2.0));
        }
        long long c = Q.top() - 1;
        fout << "Case #" << q << ": " << ceil(c/2.0) << " " << floor(c/2.0) << "\n";
    }
    cout << "done";
    return 0;
}
