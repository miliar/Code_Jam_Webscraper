//
//  main.cpp
//  BathroomStalls
//
//  Created by Wenzhen Zhu on 4/8/17.
//  Copyright © 2017 Wenzhen Zhu. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>

using namespace std;

typedef pair<int,int> ii;
typedef pair<int,ii> iii;



#define filename "C-small-2-attempt0"

struct input {
    int N;
    int K;
};

struct output {
    int MAX;
    int MIN;
};

void read(ifstream &in, input &test) {
    in >> test.N >> test.K;
}

void write(ofstream &out, output test) {
    out << test.MAX << " " << test.MIN;
}

output solve (input test) {
    
    output result;
    
    iii u;
    u.second.first = -1;
    u.second.second = test.N + 1;
    u.first = u.second.second + u.second.first;
    priority_queue<iii> pq;
    pq.push(u);
    
    iii v;
    int mid;
    iii last1;
    iii last2;
    
    for(int i = 1; i <= test.K; i++){
        u = pq.top();
        pq.pop();
        mid = (u.second.second - u.second.first - 1) / 2;
        v.second.second = mid;
        v.second.first = u.second.first;
        v.first =  (v.second.second + v.second.first);
        last1 = v;
        pq.push(v);
        v.second.first = -(mid+1);
        v.second.second = u.second.second;
        v.first = v.second.second + v.second.first;
        pq.push(v);
        last2 = v;
    }
    int val1 = last1.second.second + last1.second.first;
    pq.pop();
    int val2 = last2.second.second + last2.second.first;
    
    result.MAX = max(val1, val2);
    result.MIN = min(val1, val2);

    return result;
}

void readAll(vector <input> &tests) {
    ifstream in("/Users/wenzhen/Downloads/" + (string)filename + ".in");
    
    int T;
    in >> T;
    tests.resize(T);
    for (int i = 0; i < T; i++) {
        read(in, tests[i]);
    }
    in.close();
}

void solveAll(vector <input> &tests, vector <output> &results) {
    results.resize(tests.size());
    for (int i = 0; i < tests.size(); i++) {
        results[i] = solve(tests[i]);
        //cout << tests[i].N << " " << tests[i].K << " " << results[i].MAX << " " << results[i].MIN << endl;
    }
}

void writeAll(vector <output> &results) {
    ofstream out("/Users/wenzhen/Downloads/" + (string)filename + ".out");
    
    out << "Case #1: ";
    write(out, results[0]);
    for (int i = 1; i < results.size(); i++) {
        out << endl << "Case #" << i+1 << ": ";
        write(out, results[i]);
    }
    
    out.close();
}

int main(int argc, const char * argv[]) {
    vector <input> tests;
    vector <output> results;
    
    readAll(tests);
    solveAll(tests, results);
    writeAll(results);
    
    
//    input test;
//    test.N = 1000;
//    test.K = 1;
//    
//    output out1 = solve(test);
//    cout << out1.MAX << " " << out1.MIN << endl;
    
    
    return 0;
}
