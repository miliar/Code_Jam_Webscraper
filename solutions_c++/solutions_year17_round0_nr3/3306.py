//
//  main.cpp
//  C. Bathroom Stalls
//
//  Created by Jason Naldi on 08.04.17.
//  Copyright © 2017 jasonnaldi. All rights reserved.
//

#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>

#define READ_IN in
#define PRINT_OUT out

using namespace std;

namespace Path {
    string path = "/Users/jason/Documents/School/Uni/CS/Bachelor/2nd semester/Computer Challenges Lab/Google Codejam/2017/";
    string round = "1. Qualification Round/";
    string problemName = "C. Bathroom Stalls/";
    string file_name = path + round + problemName + "/tests/large";
    string file_in = file_name + "_input.txt";
    string file_out = file_name + "_output.txt";
}

typedef int64_t number_t;

struct Distances {
    number_t Ls;
    number_t Rs;
};

Distances getLastDistance(number_t K, Distances d, ssize_t depth = 1) {
    if (K < depth)
        return d;
    
    number_t deltaModulo = K % depth;
    K -= deltaModulo;
    
    number_t previousSpots = 0;
    if (deltaModulo == 0)
        // go right on the tree
        previousSpots = d.Rs;
    else
        // go left on the tree
        previousSpots = d.Ls;
  
    number_t takenSpot = previousSpots / 2;
    
    d.Ls = previousSpots - takenSpot - 1;
    d.Rs = previousSpots - d.Ls - 1;
    
    return getLastDistance(K, d, depth * 2); // *2 faster than pow(2, depth)
}

int main(int argc, const char * argv[]) {
    // Speeds up input reading and output printing.
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    ifstream in(Path::file_in);
    ofstream out(Path::file_out);
    
    int T = 0;
    READ_IN >> T;
    
    for (int test = 1; test <= T; ++test) {
        number_t N = 0;
        number_t K = 0;
        READ_IN >> N >> K;
        
        Distances d = getLastDistance(K, Distances{N, N});
        
        PRINT_OUT << "Case #" << test << ": " << max(d.Ls, d.Rs) << " " << min(d.Ls, d.Rs) << "\n";
        cout << test << "\n";
    }
    
    return 0;
}
