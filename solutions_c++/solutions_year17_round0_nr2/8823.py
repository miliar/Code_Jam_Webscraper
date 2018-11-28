//
//  Tidy Numbers
//  Created by McKrisch on 09.04.15
//

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <set>
#include <vector>
#include <iostream>
#include <list>
#include <map>
#include <assert.h>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep1(i,m) for(int i=1;i<=(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define ForRev(it,c) for(__typeof(c.rbegin()) it=c.rbegin();it!=c.rend();++it)

typedef unsigned long long ll;

//#define TEST
//#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "B-test.in";
#else
#ifdef SMALL
const char *kIn  = "B-small.in";
const char *kOut = "B-small.out";
#else
const char *kIn  = "B-large.in";
const char *kOut = "B-large.out";
#endif
#endif

ll readInt() {
    ll num, c;
    while ((c = getchar_unlocked()) < '-');
    num = c - '0';
    while ((c = getchar_unlocked()) >= '0') {
        num = (num<<3) + (num<<1) + (c-'0');
    }
    return num;
}

bool check(ll v) {
    while (v) {
        int a = v%10;
        int b = (v/10)%10;
        if (b > a) return false;
        v /= 10;
    }
    return true;
}

ll calc(ll v) {
    ll orgV = v;
    int c = 0;
    while (v) {
        int a = v%10;
        int b = (v/10)%10;
        if (b > a) c++;
        v /= 10;
    }
    v = orgV;
    if (c > 0) {
        ll pow10 = 1;
        while (c) {
            int a = v%10;
            int b = (v/10)%10;
            if (b > a) c--;
            v /= 10;
            pow10 *= 10;
        }
        v = v * pow10 - 1;
    }
    return v;
}

void workCase() {
    ll v = readInt();
    while (true) {
        ll tmp = calc(v);
        if (tmp == v) break;
        v = tmp;
    }
    printf("%lld\n", v);
}

int main(int argc, const char * argv[]) {
    if (!freopen(kIn, "rt", stdin)) {
        return 1;
    }
#if !defined(COUT) && !defined(TEST)
    if (!freopen(kOut, "wt", stdout)) {
        return 2;
    }
#endif
    int T = (int)readInt();
    rep (i, T) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
