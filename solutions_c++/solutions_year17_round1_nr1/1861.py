#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int x=1;
    while(x<=t)
    {
         int r,c;
         cin>>r>>c;
         char arr[r][c];
         int i,j=0;
         for(i=0;i<r;i++)
         {
             for(j=0;j<c;j++)
                  cin>>arr[i][j];
         }
         for(i=0;i<r;i++)
         {  int p=0;
             for(j=0;j<c;j++)
             {


             if(arr[i][j]=='?'&&j>0&&arr[i][j-1]!='?')
                          arr[i][j]=arr[i][j-1];



         }
         for(j=c-1;j>=0;j--)
         {
             if(arr[i][j]=='?'&&j<c-1&&arr[i][j+1]!='?')
                  arr[i][j]=arr[i][j+1];

         }}
         for(i=0;i<c;i++)
         {  int p=0;
             for(j=0;j<r;j++)
             {

                if(arr[j][i]=='?'&&j>0&&arr[j-1][i]!='?')
                          {  arr[j][i]=arr[j-1][i];
                             p=j;
                          }



         }
             for(j=r-1;j>=0;j--)
                   if(arr[j][i]=='?'&&j<r-1&&arr[j+1][i]!='?')
                       arr[j][i]=arr[j+1][i];
         }
         cout<<"Case #"<<x<<":";
         cout<<endl;
         for(i=0;i<r;i++)
         {
             for(j=0;j<c;j++)
                    cout<<arr[i][j];
             cout<<endl;
         }
         x++;
    }

    return 0;
}
