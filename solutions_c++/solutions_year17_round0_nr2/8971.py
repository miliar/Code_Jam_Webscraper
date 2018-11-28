/*************************************************************************
	> File Name: b.cpp
	> Author: Anson
	> Mail: 354830997@qq.com
	> Created Time: Sat 08 Apr 2017 07:08:33 PM CST
 ************************************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#define LL long long
#define clr(x) memset(x,0,sizeof(x))
using namespace std;

string s;

int main() {
	ios::sync_with_stdio(false);
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int t = 0;
    cin>> t;
    for (int test = 1; test <= t; test++) {
        cin>> s;
        int len = s.length();
        int k = len;
        for (int i = len-1; i >= 0; i--) {
            if (s[i] < s[i-1]) {
                k = i-1;
            } else if (s[i] == s[i-1]) {
                if (k != len) {
                    k = i-1;
                }
            }
        }
        cout<< "Case #"<< test<< ": ";
        for (int i = 0; i < k; i++) {
            cout<< s[i];
        }
        if ((k != s.length() )&&(k != 0 || s[0]-49 != 0))
            cout<< s[k]-49;
        for (int i = k+1; i < len; i++) {
            cout<< 9;
        }
        cout<< endl;
    }
	return 0;
}
