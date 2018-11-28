//
//  main.cpp
//  gg2-A
//
//  Created by Ran Wang on 4/22/17.
//  Copyright © 2017 Ran Wang. All rights reserved.
//

//
//  main.cpp
//  gg1-C
//
//  Created by Ran Wang on 4/14/17.
//  Copyright © 2017 Ran Wang. All rights reserved.
//

#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<(n);i++)
#define F1(i,n) for(int i=1;i<=(n);i++)
#define F2(i,a,b) for(int i=(a);i<=(b);i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }


int main() {
    int T;
    cin >> T;
    for(int caset = 1; caset <= T; caset++)
    {
        int K, D;
        cin >> K >> D;
        double hours = 0;
        while(D--)
        {
            double a, b;
            cin >> a >> b;
            hours = max(hours, (K - a) / b);
        }
        
        cout << "Case #" << caset << ": " << fixed << setprecision(6) << K / hours << endl;
    }
}

