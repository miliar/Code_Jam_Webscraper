#include<bits/stdc++.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("output.in");
char arr[1000];
int main()
{
    int tc;
    fin>>tc;
    int z=tc;
    while(tc--)
    {
        fin>>arr;
        int p;
        fin>>p;
        int sum=0;
        int l=strlen(arr);
        for(int i=0;i<=l-p;i++)
        {
            if(arr[i]=='-')
            {
                sum++;
                for(int j=0;j<p;j++)
                {
                    if(arr[i+j]=='-')
                    {
                        arr[i+j]='+';
                    }
                    else
                    {
                        arr[i+j]='-';
                    }
                }
            }
        }
        int flag=0;
        for(int i=0;i<l;i++)
        {
            if(arr[i]=='-')
            {
                fout<<"Case #"<<z-tc<<": "<<"IMPOSSIBLE\n";
                flag=1;
                break;
            }
        }
        if(flag==0)
        fout<<"Case #"<<z-tc<<": "<<sum<<endl;
    }
    return 0;
}
