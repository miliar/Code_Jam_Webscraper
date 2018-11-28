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


//Bathroom Stalls
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
        long long N, K;
        input >> N >> K;
        
        long long result;
        
        long long a = (int)(log2l(K));
        result = (long long)(N / (pow(2, a)));
        
        long long total = (pow(2, a + 1)) - (pow(2, a));
        long long Kdu = K - (pow(2, a));
        
        if (N % 2 == 0) //chan
        {
            long long x = N/2; //so lon
            long long y = N/2 - 1; //so be
            long long xNum = 1;
            long long yNum = 1;
            long long k = 1;
            while (k < a)
            {
                
                if ((x % 2 != 0) && (y % 2 == 0))
                {
                    xNum = 2*xNum + yNum;
                    yNum = yNum;
                }
                else if((x % 2 == 0) && (y % 2 != 0))
                {
                    xNum = xNum;
                    yNum = 2*yNum + xNum;
                }
                x = x/2;
                y = x-1;
                k++;
            }
            //                output << "Case #" << t << ": " << xNum << " " << yNum  << endl;
            if (Kdu >= xNum)
                result = result -  1;
        }
        else //le
        {
            long long x = N/2; //so lon
            long long y = N/2; //so be
            long long xNum = 1;
            long long yNum = 1;
            long long k = 1;
            while (k < a)
            {
                if ((x % 2 != 0) && (y % 2 == 0))
                {
                    xNum = 2*xNum + yNum;
                    yNum = yNum;
                }
                else if((x % 2 == 0) && (y % 2 != 0))
                {
                    xNum = xNum;
                    yNum = 2*yNum + xNum;
                }
                else if((x % 2 == 0) && (y % 2 == 0))
                {
                    xNum = 2*xNum;
                    yNum = 2*yNum;
                }
                else if((x % 2 != 0) && (y % 2 != 0))
                {
                    xNum = 2*xNum;
                    yNum = 2*yNum;
                }
                x = x/2;
                y = x-1;
                k++;
            }
            //                output << "Case #" << t << ": " << xNum << " " << yNum  << endl;
            if (Kdu > xNum + 1)
                result = result -  1;
            
        }
        if (result % 2 == 0)
        {
            output << "Case #" << t << ": " << max(result/2,(result/2 - 1)) << " " << ((min(result/2,(result/2 - 1)) >= 0) ? min(result/2,(result/2 - 1)) : 0)  << endl;
        }
        else
        {
            output << "Case #" << t << ": " << result/2 << " " << result/2  << endl;
        }
    }
    
    input.close();
    return 0;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////
////  main.cpp
////  googleJam
////
////  Created by Nguyen Viet Trung on 3/29/16. now is 17
////  Copyright © 2016 Nguyen Viet Trung. All rights reserved.
////
//
//#include <iostream>
//#include <fstream>
//#include <istream>
//#include <string>
//#include <sstream>
//#include <algorithm>    // std::set_intersection, std::sort
//#include <vector>       // std::vector
//#include <iomanip>
//#include <math.h>
//#include <cstdio>
//#include <algorithm>
//#include <vector>
//#include <string>
//#include <set>
//#include <map>
//#include <queue>
//#include <deque>
//#include <list>
//#include <complex>
//#include <stack>
//#include <cmath>
//#include <iostream>
//#include <sstream>
//#include <cctype>
//#include <cstdlib>
//#include <utility>
//#include <bitset>
//#include <assert.h>
//#include <stdio.h>      /* printf, NULL */
//#include <stdlib.h>
//using namespace std;
//
//
////Bathroom Stalls
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//int main(int argc, const char * argv[]) {
//    // insert code here...
//    ifstream input;
//    input.open("input.txt");
//
//    ofstream output;
//    output.open("output.txt");
//    int T;
//    input >> T;
//
//    for (int t = 1; t <= T; t++) {
//        long long N, K;
//        input >> N >> K;
//
//        long long result = N;
//        vector<long long> arr;
//        long long temp1;
//        arr.push_back(N);
//        for (long long ab = 0; ab < K; ab++)
//        {
//            sort(arr.begin(), arr.end(), greater<int>());
//            result = arr[0];
////            output << "step #" << ab << ": result" << result << " ";
//            temp1 = result/2;
//            arr.push_back(temp1);
////            output << "step #" << ab << ": " << temp1 << " ";
//            if (result % 2 == 0)
//            {
//                temp1--;
//            }
//            arr.push_back(temp1);
////            output << temp1 << " " << endl;
////            output << "erase" << arr[0] << endl;
//            arr.erase(arr.begin());
//        }
//        if (result % 2 == 0)
//        {
//            output << "Case #" << t << ": " << max(result/2,(result/2 - 1)) << " " << ((min(result/2,(result/2 - 1)) >= 0) ? min(result/2,(result/2 - 1)) : 0)  << endl;
//        }
//        else
//        {
//            output << "Case #" << t << ": " << result/2 << " " << result/2  << endl;
//        }
//    }
//
//    input.close();
//    return 0;
//}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
