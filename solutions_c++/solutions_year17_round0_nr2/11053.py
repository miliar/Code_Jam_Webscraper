//
//  main.cpp
//  cpp_test
//
//  Created by Tianwei Liu on 2017-04-08.
//  Copyright © 2017 Tianwei Liu. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    int t, n;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> n;  // read n and then m.
        if (n>=10) {
            while (n >= 10){
                int num = n;
                int max = num%10;
                //cout <<max<<endl;
                if (max ==0){
                    n--;
                    continue;
                }
                
                num /= 10;
                int digit = num%10;
                int flag = 1;
                while (num > 0){
                    flag = 1;
                    if (digit > max){
                        flag = 0;
                        break;
                    }
                    max = digit;
                    num /= 10;
                    digit = num%10;
                }
                if (flag ==1){
                    break;
                } else {
                    n--;
                }
            }
        }
        cout << "Case #" << i << ": " << n << endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }

    return 0;
}
