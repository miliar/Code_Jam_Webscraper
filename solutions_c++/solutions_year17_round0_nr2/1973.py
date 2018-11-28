#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>

#include <fstream>
#include <sys/stat.h>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

#define FOR(i, a, b) for(int i=(a);i<(b);i++)
#define RFOR(i, b, a) for(int i=(b)-1;i>=(a);--i)
#define FILL(A,value) memset(A,value,sizeof(A))
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int, int> PII;



int main()
{
    freopen("in.txt", "r" , stdin);
    freopen("out.txt" , "w" , stdout);


    int t;
    cin >> t;
    FOR(tt,0,t)
    {
        printf("Case #%d: ", tt + 1);
        Int n;
        cin >> n;
        Int nn = n;
        VI a;
        int len = 0;
        while (nn)
        {
            ++ len;
            a.push_back(nn % 10);
            nn /= 10;
        }
        reverse(ALL(a));
        VI b;
        FOR(i,0,len)
        {
            int dig;
            RFOR(j,10,0)
            {
                VI bb = b;
                while (SZ(bb) < SZ(a))
                {
                    bb.push_back(j);
                }
                if (bb <= a)
                {
                    dig = j;
                    break;
                }
            }
            b.push_back(dig);
        }
        Int res = 0;
        FOR(i,0,SZ(b))
            res = 10 * res + b[i];

        cout << res << endl;
    }

    return 0;
}
