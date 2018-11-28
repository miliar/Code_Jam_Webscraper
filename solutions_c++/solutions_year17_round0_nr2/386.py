#include <bits/stdc++.h>
using namespace std;
vector<long long> blah;
long long eiei=0;
void gn(int x,long long pr,int lc)
{
    if(x==19)
        return;
    blah.push_back(pr);
    eiei=max(eiei,pr);
    for(int i=lc;i<=9;i++)
        gn(x+1,pr*10+i,i);
}
int main()
{
    freopen("Bi.in","r",stdin);
    freopen("B.out","w",stdout);
    gn(0,0,0);
    sort(blah.begin(),blah.end());
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        long long n;
        cin>>n;
        long long an=0;
        int b=0,e=blah.size()-1,md,re=0;
        while(b<=e)
        {
            md=(b+e)/2;
            if(blah[md]<=n)
            {
                re=max(re,md);
                b=md+1;
            }
            else
                e=md-1;
        }
        printf("Case #%d: ",tt);
        cout<<blah[re]<<endl;
    }
}
