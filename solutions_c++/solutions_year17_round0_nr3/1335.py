#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

long long calc(long long N, long long K) {
    long long cntLow = 0, cntHigh = 1, low = -1, high = N, assigned = 0;

    while (true) {
        assigned += cntHigh;
        if (assigned>=K || high==1) {
            return high;
        }
        assigned += cntLow;
        if (assigned >= K) {
            return low;
        }

        long long tempLowCnt = 0, tempHighCnt = 0;
        if (low != -1 && low != 1) {
            if (low&1) {
                tempLowCnt += cntLow<<1;
            }
            else {
                tempLowCnt += cntLow;
                tempHighCnt += cntLow;
            }
            low = (low-1)>>1;
        }
        if (high&1) {
            high >>= 1;
            tempHighCnt += cntHigh<<1;
        }
        else {
            low = (high-1)>>1;
            high >>= 1;
            tempLowCnt += cntHigh;
            tempHighCnt += cntHigh;
        }
        cntLow = tempLowCnt;
        cntHigh = tempHighCnt;
    }
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int T = INPT_INT;
    for (int _case = 1; _case <= T; ++_case) {
        long long N, K;
        cin>>N>>K;

        long long res = calc(N,K);
        printf("Case #%d: %lld %lld\n",_case,res>>1,(res-1)>>1);
    }
    return 0;
}
