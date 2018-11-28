#include<bits/stdc++.h>
using namespace std;

void doit(char ar[50][50],int r,int c,int row,int col)
{
    char curr=ar[row][col];
    int end1=r-1;
    int start=0;
    int colstart=0;
    int colend=c-1;
    for(int i=row+1;i<r;++i)
    {
        if(ar[i][col]!='?')
        {
            end1=i-1;
            break;
        }
    }
    for(int i=row-1;i>=0;--i)
    {
        if(ar[i][col]!='?')
        {
            start=i+1;
            break;
        }
    }
    int chk=0;
    for(int j=col-1;j>=0;--j)
    {
        for(int i=start;i<=end1;++i)
        {
            if(ar[i][j]!='?')
            {
                colstart=j+1;
                chk=1;
                break;
            }
        }
        if(chk==1)
        {
            break;
        }
    }
    chk=0;
    for(int j=col+1;j<c;++j)
    {
        for(int i=start;i<=end1;++i)
        {
            if(ar[i][j]!='?')
            {
                colend=j-1;
                chk=1;
                break;
            }
        }
        if(chk==1)
        {
            break;
        }
    }

    //cout<<curr<<" "<<start<<" "<<end1<<" "<<colstart<<" "<<colend<<endl;
    for(int i=start;i<=end1;++i)
    {
        for(int j=colstart;j<=colend;++j)
        {
            ar[i][j]=curr;
        }
    }

/*
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            cout<<ar[i][j];
        }
        cout<<endl;
    }
*/
    return;
}

int main()
{
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
int t;
cin>>t;
for(int loop=0;loop<t;++loop)
{
    char ar[50][50],br[50][50];
    int r,c;
    string str;
    cin>>r>>c;
    for(int i=0;i<r;++i)
    {
        cin>>str;
        for(int j=0;j<c;++j)
        {
            ar[i][j]=str[j];
        }
    }
/*
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            cout<<ar[i][j];
        }
        cout<<endl;
    }*/

    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            br[i][j]=ar[i][j];
        }
    }


    for(int j=0;j<c;++j)
    {

    for(int i=0;i<r;++i)
    {
        if(br[i][j]!='?')
        {
            doit(ar,r,c,i,j);
        }
    }
    }
    cout<<"Case #"<<loop+1<<":"<<endl;
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            cout<<ar[i][j];
        }
        cout<<endl;
    }
}


return 0;
}
