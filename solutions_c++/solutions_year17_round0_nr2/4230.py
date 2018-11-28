#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <vector>
#include <bits/stdc++.h>
#include <time.h>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <bitset>
#include <algorithm>
using namespace std;
#define MP make_pair
#define PB push_back
#define mst(a,b) memset((a),(b),sizeof(a))
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int, int> Pii;
typedef vector<int> Vi;
typedef vector<Pii> Vii;
const int inf = 0x3f3f3f3f;
const LL INF = (1uLL << 63) - 1;
const LL mod = 1000000007;
const int N = 1e5 + 7;
const double Pi = acos(-1.0);
const int maxn = 1e4 + 5;
const uLL Hashmod = 29050993;
char s[111];
int judge(int len) {
    for(int i = 0; i < len - 1; i++) {
        if(s[i] > s[i + 1])return i;
    }
    return -1;
}
int main() {
#ifdef local
    freopen("B-large.in", "r", stdin);
    freopen("w", "w", stdout);
#endif
    // ios::sync_with_stdio(0);
    // cin.tie();
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        printf("Case #%d: ", cas);
        scanf("%s", s);
        int len = strlen(s);
        int pos = judge(len);
        if(pos == -1) {
            printf("%s\n", s);
        } else {
            for(int j = pos + 1; j < len; j++)s[j] = '9';
            if(s[pos] == '1') {
                for(int j = 1; j <= pos; j++)s[j] = '9';
                printf("%s\n", s + 1);
            } else {
                int st = 0;
                for(int j = pos; j >= 1; j--) {
                    if(s[j - 1] < s[j]) {
                        st = j;
                        break;
                    }
                }
                s[st]--;
                for(int j = st + 1; j <= pos; j++) {
                    s[j] = '9';
                }
                printf("%s\n", s);
            }
        }
    }
}
