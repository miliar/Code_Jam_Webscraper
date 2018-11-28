#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin>>T;

    for(int t = 1;t<=T;t++ )
    {
        int r,c;
        cin>>r>>c;
        char ca;
        char a[100][100];
        for(int i = 0;i< r;i++)
        {
            for(int j  = 0;j< c;j++)
            {
                cin>>a[i][j];
                if(a[i][j] != '?')
                    ca = a[i][j];
            }
        }


        for(int i = 0;i< r;i++)
        {
            for(int j  = 0;j< c;j++)
            {
                if(a[i][j] != '?')
               {
                   for(int k = j+1;k<c;k++)
                   {
                       if(a[i][k] == '?')
                       a[i][k] = a[i][j];
                       else
                        break;
                   }
                   for(int k = j-1;k>=0;k--)
                   {
                       if(a[i][k] == '?')
                       a[i][k] = a[i][j];
                       else
                        break;
                   }


               }
            }
        }

        for(int i = 0;i< r;i++)
        {
            for(int j  = 0;j< c;j++)
            {
                if(a[i][j] == '?' && i != 0)
               {
                   a[i][j] = a[i-1][j];


               }
            }
        }
        for(int i = r-1;i>=0;i--)
        {
            for(int j  = 0;j< c;j++)
            {
                if(a[i][j] == '?' && i != r-1)
               {
                   a[i][j] = a[i+1][j];


               }
            }
        }
        cout<<"Case #"<<t<<":\n";
        for(int i = 0;i< r;i++)
        {
            for(int j  = 0;j< c;j++)
            {

                cout<<a[i][j];
            }
            cout<<endl;
        }
    }
}
