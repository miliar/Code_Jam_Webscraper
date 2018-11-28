#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<queue>
#include<algorithm>

using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("inputLarge.txt");
    out.open("outputLarge.txt");
    int t,cases=0;
    in>>t;
    while(t--)
    {
        cases++;
        int r,c;
        in>>r>>c;
        char arr[r][c];
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                in>>arr[i][j];
            }
        }
        int a[r];
        for(int i=0;i<r;i++)a[i]=0;
        for(int i=0;i<r;i++)
        {
            char last = arr[i][0];
            for(int j=1;j<c;j++)
            {
                if(arr[i][j] != last)
                {
                    if(last == '?')
                    {
                        for(int k=j;k>=0;k--)
                        {
                            arr[i][k] = arr[i][j];
                        }
                    }
                    else if(arr[i][j] == '?')
                    {
                        arr[i][j] = last;
                    }
                }
                last = arr[i][j];
            }
            if(last == '?') a[i]=1;
        }

        int index = 0;
        for(int i=0;i<r;i++)
        {
            if(a[i]==0)
            {
                index = i;
                break;
            }
        }
        for(int i=index-1;i>=0;i--)
        {
            for(int j=0;j<c;j++)
            {
                arr[i][j] = arr[i+1][j];
            }
        }
        for(int i=index+1;i<r;i++)
        {
            if(a[i] == 1)
            {
                for(int j=0;j<c;j++)
                {
                    arr[i][j] = arr[i-1][j];
                }
                a[i] = 0;
            }
        }
        out<<"Case #"<<cases<<": "<<endl;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                out<<arr[i][j];
            }
            out<<endl;
        }
    }
    return 0;
}
