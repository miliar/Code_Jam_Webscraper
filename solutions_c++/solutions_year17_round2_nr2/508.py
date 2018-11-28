//
//  main.cpp
//  gg2-B
//
//  Created by Ran Wang on 4/22/17.
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

struct Color {
    Color (char a, int b) : c{a}, n{b} {}
    
    char c;
    int n;
};

int main() {
    int T;
    cin >> T;
    for(int caset = 1; caset <= T; caset++)
    {
        string res;
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        
        int m = max(R, max(Y, B));
        
        if(m * 2 > N)res = "IMPOSSIBLE";
        else
        {
            vector<Color> all;
            all.push_back(Color('R', R));
            all.push_back(Color('O', O));
            all.push_back(Color('Y', Y));
            all.push_back(Color('G', G));
            all.push_back(Color('B', B));
            all.push_back(Color('V', V));
            
            sort(all.begin(), all.end(), [](const Color& a, const Color& b){
                return a.n > b.n;});
            
            while(res.size() < N)
            {
                if(all[0].n == all[2].n)
                {
                    res += all[0].c;
                    res += all[1].c;
                    res += all[2].c;
                    all[0].n--;
                    all[1].n--;
                    all[2].n--;
                }
                else
                {
                    res += all[0].c;
                    res += all[1].c;
                    all[0].n--;
                    all[1].n--;
                    if(all[1].n < all[2].n)swap(all[1], all[2]);
                }
            }
        }
        cout << "Case #" << caset << ": " << res << endl;
    }
}
