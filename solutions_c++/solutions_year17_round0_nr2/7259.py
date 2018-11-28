#include <iostream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <algorithm>
#include <vector>

using namespace std;

char ans[19];
char arr[19];

void solve()
{
        int i,j;
        ans[0]=arr[0];
        for(i=1;arr[i]!='\0';i++)
        {
            if(arr[i-1]>arr[i])
            {
                ans[i-1]=arr[i-1]-1;
                for(j=i;arr[j]!='\0';j++,i++)
                    ans[j]='9';
                ans[j]='\0';
                break;
            }
            else
                ans[i]=arr[i];
        }
        ans[i]='\0';
}

int check()
{
    for(int i=1;ans[i]!='\0';i++)
        if(ans[i]<ans[i-1])
        {
            for(int j=0;ans[j]!='\0';j++)
                arr[j]=ans[j];
            return 1;
        }
    return 0;
}

int main()
{

    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);

    int t,count=1;
    cin>>t;
    while(t--)
    {
        cin>>arr;
        //cout<<n;
        int i;
        do
        {
            solve();
            for(i=0;ans[i]!='\0';i++)
                if(ans[i]!='0')
                    break;
        }while(check());

        cout<<"Case #"<<count++<<": "<<&ans[i]<<endl;
    }

    return 0;
}
