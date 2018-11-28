#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{
    int Case;
    scanf("%d" ,&Case);

    long long int stall;
    long long int people;

    int n;
    long long int m; 
    long long int jump;

    long long int start;
    long long int tmp;
    long long int ans;

    char filename[]="C.txt";
    fstream fp;
    fp.open(filename, ios::out);

    for(int c=0 ;c<Case ;c++)
    {
        scanf("%lld%lld" ,&stall ,&people);

        n=0;
        tmp = people;
        while (tmp >>= 1) ++n;
        //n    = log( (double)(people+1) ) / log(2.0);
        
        // n=40;
        // jump = 1 << n;

        jump = 1;
        for(int i=0 ;i<n ;i++)
        {
            jump*=2;
        }

        m = people-jump;
        
        start = jump*2;
        start +=m;
        ans=0;
        //printf(" %lld %d %lld %lld\n" ,start ,n ,m ,jump);
        if( stall >= start )
        {
            ans = 1;
            ans += (stall-start) / jump;
        }
        //printf("Case #%d: %lld %lld\n" ,c+1 ,(ans+1)/2 ,ans/2);
        fp << "Case #" << c+1 << ": " << (ans+1)/2 << " " << ans/2 << "\n";
        
    }
fp.close();
return 0;
}