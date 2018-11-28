//
//  main.cpp
//  test
//
//  Created by pzmrzy on 08/04/2017.
//  Copyright © 2017 pzmrzy. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <queue>
using namespace std;
int main(int argc, const char * argv[]) {
    ifstream fin;
    ofstream fout;
    fin.open("/Users/pzmrzy/Desktop/test/test/C-small-2-attempt1.in");
    fout.open("/Users/pzmrzy/Desktop/test/test/C_output.txt");
    int T, N, K, size, ls, rs;
    fin >> T;
    for (int tt=0; tt<T; tt++){
        fin >> N >> K;
        priority_queue<int> q;
        q.push(N);
        for (int i=0; i < K - 1; i++){
            size = q.top();
            q.pop();
            if (size == 1) continue;
            int t = (size - 1) / 2;
            q.push(t);
            q.push(size - 1 - t);
        }
        size = q.top();
        q.pop();
        ls = (size - 1) / 2;
        rs = (size - 1 - ls);
        int max, min;
        if (ls > rs){
            max = ls;
            min = rs;
        }else{
            max = rs;
            min = ls;
        }
        fout << "Case #" << tt + 1 << ": " << max << " " << min << endl;
    }
    fout.close();
    fin.close();
    
    return 0;
}
