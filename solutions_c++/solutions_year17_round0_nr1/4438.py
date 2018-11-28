#include <iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cstring>
#include<set>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<utility>
#include<map>
#include<functional>
#define rep(i,l,r) for(int i=l;i<r;i++)
#define down(i,l,r) for(int i=l;i>r;i--)
#define pb(x) push_back(x)
#define mp(a,b) make_pair(a,b)
#define ll long long
#define pii pair<int,int>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    fstream ci,co;
    ci.open("A-large.in",ios::in|ios::binary);
    co.open("aout.txt",ios::out);
    int q;
    ci>>q;
    rep(t,1,q+1)
    {
        string s;
        int k;
        ci>>s>>k;
        int ans=0;
        int slen=s.length();
        rep(i,0,slen)
        {
            if(s[i]=='-')
            {
                ++ans;
                if((i+k-1)<slen)
                {
                    rep(j,i+1,i+k)
                    {
                        if(s[j]=='-')
                        {
                            s[j]='+';
                        }
                        else
                        {
                            s[j]='-';
                        }
                    }
                }
                else
                {
                    ans=-1;
                    break;
                }
            }
        }
        if(ans==-1)
        {
            co<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            co<<"Case #"<<t<<": "<<ans<<endl;
        }
    }

}
