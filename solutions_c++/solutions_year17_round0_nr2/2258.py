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
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    long long N;
    long long D[19],W[19];
    W[0] = 1;
    for(int i=1; i<19; i++)
    {
        W[i] = W[i-1] * 10;
    }

    cin>>T;

    for(int ca=1; ca<=T; ca++)
    {
        cin>>N;
        memset(D,0,sizeof(D));
        int j=0;
        while(N > 0)
        {
            D[j] = N % 10;
            N = N / 10;
            j++;
        }

        for(int i=17; i>=0; i--)
        {
            if(D[i] >= D[i+1]) continue;
            for(int j=i; j>=0; j--)
            {
                D[j] = 9;
            }
            D[i+1]--;
            for(int j=i+1; j<18; j++)
            {
                if(D[j] >= D[j+1]) break;
                D[j] = 9;
                D[j+1]--;
            }
        }

        N = 0;
        for(int i=0; i<19; i++)
        {
            N += (D[i] * W[i]);
        }
        cout<<"Case #"<<ca<<": "<<N<<endl;
    }
    return 0;
}
