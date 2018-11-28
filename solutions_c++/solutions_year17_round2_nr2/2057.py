#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in", "r" , stdin);
    freopen("output.out", "w", stdout);
    int caseno=0,t;
    cin>>t;
    while(caseno++<t)
    {
        char si[1005];
        int len=0;
        int n,r,o,y,g,b,v;
        char f,s,t,fl,sl,tl;
        int first=-1,last=-1;
        int ff,sf,tf,flf,slf,tlf;
        cin>>n>>r>>o>>y>>g>>b>>v;
        cout<<"Case #"<<caseno<<": ";
        int r1=r-g;
        int y1=y-v;
        int b1=b-o;
        if(r1>=y1&&r1>=b1)
        {
            f='R';
            ff=r;
            fl='G';
            flf=g;
            if(b>=y)
            {
                s='B';sl='O';t='Y';tl='V';
                sf=b;slf=o;tf=y;tlf=v;
            }
            else
            {
                s='Y';sl='V';t='B';tl='O';
                sf=y;slf=v;tf=b;tlf=o;
            }
        }
        else if(y1>=r1&&y1>=b1)
        {
            f='Y';
            ff=y;
            fl='V';
            flf=v;
            if(b>=r)
            {
                s='B';sl='O';t='R';tl='G';
                sf=b;slf=o;tf=r;tlf=g;
            }
            else
            {
                s='R';sl='G';t='B';tl='O';
                sf=r;slf=g;tf=b;tlf=o;
            }
        }
        else
        {
            f='B';
            ff=b;
            fl='O';
            flf=o;
            if(r>=y)
            {
                s='R';sl='G';t='Y';tl='V';
                sf=r;slf=g;tf=y;tlf=v;
            }
            else
            {
                s='Y';sl='V';t='R';tl='G';
                sf=y;slf=v;tf=r;tlf=g;
            }
        }
        if(b<o||r<g||y<v)
        {
            cout<<"IMPOSSIBLE\n";continue;
        }
        else
        {
            if(b==o&&r+g+v+y>0&&b>o)
                {cout<<"IMPOSSIBLE\n";continue;}
            else if(r==g&&b+o+v+y>0&&r>g)
                {cout<<"IMPOSSIBLE\n";continue;}
            else if(y==v&&r+g+b+o>0&&y>v)
                {cout<<"IMPOSSIBLE\n";continue;}
            else
            {
                if((ff-flf)>0&&(sf==0||(sf-slf<=1&&tf==0&&n>2)))
                {
                    cout<<"IMPOSSIBLE\n";
                    continue;
                }
                if(tlf>0)
                {
                    si[len++]=t;
                    //cout<<t;
                    tf--;
                }
                while(tlf>0)
                {
                    si[len++]=tl;
                    si[len++]=t;
                    //cout<<tl<<t;
                    tf--;
                    tlf--;
                }
                if(flf>0)
                {
                    si[len++]=f;
                    //cout<<f;
                    ff--;
                }
                while(flf>0)
                {
                    si[len++]=fl;
                    si[len++]=f;
                    //cout<<fl<<f;
                    ff--;
                    flf--;
                }
                /*if(slf==0)
                {
                    if()
                    cout<<t;
                }*/
                if(slf>0)
                {
                    si[len++]=s;
                    //cout<<s;
                    sf--;
                }
                while(slf>0)
                {
                    si[len++]=sl;
                    si[len++]=s;
                    //cout<<sl<<s;
                    sf--;
                    slf--;
                }
                while(ff>0)
                {
                    si[len++]=f;
                    //cout<<f;
                    if(tf>0)
                    {
                        si[len++]=t;
                        //cout<<t;
                        tf--;
                    }
                    if(ff==sf)
                    {
                        si[len++]=s;
                        //cout<<s;
                        sf--;
                    }
                    ff--;
                }
                int flag=0;
                for(int i=1;i<len;i++)
                    if(si[i]==si[i-1])
                    {
                        flag=1;
                        cout<<"IMPOSSIBLE\n";
                        break;
                    }
                if(si[0]==si[len-1]&&n>1)
                {
                    cout<<"IMPOSSIBLE\n";
                    continue;
                }
                if(flag==0)
                {
                    for(int i=0;i<len;i++)
                    cout<<si[i];
                    cout<<"\n";
                }
            }
        }
    }
    return 0;
}
