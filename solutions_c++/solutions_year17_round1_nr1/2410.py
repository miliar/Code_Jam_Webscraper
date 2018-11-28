#include<bits/stdc++.h>
using namespace std;
int main()
{
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
int r,c,t,tc=0,i,j,k,n,f;
    string s[50];
    char ch;
    cin>>t;
    while(t--)
    {
        cin>>r>>c;
        for(i=0;i<r;i++)
        {
            cin>>s[i];
        }
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(s[i][j]>='A' && s[i][j]<='Z')
                {
                    n=i-1;
                    for(k=n;k>=0;k--)
                    {
                        if(s[k][j]=='?') s[k][j]=s[i][j];
                        else break;
                    }
                    n=i+1;
                    for(k=n;k<r;k++)
                    {
                        if(s[k][j]=='?') s[k][j]=s[i][j];
                        else break;
                    }
                }
            }
        }
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(s[i][j]=='?')
                {
                    f=0;
//                    n=j;
//                    for(k=0;k<n;k++)
//                    {
//                        if(s[i][k]>='A' && s[i][k]<='Z') ch=s[i][k];
//                    }
//                    for(k=j;k>=0;k++)
//                    {
//                        if(s[i][k]=='?') s[i][k]=ch;
//                    }
//
//
//                    for(k=n;k>=0;k--)
//                    {
//                        if(s[i][k]>='A' && s[i][k]<='Z') {s[i][j]=s[i][k];f=1;break;}
//                    }
                    if(j==0) f=0;

                    else if (s[i][j-1]>='A' && s[i][j-1]<='Z') {s[i][j]=s[i][j-1];f=1;}


                    if(f==1) continue;
                        n=j+1;
                    for(k=c-1;k>=n;k--)
                    {
                        if(s[i][k]>='A' && s[i][k]<='Z') ch=s[i][k];
                    }
                    for(k=j;k<c;k++)
                    {
                        if(s[i][k]=='?') s[i][k]=ch;
                        else break;
                    }
                }
            }
        }
        printf("Case #%d:\n",++tc);
        for(i=0;i<r;i++) {cout<<s[i]<<endl;s[i]="";}
    }
    return 0;
}
