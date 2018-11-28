#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
#define pi acos(-1)
#include<string.h>
#define rep(i,n) for(i=0;i<n;i++)
#define pb push_back
#include<stdio.h>
#include<stdlib.h>
using  namespace std;
typedef long long int lli;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<int> vi;
typedef vector<lli> vlli;
typedef vector<double> vd;
typedef map<int,int> mpii;
typedef map<string,int> mpsi;
#define mp make_pair
#define modu 1000000007
void fill_cake2(char* cake,int i,int j,int r,int c)
{
    ///south-east
    int col,row,check,flag,k;
    char ch=*(cake+i*c+j)+32;
    col=j+1;
    row=i+1;
    check=1;
    flag=1;
    while(check && col<c && row<r)
    {
        for(k=i;k<=row;k++)
            if(*(cake+k*c+col)!='?')  check=0;
        for(k=j;k<=col;k++)
            if(*(cake+row*c+k)!='?')  check=0;
        if(check==1)
        {
            for(k=i;k<=row;k++) *(cake+k*c+col)=ch;
            for(k=j;k<=col;k++) *(cake+row*c+k)=ch;
            flag=0;
        }
        row++;
        col++;
    }
    if(flag == 1)
    { /// south-west
        col=j-1;
    row=i+1;
    check=1;
    while(check && col>=0 && row<r)
    {
        for(k=i;k<=row;k++)
            if(*(cake+k*c+col)!='?')  check=0;
        for(k=j;k>=col;k--)
            if(*(cake+row*c+k)!='?')  check=0;
        if(check==1)
        {
            for(k=i;k<=row;k++) *(cake+k*c+col)=ch;
            for(k=j;k>=col;k--) *(cake+row*c+k)=ch;
            flag=0;
        }
        row++;
        col--;
    }
    }
    if(flag == 1)
    { /// north-west
        col=j-1;
    row=i-1;
    check=1;
    while(check && col>=0 && row>=0)
    {
        for(k=i;k>=row;k--)
            if(*(cake+k*c+col)!='?')  check=0;
        for(k=j;k>=col;k--)
            if(*(cake+row*c+k)!='?')  check=0;
        if(check==1)
        {
            for(k=i;k>=row;k--) *(cake+k*c+col)=ch;
            for(k=j;k>=col;k--) *(cake+row*c+k)=ch;
            flag=0;
        }
        row--;
        col--;
    }
    }
    if(flag == 1)
    { /// north-east
        col=j+1;
    row=i-1;
    check=1;
    while(check && col>=0 && row>=0)
    {
        for(k=i;k>=row;k--)
            if(*(cake+k*c+col)!='?')  check=0;
        for(k=j;k<=col;k++)
            if(*(cake+row*c+k)!='?')  check=0;
        if(check==1)
        {
            for(k=i;k>=row;k--) *(cake+k*c+col)=ch;
            for(k=j;k<=col;k++) *(cake+row*c+k)=ch;
            flag=0;
        }
        row--;
        col++;
    }
    }
}
void fill_cake(char* cake,int i,int j,int r,int c)
{
    int flag,k,kt,kd,allowed,col;
    char ch=*(cake+i*c+j)+32;
    ///up-down
    flag=0;
    kt=i-1;
    while(kt>=0 && *(cake + kt*c+j)=='?')
        {
            *(cake + kt*c+j)=ch;
            kt--;
            flag=1;
        }
    kt++;
    kd=i+1;
    while(kd<r && *(cake + kd*c+j)=='?')
        {
            *(cake + kd*c+j)=ch;
            kd++;
            flag=1;
        }
    kd--;
    if(flag==1)///sweep laterally
    {
        allowed=1;
        col=j+1;
        while(col<c && allowed)///right sweep
        {
            //for(col=j+1;col<c;col++)
            for(i=kt;i<=kd;i++)
                if(*(cake+i*c+col)!='?')allowed=0;
            if(allowed==1)
                for(i=kt;i<=kd;i++)
                    *(cake+i*c+col)=ch;
            col++;
        }
        allowed=1;
        col=j-1;
        while(col>=0 && allowed)///left sweep
        {
            //for(col=j+1;col<c;col++)
            for(i=kt;i<=kd;i++)
                if(*(cake+i*c+col)!='?')allowed=0;
            if(allowed==1)
                for(i=kt;i<=kd;i++)
                    *(cake+i*c+col)=ch;
            col--;
        }
    }
    /// ///
    if(flag==0)
    {
        ///left-right
        k=j-1;
        while(k>=0 && *(cake + i*c+k)=='?')
            {
                *(cake + i*c+k)=ch;
                k--;
                flag=1;
            }
        k=j+1;
        while(k<c && *(cake + i*c+k)=='?')
            {
                *(cake + i*c+k)=ch;
                k++;
                flag=1;
            }
    }
}
int main()
{
    freopen("inputa3.in","r",stdin);
    freopen("outputa.out","w",stdout);
    lli test,t,r,c,row,j,i,done;
    cin>>test;

    for(t=0;t<test;t++)
    {
        cin>>r>>c;
        char cake[r][c],cake2[r][c];
        string col;
        for(row=0;row<r;row++)
        {
            cin>>col;
            for(j=0;j<c;j++)
                {
                    cake[row][j]=col[j];
                    cake2[row][j]=col[j];
                }
        }

        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                if(cake[i][j]!='?' && cake[i][j]>=65 && cake[i][j]<=90)
                    fill_cake(&cake[0][0],i,j,r,c);
        done=1;
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
            if(cake[i][j]=='?')done=0;
        if(done==0)
        {
            for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                if(cake2[i][j]!='?' && cake2[i][j]>=65 && cake2[i][j]<=90)
                    fill_cake2(&cake2[0][0],i,j,r,c);
        }
        cout<<"Case #"<<t+1<<": "<<endl;
        if(done==1)
        {
                for(i=0;i<r;i++)
            {
                for(j=0;j<c;j++)
                    if(cake[i][j]>=97)
                        cout<<(char)(cake[i][j]-32);
                    else cout<<(char)(cake[i][j]);
                cout<<endl;
            }
        }
        else{
            for(i=0;i<r;i++)
            {
                for(j=0;j<c;j++)
                    if(cake2[i][j]>=97)
                        cout<<(char)(cake2[i][j]-32);
                    else cout<<(char)(cake2[i][j]);
                cout<<endl;
            }
        }
    }
}
