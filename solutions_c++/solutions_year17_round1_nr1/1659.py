#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    freopen("a1.in","r",stdin);
    freopen("a.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll tt;
    cin>>tt;
    for(ll t=1; t<=tt; t++)
    {
        int r,c;
        cin>>r>>c;
        char arr[r+1][c+1];
        for(int i=0; i<r; i++)
        {
            string str;
            cin>>str;
            for(int j=0;j<c;j++)
                arr[i][j]=str[j];
        }
        while(1)
        {
            for(int i=0; i<r; i++)
            {
                for(int j=0; j<c; j++)
                {
                    if(arr[i][j]!='?')
                    {
                        for(int k=j-1; k>=0 && arr[i][k]=='?'; k--)
                            arr[i][k]=arr[i][j];
                        for(int k=j+1; k<c && arr[i][k]=='?'; k++)
                            arr[i][k]=arr[i][j];
                    }
                }
            }
            for(int i=0; i<r; i++)
            {
                for(int j=0; j<c; j++)
                {
                    if(arr[i][j]!='?')
                    {
                        for(int k=i-1; k>=0 && arr[k][j]=='?'; k--)
                            arr[k][j]=arr[i][j];
                        for(int k=i+1; k<r && arr[k][j]=='?'; k++)
                            arr[k][j]=arr[i][j];
                    }
                }
            }
            int cou=0;
            for(int i=0; i<r; i++)
            {
                for(int j=0; j<c; j++)
                {
                    if(arr[i][j]!='?')
                    {
                        cou++;
                    }
                }
            }
            if(cou==r*c)
                break;
        }




        cout<<"Case #"<<t<<":"<<endl;
        for(int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                cout<<arr[i][j];
            }
            cout<<endl;
        }
        cout<<endl;
        cerr<<"Test Case "<<t<<" Solved"<<endl;
    }
    return 0;
}
