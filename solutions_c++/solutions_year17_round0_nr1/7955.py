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

set<string> has;

int solve(string s,int k)
{
    int ans = 0;
    for(int i=0;i<=s.length()-k;i++)
    {
        if(s[i]=='-')
        {
            ans++;
            for(int j = i;j<i+k;j++)
            {
                if(s[j]=='-')
                {
                    s[j] = '+';
                }
                else
                {
                    s[j] = '-';
                }
            }
        }
    }
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='-')
        {
            return -1;
        }
    }
    return ans;
}

int main()
{
    //freopen("practice.in","r",stdin);
	freopen("A-large.in","r",stdin);
	//freopen("A-small-attempt2.in","r",stdin);
	freopen("output.out","w",stdout);
	long long T;
	//T =1;
	long long mod = 1000000007;
	scanf("%lld",&T);
	for(long long t=1;t<=T;t++)
    {
        has.clear();
        printf("Case #%lld: ",t);
        string s;
        int k;
        cin >> s >> k;
        int ans = solve(s,k);
        if(ans!=-1)
        {
            printf("%d\n",ans);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
