#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#define ll long long
#define ull unsigned long long
//#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define rep(i,n) for(int i = 0;i < n; i++)
#define fil(a,b) memset((a),(b),sizeof(a))
#define cl(a) fil(a,0)
#define pb push_back
#define mp make_pair
#define exp 2.7182818
#define PI 3.141592653589793
#define inf 0x3f3f3f3f
#define fi first
#define se second
#define eps 1e-7
#define mod 1000000007ll
using namespace std;

int dig[20];
int main()
{
    //freopen("B-small-attempt0","r",stdin);
    //freopen("output1.out","w",stdout);
    int n;
    cin>>n;
    
    for(int z=1;z<=n;++z)
    {
        cl(dig);
        string in;
        string res;
        cin>>in;
        int flag=1;
        int tmp;
        int sign;
        for(int i=0;i<in.size()-1;++i)
        {
            sign=i;
            if(in[i]>in[i+1])
            {
                tmp=i;
                flag=0;
                break;
            }
        }
        if(flag)
        {
            res=in;
        }
        else
        {
            if(sign==0)
            {
                if(in[sign]!='1')
                {
                    in[sign]--;
                    for(int i=1;i<in.size();++i) in[i]='9';
                    res=in;
                }
                else
                {
                    for(int i=1;i<=in.size()-1;++i) res.append("9");
                }
            }
            else
            {
                while(sign-1>=0&&in[sign]-in[sign-1]<1)
                {
                    sign--;
                }
                if(sign==0)
                {
                    if(in[sign]!='1')
                    {
                        in[sign]--;
                        for(int i=1;i<in.size();++i) in[i]='9';
                        res=in;
                    }
                    else
                    {
                        for(int i=1;i<=in.size()-1;++i) res.append("9");
                    }
                }
                else
                {
                    in[sign]--;
                    for(int i=sign+1;i<in.size();++i) in[i]='9';
                    res=in;
                }
            }
        }


        printf("Case #%d: ",z);
        cout<<res<<endl;
    }
    return 0;
}