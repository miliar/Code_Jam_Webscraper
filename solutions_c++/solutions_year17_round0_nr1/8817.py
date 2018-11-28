/*************************************************************************
	> File Name: a.cpp
	> Author: Anson
	> Mail: 354830997@qq.com
	> Created Time: Sat 08 Apr 2017 02:57:22 PM CST
 ************************************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#define LL long long
#define clr(x) memset(x,0,sizeof(x))
using namespace std;



int main() {
	ios::sync_with_stdio(false);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    cin>> t;
    for (int test = 0; test < t; test++) {
        int k;
        string s, str = "";
        cin>> s>> k;
        for (int i = 0; i < s.length(); i++) {
            if(s[i] == '-') {
                str += '1';
            } else {
                str += '0';
            }
        }
        queue<int> q;
        bool flag = false;
        int ans = 0;
        for (int i = 0 ; i < str.length(); i++) {
            if (!q.empty() && q.front() < i) {
                q.pop();
            }
            int sta = str[i] - '0' + q.size();
            if (sta & 1) {
                ans++;
                if (i + k -1 >= str.length()) {
                    flag = true;
                    break;
                }
                q.push(i + k -1);
            }
        }
        if (flag) {
            cout<< "Case #"<< test+1<< ": IMPOSSIBLE"<< endl;
        } else {
            cout<< "Case #"<< test+1<< ": "<< ans<< endl;
        }
    }
    return 0;
}
