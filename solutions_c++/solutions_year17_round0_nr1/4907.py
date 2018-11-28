#include<bits/stdc++.h>
using namespace std;
#define sc scanint
#define f first
#define s second
#define pb push_back
#define mi 100000007
#define try int t;cin>>t; while(t--)
typedef long long llu;
typedef vector<int> vi;
int main()
{
    int tloop;
    int tcase;
    scanf("%d",&tloop);
    tcase=tloop;
    while(tloop--)
    {
        string chr;
        int fun=0,gun=0;
        int kun,cun=0,jun=0;
        cin>>chr;
        cin>>kun;
        int p = chr.size();
        for(int iv=0;iv<p;iv++)
        {
            if(chr[iv]=='-')
            {
            fun=1;
            break;
            }
        }

        if(fun==0)
            {cout<<"Case #";
            cout<<tcase-tloop;
            cout<<": ";
            cout<<0<<endl;}
        else
        {
            for(int i=0;i<p;i++)
            {
            if(chr[i]=='-')
                {
                cun++;
                for(int jun=i;jun<=(i+kun-1) && (i+kun-1)<p ;jun++)
                {
                    if(chr[jun]=='+')
                        chr[jun]='-';
                        else
            chr[jun]='+';
        }
                }
            }
            for(int x=0;x<p;x++)
            {
                if(chr[x]=='-')
                {
                    gun=1;
                break;
                }
            }
            if(gun!=1)
            {cout<<"Case #"<<tcase-tloop;
            cout<<": "<<cun<<endl;}
            else
            {cout<<"Case #"<<tcase-tloop;
            cout<<": "<<"IMPOSSIBLE\n";}
        }
    }
}
