#include <bits/stdc++.h>
using namespace std;
int main()
{
    std::ios::sync_with_stdio(false);
    freopen("a.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,r,c;
    char arr[25][25];
    cin>>t;
    for(int lc=1;lc<=t;lc++)
    {
        cin>>r>>c;
        for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            cin>>arr[i][j];
        for(int i=0;i<r;i++)
        for(int j=1;j<c;j++)
            if(arr[i][j]=='?')
            arr[i][j]=arr[i][j-1];
        for(int i=0;i<r;i++)
        for(int j=c-2;j>=0;j--)
            if(arr[i][j]=='?')
            arr[i][j]=arr[i][j+1];
        for(int i=1;i<r;i++)
        for(int j=0;j<c;j++)
            if(arr[i][j]=='?')
            arr[i][j]=arr[i-1][j];
        for(int i=r-1;i>=0;i--)
        for(int j=0;j<c;j++)
            if(arr[i][j]=='?')
            arr[i][j]=arr[i+1][j];
            cout<<"Case #"<<lc<<": "<<endl;
            for(int i=0;i<r;i++)
            {
             for(int j=0;j<c;j++)
            cout<<arr[i][j];
            cout<<endl;
            }
    }

    return 0;
}
