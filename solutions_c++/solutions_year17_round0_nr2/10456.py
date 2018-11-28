#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;

int main() {
    int t, i; cin>>t; ull j;
    for(i=1; i<=t; i++)
        {
        ull n; cin>>n;
        for(j=n; j>=0; j--)
            {
            ull num=j; int count=0; int last=num%10; num/=10;
            while(num!=0)
                {
               int temp=num%10;
                if(temp>last)
                {count=1; break;}
                last=temp;
                num/=10;
            }
            if(count==0)
                {printf("Case #%d: %llu\n", i, j); break;}
        }
    }
    return 0;
}
