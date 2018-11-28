// A C program to implement Ukkonen's Suffix Tree Construction
// Here we build generalized suffix tree for two strings
// And then we find longest common substring of the two input strings
#include <stdio.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
#define MAXN 105

ll t;

double n, d;
double eps = 1e-7;

int main()
{
    cin >> t;
    for (int cse = 1; cse <= t; cse++){
        cin >> d >> n;
        double cur = 1e14;
        for (int i = 0; i < n; i++){
            double k, s;
            cin >> k >> s;
            double dist = d - k;
            double time = dist/s;
            cur = min(cur, d/time);
        }
        printf("Case #%d: %0.07f\n", cse, cur);
    }
    return 0;
}

