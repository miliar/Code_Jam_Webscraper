/* 
 * File:   tidy_number.cpp
 * Author: hanv2
 *
 * Created on April 8, 2017, 1:53 PM
 */

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;
/*
 * 
 */
unsigned long long brute_force_tidy(const unsigned long long inp);
unsigned long long smart_tidy(const unsigned long long inp);
bool is_tidy(const unsigned long long inp);

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    for (int i = 1;i <= t;++i){
        unsigned long long inp;
        cin >> inp;
        //debug input
//        cout << "\ninput: "<<inp<<"\n";
        
        //solve
        unsigned long long result = smart_tidy(inp);
        
        //print result 
        cout << "Case #" << i << ": " <<  result << "\n";
        
        //double check by brute force
//        unsigned long long result1 = brute_force_tidy(inp);        
//        if (result == result1){
//            cout << "Check case #" << i << ":OK\n";
//        } else {
//            cout << "Check case #" << i << ":ERRRRR\n";
//            cout << "Case #" << i << ":" <<  result1 << "(brute force)\n";
//        }
    }
    return 0;
}

unsigned long long smart_tidy(const unsigned long long inp){
    unsigned long long num = inp;
    
    while (true) {
        unsigned long long num2 = num;
        
        int lastDigit = -1;
        int i = 0;        
        int firstOccur = i;
        while(num2 > 0){
            int digit = num2 % 10;
            num2 = num2 / 10;
            if (lastDigit >= 0 && digit > lastDigit){
                firstOccur = i;
            }
            lastDigit = digit;

            ++i;
        }
        
        unsigned long long splitter = (unsigned long long)pow(10.0,firstOccur);
        unsigned long long decrease = num % splitter;
        if (firstOccur > 0){
            num = num - decrease - 1;
        } else {
            //no more untidy pair of digits
            break;
        }        
    }
    return num;
}

unsigned long long brute_force_tidy(const unsigned long long inp){
    unsigned long long num = inp;
    while (num > 0){
        if (is_tidy(num)){
            break;
        }
        --num;
    }
    return num;
}

bool is_tidy(const unsigned long long inp){
    unsigned long long num = inp;
    int lastDigit = -1;
    while(num > 0){
        int digit = num % 10;
        num = num / 10;
        if (lastDigit >= 0 && digit > lastDigit){
            return false;
        }
        lastDigit = digit;
    }
    return true;
}

