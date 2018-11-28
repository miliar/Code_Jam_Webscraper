#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    int r,c;

    for(int l=0;l<t;l++)
    {
        scanf("%d%d", &r, &c);

        char arr[r][c];

        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cin>>arr[i][j];
            }
        }
        //

        for(int kk=0;kk<650;kk++)
        {
            for(int i=0;i<r;i++)
            {
                for(int j=0;j<c;j++)
                {
                    if(arr[i][j]=='?')
                    {
                        if(i>0&&arr[i-1][j]!='?')
                        {
                            arr[i][j] = arr[i-1][j];
                        }
                        else
                        {
                            if(i<r-1&&arr[i+1][j]!='?')
                            {
                                arr[i][j] = arr[i+1][j];
                            }
                        }
                    }
                }
            }

            for(int i=r-1;i>=0;i--)
            {
                for(int j=c-1;j>=0;j--)
                {
                    if(arr[i][j]=='?')
                    {
                        if(i<r-1&&arr[i+1][j]!='?')
                        {
                            arr[i][j] = arr[i+1][j];
                        }
                        else
                        {
                            if(i>0&&arr[i-1][j]!='?')
                            {
                                arr[i][j] = arr[i-1][j];
                            }
                        }
                    }
                }
            }
            //
            for(int i=0;i<r;i++)
            {
                for(int j=0;j<c;j++)
                {
                    if(arr[i][j]=='?')
                    {
                        if(j>0&&arr[i][j-1]!='?')
                        {
                            arr[i][j] = arr[i][j-1];
                        }
                        else
                        {
                            if(j<c-1&&arr[i][j+1]!='?')
                            {
                                arr[i][j] = arr[i][j+1];
                            }
                        }
                    }
                }
            }
            for(int i=r-1;i>=0;i--)
            {
                for(int j=c-1;j>=0;j--)
                {
                    if(arr[i][j]=='?')
                    {
                        if(j<c-1&&arr[i][j+1]!='?')
                        {
                            arr[i][j] = arr[i][j+1];
                        }
                        else
                        {
                            if(j>0&&arr[i][j-1]!='?')
                            {
                                arr[i][j] = arr[i][j-1];
                            }
                        }
                    }
                }
            }

        }

        //

        cout<<"Case #"<<l+1<<":"<<endl;

        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cout<<arr[i][j];
            }
            cout<<endl;
        }
    }
}
