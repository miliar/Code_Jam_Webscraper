//
//  main.cpp
//  flipper
//
//  Created by Pavan Kumar Sunkara on 08/04/17.
//  Copyright © 2017 Pavan Kumar Sunkara. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>

#include <string>
#include <algorithm>
#include <numeric>
#include <functional>
#include <utility>
#include <iomanip>

#include <list>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <bitset>

#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <climits>
#include <ctime>

using namespace std;

#define p(n)		printf("%d",n)
#define pl(n)		printf("%lld",n)
#define pf(n)		printf("%lf",n)
#define ps(n)		printf("%s",n)

#define pp(k,n)		printf("%0.klf",n)
#define pt			printf("\t")
#define pe			printf("\n")
#define pa          cout << " "

#define s(n)		scanf("%d",&n)
#define si(n)		int n; s(n);
#define sl(n)		scanf("%lld",&n)
#define sf(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)

#define ge			getchar()
#define gc(n)		n=getchar()
#define pc(n)		putchar(n)

#define inf			(int)1e9
#define linf		(long long)1e18
#define eps			1e-9
#define pi			3.14159265

#define fo(i,a,b)	for(int i=a;i<b;i++)
#define fn(i,n)		fo(i,0,n)
#define fe(v,c)		for(typeof((c).begin()) v = (c).begin(); v != (c).end(); ++v)

#define mp			make_pair
#define ft			first
#define sd			second
#define pb			push_back

#define sz(v)		((int)(v.size()))
#define st(s)		((int)(strlen(s)))

#define tr(a,b,c)	mp(a,mp(b,c))
#define fill(a,v)	memset(a,v,sizeof a)

#define unt(n)		int n; while (until(&n))
#define asl(n)		char n; while (aslong(&n))
#define cas(i,n)	si(n); fo(i,1,n+1)

#define mai(a,n)	int *a = new int[n];
#define mab(a,n)	bool *a = new bool[n];

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pii> tri;

typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;
typedef vector<tri> vt;

typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef vector<vt> vvt;

bool until(int *n) {
    s(*n); return (*n==0?false:true);
}

bool aslong(char *c) {
    gc(*c); return (*c==-1?false:true);
}

int gcd(int a, int b) {
    while(1) {
        a = a%b;
        if(a==0) return b;
        b = b%a;
        if(b==0) return a;
    }
}

/*Main code begins now */

void print(int i, int max, int min) {
    ps("Case #"); p(i); ps(": ");
    p(max); ps(" "); p(min); pe;
}

bool isPower2(int n) {
    return (n & (n - 1)) == 0;
}

int main(int argc, char **argv) {
    cas(i, t) {
        si(n); si(k);
        int max = 0, min = 0;

        int nExp = floor(log2(n));
        int closest = 1 << nExp;
        int closestSmall = closest >> 1;

        if ((n >= closestSmall + closest && k >= closest) || (k > n - closestSmall)) {
            print(i, 0, 0); continue;
        }

        int kExp = ceil(log2(k + 1));
        int po = exp2(kExp - 1);
        int poBig = po << 1;
        int diff = po & (n + poBig - k);

        max = n / poBig;

        if (k > 1 && n % poBig < po - 1 && k != po) {
            max--;
        }

        if (diff) {
            min = max - 1;
        } else {
            min = max;
        }

        print(i, max, min);
    }

    return 0;
}
