#include<bits/stdc++.h>
using namespace std;
char ch[30][30];
int main()
{
     ifstream cin("alph.in");
    ofstream cout("alph.out");
    long long r,c,i,i2,j,k,T,TC;

    char cwal;
    cin>>T;
    TC=0;
    while(T--)
    {
        cout<<"Case #"<<++TC<<":\n";

    cin>>r>>c;
    for(i=0;i<r;++i)
    {
        for(i2=0;i2<c;++i2)
        {
            cin>>ch[i][i2];
        }
    }
    for(i=0;i<c;++i)
    {
        cwal='.';
        for(i2=0;i2<r;++i2)
        {
            if(ch[i2][i]=='?')
            {
                if(cwal!='.')
                {
                    ch[i2][i]=cwal;
                }
            }
            else cwal=ch[i2][i];
        }
        for(i2=r-1;i2>=0;--i2)
        {
            if(ch[i2][i]=='?')
            {
                if(cwal!='.')
                {
                    ch[i2][i]=cwal;
                }
            }
            else cwal=ch[i2][i];
        }
    }

    for(i=0;i<r;++i)
    {
        cwal='.';
        for(i2=0;i2<c;++i2)
        {
            if(ch[i][i2]=='?')
            {
                if(cwal!='.')
                {
                    ch[i][i2]=cwal;
                }
            }
            else cwal=ch[i][i2];
        }
        for(i2=c-1;i2>=0;--i2)
        {
            if(ch[i][i2]=='?')
            {
                if(cwal!='.')
                {
                    ch[i][i2]=cwal;
                }
            }
            else cwal=ch[i][i2];
        }
    }
    for(i=0;i<r;++i)
    {
        for(i2=0;i2<c;++i2)
        {
            cout<<ch[i][i2];
        }
        cout<<endl;
    }
    }
}
