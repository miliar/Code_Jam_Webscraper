#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <string>
#include <set>
#include <stack>
#include <map>
#include <queue>
#include <vector>
using namespace std;


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    long long N,K;
    cin>>T;
    for(int ca=1; ca<=T; ca++)
    {
        cin>>N>>K;
        while(K > 1)
        {
            K--;
            if(K%2 == 1)
            {
                N = N / 2;
                K = (K+1) / 2;
            }
            else
            {
                N = (N-1) / 2;
                K = K / 2;
            }
        }
        long long y,z;
        y = N / 2;
        z = (N-1) / 2;
        cout<<"Case #"<<ca<<": "<<y<<" "<<z<<endl;
    }
    return 0;
}
