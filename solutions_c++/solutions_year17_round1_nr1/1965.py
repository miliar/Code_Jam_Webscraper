#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string.h>
#include<iomanip>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for(int q=1;q<=t;q++)
    {

        int r,c;
        cin>>r>>c;
        char arr[r+1][c+1];
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cin>>arr[i][j];
            }
        }
        cout<<"Case #"<<q<<":\n";
        bool vis[26];
        memset(vis,false,sizeof(vis));
        char recent='0';
        bool flag = false;
        for(int i=0;i<r;i++)
        {   recent='0';
            flag=false;
            for(int j=0;j<c;j++)
            {
                if(arr[i][j]=='?')
                {
                    if(recent!='0')
                    {
                        arr[i][j]=recent;
                    }
                }
                else {
                        vis[i] = true;
                        recent=arr[i][j];
                        if(!flag)
                        {for(int k=0;k<j;k++)
                        {
                            if(arr[i][k]=='?')
                                arr[i][k]=recent;
                            flag=true;
                        }}
                    }
            }

        }
        for(int i=0;i<r;i++)
        {
            if(vis[i]==true)
            {
                if(i!=0 && vis[i-1]==false)
                {
                    for(int j=0;j<c;j++)
                    {
                        arr[i-1][j]=arr[i][j];
                    }
                    vis[i-1]=true;
                    int k=i-2;
                    while(k>=0 && vis[k]==false)
                    {
                        for(int j=0;j<c;j++)
                        {
                            arr[k][j]=arr[i][j];
                        }
                        vis[k]=true;
                        k--;
                    }

                }
                if(i!=r-1 && vis[i+1]==false)
                {
                    for(int j=0;j<c;j++)
                    {
                        arr[i+1][j]=arr[i][j];
                    }
                    vis[i+1]=true;
                    int k=i+2;
                    while(k<r && vis[k]==false)
                    {
                        for(int j=0;j<c;j++)
                        {
                            arr[k][j]=arr[i][j];
                        }
                        vis[k]=true;
                        k++;
                    }
                }

            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cout<<arr[i][j];
            }
            cout<<endl;
        }
    }
    fclose(stdin);
   fclose(stdout);
    return 0;
}
