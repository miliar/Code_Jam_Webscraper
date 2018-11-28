//
//  main.cpp
//  googleJam
//
//  Created by Nguyen Viet Trung on 3/29/16. now is 17
//  Copyright © 2016 Nguyen Viet Trung. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <sstream>
#include <algorithm>    // std::set_intersection, std::sort
#include <vector>       // std::vector
#include <iomanip>
#include <math.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>
using namespace std;

//Problem A. Steed 2: Cruise Contro
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream input;
    input.open("input.txt");

    ofstream output;
    output.open("output.txt");
    int T;
    input >> T;

    for (int t = 1; t <= T; t++) {
        double D, N;
        input >> D >> N;
        
        double K[1001];
        double S[1001];
        for (int n = 0; n < N; n++) {
            input >> K[n] >> S[n];
        }
        double Time[1001];
        double maxTime = -1;
        for (int n = 0; n < N; n++) {
            Time[n] = (D - K[n])/S[n];
            maxTime = max(maxTime, Time[n]);
        }
        double result = D / maxTime;
        
        output << "Case #" << t << ": " << setprecision(6) << fixed << result << endl;

    }

    input.close();
    return 0;
}

