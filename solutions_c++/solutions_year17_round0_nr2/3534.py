#include <cstdio>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#define MAX_N 1005
#define ll __int64

using namespace std;

bool check(ll x) {
    int pre = x % 10;
    x /= 10;
    while (x != 0) {
        if (pre < x % 10) {
            return false;
        } else {
            pre = x % 10;
            x /= 10;
        }
    }
    return true;
}


void test(int i, string s) {


        ll x = 0;
        for (int i = 0; i < s.size(); i++) {
            x = x * 10 + s[i]-'0';
        }
        while (check(x) == false) {
            x--;
        }
        cout << "Case #" << i << ": " << x  << endl;
        //cout << x << endl;
}


int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
  //  freopen("B-small-attempt4.in", "r", stdin);
    freopen("out.txt", "w+", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i<= T; i++) {
       // ll x;
       // scanf("%I64d", &x);
        string s;
        cin >> s;
     //   test(i, s);

        reverse(s.begin(), s.end());
        string ans;
        int flag0 = 0;
        char pre = s[0];
        for (int i = 0; i < s.size(); i++) {
            if (s[i] > pre) {
                s[i] = s[i] - 1;
                for (int j = 0; j < i; j++) {
                    s[j] = '9';
                }
            }
            pre = s[i];

        }
        reverse(s.begin(), s.end());
        while (s[0] == '0') {
            s.erase(s.begin());
        }
        cout << "Case #" << i << ": " << s << endl;

    }
    return 0;
}
