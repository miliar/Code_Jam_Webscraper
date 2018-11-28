#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;

lli power(int x,int y)
{
    if(y==0)
        return 1LL;

    if(y&1)
        return x*power(x,y-1);
    lli ans= power(x,y/2);
    return ans*ans;
}


int len;
lli solve(string r,int pos, bool isequal)
{
    if(pos==len)
        return 0;

    lli ans=0;

    if(!isequal)
        return power(10,len-pos)-1;
    else
    {
        if(pos>0)
        {
            if(r[pos]>=r[pos-1])
            {
                lli ifequal= solve(r,pos+1,1) + power(10,len-pos-1)*(r[pos]-'0');
                lli notequal=-1e18;
                if(r[pos]>r[pos-1])
                    notequal= solve(r,pos+1,0) + power(10,len-pos-1)*(r[pos]-'0'-1);
                return max(ifequal,notequal);
            }
            else
                return -1e18;
        }
        else
        {
            lli ifequal= solve(r,pos+1,1) + power(10,len-pos-1)*(r[pos]-'0');
            lli notequal= solve(r,pos+1,0) + power(10,len-pos-1)*(r[pos]-'0'-1);
            return max(ifequal,notequal);
        }
    }
}

int t,cas;
lli n,ans;
string r;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        cas++;
        scanf("%lld",&n);
        r = to_string(n);
        len= r.length();
        ans = solve(r,0,1);

        printf("Case #%d %lld\n: ",cas,ans);
    }

    return 0;
}
