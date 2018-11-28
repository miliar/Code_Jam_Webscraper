//
//  main.cpp
//  codejam1b01
//
//  Created by hyspace on 4/22/17.
//  Copyright © 2017 hyspace. All rights reserved.
//

#include <iostream>
#include <set>
#include <queue>

using namespace std;

double cal(vector<int>& k, vector<int>& s, int d){
    double max = 0;
    for(int i = 0; i < k.size(); ++i){
        int dd = d - k[i];
        double t = (double) dd / (double) s[i];
        if(t > max) max = t;
    }
    return (double) d / max;
}

int main(int argc, const char * argv[]) {
    int num_cases;
    cin >> num_cases;
    for(int i = 0; i < num_cases; ++i){
        int d, n;
        cin >> d;
        cin >> n;
        vector<int> k;
        vector<int> s;
        for(int j = 0; j < n; ++j){
            int _k, _s;
            cin >> _k;
            cin >> _s;
            k.push_back(_k);
            s.push_back(_s);
        }
        
        cout << "case #" << i + 1 << ": ";
        
        printf("%.6lf\n", cal(k,s,d));
    }
    return 0;
}
