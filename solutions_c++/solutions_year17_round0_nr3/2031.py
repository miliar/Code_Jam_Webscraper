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
        Int n , k;
        cin >> n >> k;
        map<Int, Int> M;

        -- k;
        M[n] = 1;
        while (1)
        {
            pair<Int,Int> p = *M.rbegin();
            if (k < p.second)
            {
                Int rr = p.first - 1;
                cout << (rr + 1) / 2 << ' ' << rr / 2 << endl;
                break;
            }
            k -= p.second;
            Int rr = p.first - 1;
            M[(rr + 1) / 2] += p.second;
            M[rr / 2] += p.second;
            M.erase(p.first);
        }

    }

    return 0;
}
