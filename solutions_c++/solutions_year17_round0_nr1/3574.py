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


//Oversized Pancake Flipper
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
        string S;
        int K;
        
        long long result = 0;
        
        input >> S >> K;
        
        int startIndex = 0;
        bool imposible = false;
        while (startIndex < S.length())
        {
            while (S[startIndex] == '+')
                startIndex++;
            
            if (startIndex == S.length())
                break;
            
            if ((startIndex + K) > S.length())
            {
                imposible = true;
                break;
            }
            for (int i = startIndex; i < startIndex + K; i++)
            {
                if (S[i] == '-')
                {
                    S[i] = '+';
                }
                else
                    S[i] = '-';
            }
            result++;
        }
        
        if (imposible)
        {
            output << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
        else
        {
            output << "Case #" << t << ": " << result << endl;
        }
    }
    
    input.close();
    return 0;
}
