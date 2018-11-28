#include<bits/stdc++.h>
using namespace std;
#define gc getchar
#define mp make_pair
#define f first
#define mi 1000000007
#define itr int t;cin>>t;while(t--)
#define sl scanlong
typedef vector<int> vi;
typedef unsigned long long int ull;


void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
int main()
{
    int lov,tru;
    scanf("%d",&tru);
    lov=tru;
    while(tru--)
    {
        string stru;
        int fw=0;
        int gw=0,kw,cw=0,jw=0;
        cin>>stru;
        cin>>kw;
        int r = stru.size();
        for(int i=0;i<r;i++)
        {
        if(stru[i]=='-')
            {
            fw=1;
            break;
        }
        }

        if(fw==0)
            {cout<<"Case #";
            cout<<lov-tru<<": "<<0<<endl;}
        else
        {
        for(int i=0;i<r;i++)
            {
                if(stru[i]=='-')
                {
                cw++;
        for(int jw=i;jw<=(i+kw-1) && (i+kw-1)<r ;jw++)
                    {
                if(stru[jw]=='+')
                            stru[jw]='-';
                else
            stru[jw]='+';
                    }
        }
            }
            for(int q=0;q<r;q++)
            {
                if(stru[q]=='-')
                {
                    gw=1;
            break;
                }
            }
            if(gw!=1)
                {cout<<"Case #"<<lov-tru;
            cout<<": "<<cw<<endl;}
            else
                {cout<<"Case #"<<lov-tru;
            cout<<": "<<"IMPOSSIBLE"<<endl;}
        }
    }
}
