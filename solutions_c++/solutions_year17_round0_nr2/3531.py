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


//Tidy Numbers
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
        string N;
        input >> N;
        
        for (long i = N.length() - 1; i >= 0 ; i--)
        {
            long j = i - 1;
            if (j >= 0)
            {
                if (N[j] > N[i])
                {
                    for (long index = i; index < N.length(); index++)
                    {
                        N[index] = '9';
                    }
                    N[j]--;
                }
            }
        }
        
        string result;
        int a = 0;
        while (N[a] == '0')
            a++;
        for (long i = a; i < N.length() ; i++)
        {
            result += N[i];
        }
        
        output << "Case #" << t << ": " << result << endl;
    }
    
    input.close();
    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
