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
int n;

int maxVal(int a,int b,int c)
{
    if(a>=b&&a>=c)
        return a;
    if(b>=a&&b>=c)
        return b;
    return c;
}

string solve(char start,int index,string ans,int R,int O,int Y,int G,int B,int V)
{
    //printf("%s\n",ans.c_str());
    if(index==n-1)
    {
        if((start=='R'&&(ans[0]=='R'||ans[0]=='O'||ans[0]=='V'))||(start=='O'&&ans[0]!='B')||(start=='V'&&ans[0]!='Y'))
            return "IMPOSSIBLE";
        if((start=='Y'&&(ans[0]=='Y'||ans[0]=='O'||ans[0]=='G'))||(start=='O'&&ans[0]!='B')||(start=='G'&&ans[0]!='R'))
            return "IMPOSSIBLE";
        if((start=='B'&&(ans[0]=='B'||ans[0]=='V'||ans[0]=='G'))||(start=='V'&&ans[0]=='Y')||(start=='G'&&ans[0]!='R'))
            return "IMPOSSIBLE";
        return ans+start;
    }
    if(start=='R')
    {
        string val = "IMPOSSIBLE";
        if(Y!=0 && Y==maxVal(Y, G, B))
            return solve('Y',index+1,ans+'R',R, O, Y-1, G, B, V);
        if(val=="IMPOSSIBLE"&&G!=0 && G==maxVal(Y, G, B))
            return solve('G',index+1,ans+'R',R, O, Y, G-1, B, V);
        if(val=="IMPOSSIBLE"&&B!=0 && B==maxVal(Y, G, B))
            return solve('B',index+1,ans+'R',R, O, Y, G, B-1, V);
        return val;
    }
    if(start=='Y')
    {
        string val = "IMPOSSIBLE";
        if(val=="IMPOSSIBLE"&&B!=0 && B==maxVal(R,B, V))
            return solve('B',index+1,ans+'Y',R, O, Y, G, B-1, V);
        if(val=="IMPOSSIBLE"&&V!=0 && V==maxVal(R, B, V))
            return solve('V',index+1,ans+'Y',R, O, Y, G, B, V-1);
        if(val=="IMPOSSIBLE"&&R!=0 && R==maxVal(R,B, V))
            return solve('R',index+1,ans+'Y',R-1, O, Y, G, B, V);
        return val;
    }
    if(start=='B')
    {
        string val = "IMPOSSIBLE";
        if(val=="IMPOSSIBLE"&&R!=0 && R==maxVal(R, O, Y))
            return solve('R',index+1,ans+'B',R-1, O, Y, G, B, V);
        if(val=="IMPOSSIBLE"&&O!=0 && O==maxVal(R, O, Y))
            return solve('O',index+1,ans+'B',R, O-1, Y, G, B, V);
        if(val=="IMPOSSIBLE"&&Y!=0 && Y==maxVal(R, O, Y))
            return solve('Y',index+1,ans+'B',R, O, Y-1, G, B, V);
        return val;
    }
    if(start=='O')
    {
        if(B!=0)
            return solve('B',index+1,ans+'O',R, O, Y, G, B-1, V);
        return "IMPOSSIBLE";
    }
    if(start=='G')
    {
        if(R!=0)
            return solve('R',index+1,ans+'G',R-1, O, Y, G, B, V);
        return "IMPOSSIBLE";
    }
    if(start=='V')
    {
        if(Y!=0)
            return solve('Y',index+1,ans+'V',R, O, Y-1, G, B, V);
        return "IMPOSSIBLE";
    }
    return "IMPOSSIBLE";
}

int main()
{
    //freopen("practice.in","r",stdin);
	//freopen("B-large.in","r",stdin);
	freopen("B-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	long long T;
	//T =1;
	long long mod = 1000000007;
	scanf("%lld",&T);
	for(long long t=1;t<=T;t++)
    {
        printf("Case #%lld: ",t);
        int R, O, Y, G, B, V;
        int r,o,y,g,b,v;
        scanf("%d %d %d %d %d %d %d",&n,&R,&O,&Y,&G,&B,&V);
        string ans = "IMPOSSIBLE";
        if(ans=="IMPOSSIBLE"&&R!=0)
        {
            ans = solve('R',0,"",R-1, O, Y, G, B, V);
        }
        if(ans=="IMPOSSIBLE"&&O!=0)
        {
            ans = solve('O',0,"",R, O-1, Y, G, B, V);
        }
        if(ans=="IMPOSSIBLE"&&Y!=0)
        {
            ans = solve('Y',0,"",R, O, Y-1, G, B, V);
        }
        if(ans=="IMPOSSIBLE"&&G!=0)
        {
            ans = solve('G',0,"",R, O, Y, G-1, B, V);
        }
        if(ans=="IMPOSSIBLE"&&B!=0)
        {
            ans = solve('B',0,"",R, O, Y, G, B-1, V);
        }
        if(ans=="IMPOSSIBLE"&&V!=0)
        {
            ans = solve('V',0,"",R, O, Y, G, B, V-1);
        }
        printf("%s\n",ans.c_str());
    }
    return 0;
}
