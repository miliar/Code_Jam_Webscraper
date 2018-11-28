#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t,r,c,cs=0;
    char arr[30][30];
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    while(t--)
    {
        cs++;
        cin>>r>>c;
        for(int i=0;i<r;i++)
            for(int j=0;j<c;j++)
                cin>>arr[i][j];
        for(int i=0;i<r;i++)
        {
            char cur='?';
            for(int j=0;j<c;j++)
            {
                if(arr[i][j]!='?')
                {
                    cur=arr[i][j];
                    for(int k=j-1;k>=0;k--)
                    {
                        if(arr[i][k]=='?')
                            arr[i][k]=cur;
                        else break;
                    }
                }
                else
                {
                    arr[i][j]=cur;
                }
            }
        }
        for(int j=0;j<c;j++)
        {
            char cur='?';
            for(int i=0;i<r;i++)
            {
                if(arr[i][j]!='?')
                {
                    cur=arr[i][j];
                    for(int k=i-1;k>=0;k--)
                    {
                        if(arr[k][j]=='?')
                            arr[k][j]=cur;
                        else break;
                    }
                }
                else
                {
                    arr[i][j]=cur;
                }
            }
        }
        cout<<"Case #"<<cs<<":\n";
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cout<<arr[i][j];
            }
            cout<<"\n";
        }
    }
    return 0;
}
