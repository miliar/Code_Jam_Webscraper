#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define gc getchar_unlocked
#define f(i,n) for(int i=0;i<n;i++)


int main()
{
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++)
    {
        int r,c;
        cin>>r>>c;
        char s[r+1][c+1];
        f(i,r)
        f(j,c)
        cin>>s[i][j];
        int flag=0;
        for(int kpl=0;kpl<10;kpl++)
        {
            int f=0,f1=0,f2=0,row;
            char cc;
            for(int i=0;i<r&&f==0&&f1==0&&f2==0;i++)
            {
                for(int j=0;j<c&&f==0&&f1==0&&f2==0;j++)
                {
                    if(s[i][j]=='?')
                    {
                        for(int k=i+1;k<r&&f==0;k++)
                        {
                            if(s[k][j]!='?')
                            {
                                cc=s[k][j];
                                row=k;
                                f=1;
                            }
                        }
                        for(int k=i-1;k>=0&&f==0;k--)
                        {
                            if(s[k][j]!='?')
                            {
                                cc=s[k][j];
                                row=k;
                                f=1;
                            }
                        }
                        
                        for(int k=row-1;k>=0&&f2==0&&f==1;k--)
                        {
                            if(s[k][j]=='?')
                            s[k][j]=cc;
                            else
                            f2=1;
                        }
                        for(int k=row+1;k<r&&f1==0&&f==1;k++)
                        {
                            if(s[k][j]=='?')
                            s[k][j]=cc;
                            else
                            f1=1;
                        }
                        
                    }
                }
            }
            /*f(i,r)
            {
                f(j,c)
                {
                    cout<<s[i][j];
                }
                cout<<endl;
                
            }
            cout<<"ssdss "<<endl;*/
        }
        f(kpl,625)
        {
                int fl=0,fl1=0,fl2=0,col,pp=0;
                char ccc;
                for(int i=0;i<r&&fl==0&&fl1==0&&fl2==0;i++)
                {
                    for(int j=0;j<c&&fl==0&&fl1==0&&fl2==0;j++)
                    {
                        if(s[i][j]=='?')
                        {
                            for(int k=j+1;k<c&&fl==0;k++)
                            {
                                if(s[i][k]!='?')
                                {
                                    ccc=s[i][k];
                                    col=k;
                                    fl=1;
                                }
                            }
                            for(int k=j-1;k>=0&&fl==0;k--)
                            {
                                if(s[i][k]!='?')
                                {
                                    ccc=s[i][k];
                                    col=k;
                                    fl=1;
                                }
                            }
                            for(int k=col+1;k<c&&fl1==0&&fl==1;k++)
                            {
                                if(s[i][k]=='?')
                                s[i][k]=ccc;
                                else
                                fl1=1;
                            }
                            for(int k=col-1;k>=0&&fl2==0&&fl==1;k--)
                            {
                                if(s[i][k]=='?')
                                s[i][k]=ccc;
                                else
                                fl2=1;
                            }
                        }
                        
                    }
                }
        }
        cout<<"Case #"<<ii+1<<":"<<endl;
        f(i,r)
        {
            f(j,c)
            {
                cout<<s[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}

