#include<bits/stdc++.h>

using namespace std;

char arr[30][30];
int main(void)
{
    freopen("C:\\Users\\ACER\\Desktop\\input.in","r",stdin);
freopen("C:\\Users\\ACER\\Desktop\\output.txt","w",stdout);

    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int r,c;
        cin>>r>>c;
        for(int j=1;j<=r;j++)
        {
            for(int k=1;k<=c;k++)
                cin>>arr[j][k];
        }


        char cur;
        for(int j=1;j<=r;j++)
        {

            for(int k=1;k<=c;k++)
            {
                    if(arr[j][k]!='?')
                    {
                        cur=arr[j][k];


                        for(int z=k-1;z>=1;z--)
                        {
                            if(arr[j][z]=='?')
                                arr[j][z]=cur;
                            else
                                    break;
                        }
                        for(int z=k+1;z<=c;z++)
                        {
                            if(arr[j][z]=='?')
                                arr[j][z]=cur;
                            else
                                break;
                        }
                    }

            }
        }
        for(int k=1;k<=c;k++)
        {

            for(int j=1;j<=r;j++)
            {
                    if(arr[j][k]!='?')
                    {
                        cur=arr[j][k];
                        for(int z=j-1;z>=1;z--)
                        {
                            if(arr[z][k]=='?')
                                arr[z][k]=cur;
                            else
                                    break;
                        }
                        for(int z=j+1;z<=r;z++)
                        {
                            if(arr[z][k]=='?')
                                arr[z][k]=cur;
                            else
                                break;
                        }
                    }

            }
        }
        cout<<"Case #"<<i<<":"<<endl;
        for(int j=1;j<=r;j++)
        {
            for(int k=1;k<=c;k++)
                cout<<arr[j][k];
            cout<<endl;
        }


    }
}
