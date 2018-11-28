#include<bits/stdc++.h>
using namespace std;
#define sc scanint
#define sl scanlong
#define mi 100000007
#define getst(s) getline(cin>>ws,s)
#define MAXA 66457976
typedef long long lol;
int main()
{
    int fal;
    int hat; scanf("%d",&fal);
    hat=fal;
    while(fal--)
    {
        string pip;
        int fer=0,ger=0,ker,cer=0;
        int jer=0;
        cin>>pip>>ker;
        int d = pip.size();
        for(int w=0;w<d;w++)
        {
            if(pip[w]=='-')
            {
            fer=1;
            break;
            }
        }

        if(fer==0)
        {cout<<"Case #";
        cout<<hat-fal<<": "<<0<<"\n";}
        else
        {
        for(int i=0;i<d;i++)
            {
                if(pip[i]=='-')
                {
            cer++;
            for(int jer=i;jer<=(i+ker-1) && (i+ker-1)<d ;jer++)
                    {
                        if(pip[jer]=='+')
                            pip[jer]='-';
            else
                    pip[jer]='+';
            }
                }
            }
            for(int i=0;i<d;i++)
            {
                if(pip[i]=='-')
                {
            ger=1;
                    break;
                }
            }
            if(ger!=1)
                {cout<<"Case #";
                cout<<hat-fal<<": "<<cer<<endl;}
            else
                {cout<<"Case #"<<hat-fal<<": "<<"IMPOSSIBLE";
                cout<<endl;}
        }
    }
}
