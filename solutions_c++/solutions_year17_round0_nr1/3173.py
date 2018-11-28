#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;
typedef long long llint;

const int N = (int)1e3 + 10;

char s[N];

int main() {
    int t;
    scanf("%d", &t);
    for (int case_ = 1; case_ <= t; case_++) {
        int k, cnt = 0;
        scanf("%s%d", s, &k);
        int len = (int)strlen(s);
        for (int i = 0; i < len; i++) {
            if (s[i] == '-' && i+k-1 < len) {
                for (int j = i; j < i+k; j++)
                    s[j] = (s[j]=='+'? '-' : '+');
                cnt++;
            }
        }
        bool flag = true;
        for (int i = 0; i < len; i++) {
            if (s[i] == '-') {
                flag = false;
                break;
            }
        }
        if (flag)
            printf("Case #%d: %d\n", case_, cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n", case_);
    }
}

//freopen("/Users/Clair/Desktop/in.txt", "r", stdin);
//    freopen("/Users/Clair/Desktop/in.txt", "w", stdout);
//    cout << 100 << endl;
//    for (int j = 0; j < 100; j++) {
//        for (int i = 0; i < 1000; i++)
//            cout << (i % 2==0? '+' : '-');
//        cout << " " << 999 << endl;
//    }
