/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define ms(x,a) memset(x,a,sizeof(x))
#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout)

using namespace std;

string s;
int k;

void flip(int pos)
{
    for(int i=0;i<k;i++)
    {
        if(s[pos+i]=='+')
        {
           s[pos+i]='-';
        }
        else
        {
           s[pos+i]='+';
        }
    }
}

bool allOn()
{
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='-')
        {
            return false;
        }
    }
    return true;
}

int solve()
{
    int ans=0;
    for(int i=0;(i+k-1)<s.size();i++)
    {
        if(s[i]=='-')
        {
            flip(i);
            ans++;
        }
    }

    if(allOn())
    {
        return ans;
    }

    return -1;
}

int main()
{
    read("A-large.in");
    write("A-large.out");
    int t, check=1, ans;
    cin>>t;
    while(t--)
    {
        cin>>s>>k;
        ans=solve();
        if(ans!=-1)
        {
            printf("Case #%d: %d\n", check++, ans);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", check++);
        }
    }

	return 0;
}
