//
//  main.cpp
//  Tidy Numbers
//
//  Created by 王越 on 17/4/8.
//  Copyright © 2017年 王越. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

#define SIZE 20

int main(int argc, const char * argv[]) {
    ofstream cout("/Users/xidui/Documents/xidui/practices/gcj/Tidy Numbers/Tidy Numbers/output2.txt");
    ifstream cin("/Users/xidui/Documents/xidui/practices/gcj/Tidy Numbers/Tidy Numbers/B-large.in");
    
    int T, t = 0;
    cin >> T;
    while (t++ != T){
        long long n;
        cin >> n;
        int digit[SIZE];
        memset(digit, 0, sizeof(digit));
        int ptr = SIZE;
        while (n != 0) {
            digit[--ptr] = n % 10;
            n /= 10;
        }
        int p1 = 0, p2 = 1;
        long long ans = 0;
        while (p1 != SIZE) {
            ans *= 10;
            if (p2 == SIZE) {
                ans += digit[p1];
                break;
            }
            if (digit[p2] > digit[p1]) {
                ans += digit[p1];
                p1++;
                p2 = p1 + 1;
                continue;
            } else if (digit[p2] < digit[p1]) {
                ans += digit[p1] - 1;
                while (++p1 != SIZE) {
                    ans = ans * 10 + 9;
                }
            } else {
                long long tmp = ans;
                tmp += digit[p1];
                while (p2 + 1 != SIZE && digit[p2 + 1] == digit[p2]) {
                    tmp *= 10;
                    tmp += digit[p2];
                    p2++;
                }
                if (p2 == SIZE) {
                    p1 = SIZE;
                    ans = tmp * 10 + digit[p2 - 1];
                } else if (digit[p2 + 1] > digit[p2]) {
                    ans = tmp * 10 + digit[p2];
                    p1 = p2 + 1;
                    p2 = p1 + 1;
                } else {
                    ans += digit[p1] - 1;
                    while (++p1 != SIZE) {
                        ans = ans * 10 + 9;
                    }
                }
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
