#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

const int N = 1e3 + 5;

int n, R, O, Y, G, B, V;
char str[N];
map<char, int> val;


int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        
        scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);
        
        printf("Case #%d: ", Case);
        
        
        val['R'] = R, val['Y'] = Y, val['B'] = B;
        int sum = R + Y + B, mx = max(R, max(Y, B));
        
        if(sum - mx < mx) {puts("IMPOSSIBLE"); continue;}
        else
        {
            int now = 0;
            char ch, ch1, ch2;
            if(R == mx) ch = 'R', ch1 = 'Y', ch2 = 'B';
            else if(B == mx) ch = 'B', ch1 = 'R', ch2 = 'Y';
            else if(Y == mx) ch = 'Y', ch1 = 'R', ch2 = 'B';
            
            int k1 = val[ch1];
            int k2 = val[ch] - k1;
            int k3 = val[ch2] - k2;
            k1 -= k3;
            for(int i = 1; i <= k3; ++i)
                str[now++] = ch, str[now++] = ch1, str[now++] = ch2;
            for(int i = k3 + 1; i <= k3 + k1; ++i)
                str[now++] = ch, str[now++] = ch1;
            for(int i = k3 + k1 + 1; i <= val[ch]; ++i)
                str[now++] = ch, str[now++] = ch2;
            str[now] = 0;
            puts(str);
        }
        
    }
    
    return 0;
}
