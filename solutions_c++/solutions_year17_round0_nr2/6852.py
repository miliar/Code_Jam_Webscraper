#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <bitset>
#include <cmath>
#include <numeric>
#include <iterator>
#include <iostream>
#include <cstdlib>
#include <functional>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <complex>
using namespace std;

typedef long long LL;

int T;
char s[20];
int q[20];

void solve(int cases) {
    scanf("%s",s);
    int len = strlen(s);
    for(int i = 0 ; i < len ; i++ ) q[i] = s[i] - '0';
    for(int i = len - 1; i >= 1 ; i--) {
        if(q[i] < q[i-1]) {
            for(int j = i ; j < len ; j++ ) {
                q[j] = 9;
            }
            q[i-1] -- ;
        }
    }
    int idx = 0;
    while(idx<len && q[idx] == 0) idx++;
    if( idx == len) {
        printf("Case #%d: 0\n",cases);
    } else {
        printf("Case #%d: ", cases);
        while(idx < len) {
            printf("%d",q[idx]);
            idx++;
        }
        printf("\n");
    }
}

int main() {
    scanf("%d",&T);
    for(int i = 1 ; i <= T ; i++) solve(i);
    return 0;
}
