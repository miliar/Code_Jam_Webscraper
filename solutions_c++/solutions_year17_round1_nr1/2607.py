#include <bits/stdc++.h>

using namespace std;
char a[30][30];
int chk[30];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;cin>>test;
    for(int ttt=1;ttt<=test;ttt++)
    {
        int row,col;cin>>row>>col;
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                cin>>a[i][j];
            }
        }
    for(int j=0;j<col;j++)
    {
        bool s=false;
        for(int i=0;i<row;i++)
        {
            if(a[i][j]!='?')s=true;
        }
        chk[j]=s;
    }
    for(int j=0;j<col;j++)
    {
        if(!chk[j]&&j==0)continue;
        if(chk[j])
        {
            for(int i=0;i<row;i++)
            {
                if(a[i][j]!='?')
                {
                    char temp=a[i][j];
                    for(int tt=0;tt<=i;tt++)
                    {
                        if(a[tt][j]=='?')
                        {
                            a[tt][j]=temp;
                        }
                    }
                }
            }
        }
        else
        {
            for(int i=0;i<row;i++)
            {
                a[i][j]=a[i][j-1];
            }
        }
    }
    if(!chk[0])
    {
        for(int i=0;i<row;i++)
        {
            a[i][0]=a[i][1];
        }
    }
    for(int j=0;j<col;j++)
    {
        for(int i=0;i<row;i++)
        {
            if(a[i][j]=='?')
            {
                for(int tt=i;tt<row;tt++)
                {
                    a[tt][j]=a[tt-1][j];
                }
            }
        }
    }
    for(int i=0;i<col;i++)
    {
        if(!chk[i])continue;
        if(chk[i])
        {
            for(int k=i-1;k>=0;k--)
            {
                if(chk[k])continue;
                for(int j=0;j<row;j++)
                {
                    a[j][k]=a[j][k+1];
                }
            }
        }
        break;
    }
    for(int i=col-1;i>=0;i--)
    {
        if(!chk[i])continue;
        if(chk[i])
        {
            for(int k=i+1;k<col;k++)
            {
                 if(chk[k])continue;
                for(int j=0;j<row;j++)
                {
                    a[j][k]=a[j][k-1];
                }
            }
        }
        break;
    }
    cout<<"Case"<<" #"<<ttt<<": "<<endl;
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            cout<<a[i][j];
        }
        cout<<endl;
    }
    }
    return 0;
}
/*
1
5 7
g ? ? ? ? c ?
? ? ? f ? ? n
? ? ? ? d ? ?
t ? ? ? ? ? ?
? m ? ? ? ? ?
*/
