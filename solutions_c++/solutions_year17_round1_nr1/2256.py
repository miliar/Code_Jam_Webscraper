#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("Ain.txt");
    fout.open("Aout.txt");
    int t,x=1;
    fin>>t;
    while(x<=t)
    {
        int r,c,i,j;
        fin>>r>>c;
        char a[r+1][c+1];
        int nos=0;
        string s;
        for(i=1;i<=r;i++)
        {
            fin>>s;//cout<<s<<endl;
            for(j=1;j<=c;j++)
            {
                a[i][j]=s[j-1];//cout<<a[i][j]<<endl;
                if(a[i][j]=='?')
                    ++nos;

            }
        }
        //cout<<"input done nos="<<nos<<endl;
        bool first=false,g=false;char ch='?';int k=0,m=0;
        for(j=1;j<=c;j++)
        {
            first=false;
            if(a[1][j]=='?')
                first=true;

            ch='?';
            for(i=1;i<=r;i++)
            {
                if(nos==0)
                {
                    g=true;break;
                }
                if(a[i][j]!='?')
                {
                    ch=a[i][j];
                    if(first==true)
                        {k=i;}
                }
                if(first==true && ch!='?')
                {
                    //cout<<"ei"<<ch;
                    for(m=k-1;m>=1;--m)
                    {a[m][j]=ch;--nos;}
                    first=false;
                }
                if(a[i][j]=='?' && first==false)
                {a[i][j]=ch;--nos;}
            }
            if(g==true)
                break;
        }
        //cout<<"after 1"<<nos<<endl;
        if(nos!=0)
        {
            //cout<<"here2"<<endl;
            for(i=1;i<=r;i++)
            {
                first=false;
                if(a[i][1]=='?')
                    first=true;

                 ch='?';
                for(j=1;j<=c;j++)
                {
                     if(nos==0)
                    {
                        g=true;break;
                    }
                    if(a[i][j]!='?')
                    {
                        ch=a[i][j];
                        if(first==true)
                            k=j;
                    }
                    if(first==true && ch!='?')
                    {
                        //cout<<"for"<<k-1<<"ch is "<<ch<<"i is "<<i<<endl;
                        for(m=k-1;m>=1;--m)
                        {a[i][m]=ch;--nos;}
                        first=false;
                    }
                    if(a[i][j]=='?' &&first==false)
                    {a[i][j]=ch;--nos;}
                }
            }
        }
        fout<<"Case #"<<x<<": "<<endl;++x;
        for(i=1;i<=r;i++)
        {
            for(j=1;j<=c;j++)
            {fout<<a[i][j];}
            fout<<endl;
        }
    }
    return 0;
}
