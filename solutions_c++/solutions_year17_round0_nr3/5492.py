//
//  mainC.cpp
//  CJ
//
//  Created by Brian Lui on 7/4/2017.
//  Copyright © 2017 Brian Lui. All rights reserved.
//

#include <stdio.h>

#include <iostream>
#include <string>
#include <set>
#include <iterator>

using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    int caseN = 1;
    unsigned long n, k;
    multiset<unsigned long> s;
    unsigned long l, r, curr;
    multiset<unsigned long>::iterator it;
    
    while (t--) {
        cin >> n >> k;
        s.clear();
        s.insert(n);
        
        for (int i = 0; i < k; i++) {
            it = s.end();
            it--;
            curr = *it;
            r = curr >> 1;
            l = (curr > 0) ? (curr - 1) >> 1 : 0;
            s.erase(it);
            s.insert(l);
            s.insert(r);
        }
        
        cout << "Case #" << caseN++ << ": " << r << " " << l << endl;
    }
    
    
    return 0;
}
