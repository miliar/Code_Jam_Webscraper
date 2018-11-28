#include <vector>
#include <string>
#include<fstream>
#include<math.h>
#include<string.h>
#include<stdio.h>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<set>
#include<climits>
#include<queue>
#include<sstream>
using namespace std;

int solve(string s)
{
    for(int i=1;i<s.length();i++)
    {
        if(s[i]<s[i-1])
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    //freopen("practice.in","r",stdin);
	freopen("B-large.in","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	long long T;
	//T =1;
	long long mod = 1000000007;
	scanf("%lld",&T);
	for(long long t=1;t<=T;t++)
    {
        printf("Case #%lld: ",t);
        long long n;
        scanf("%lld",&n);
        for(long long i=n;i>=1;)
        {
            //printf("%lld\n",i);
            std::ostringstream ss;
            ss << i;
            string s = ss.str();
            int index = solve(s);
            if(index==-1)
            {
                printf("%lld\n",i);
                break;
            }
            else
            {
                int val = s.length()-index;
                while(val--)
                {
                    i/=10;
                }
                i--;
                val = s.length()-index;
                while(val--)
                {
                    i = (i*10) + 9;
                }
            }
        }
    }
    return 0;
}
