#include <iostream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);

    int t;
    cin>>t;
    char ch[1000];
    bool arr[1000];
    int c=1;
    while(t--)
    {
       // cout<<"SDGDF";
        int count=0,i,k,j;
        cin>>ch;
        cin>>k;
        int w=0;
        for(i=0;ch[i]!='\0';i++)
        {
            //cout<<"SDGDF";
            //cout<<"SDGDF";
            if(ch[i]=='+')
                arr[i]=1;
            else
                arr[i]=0;

            w++;
        }

        for(i=0;ch[i]!='\0' && i<w-k+1;i++)
        {
            if(arr[i]==0)
            {
                for(j=i;j<i+k;j++)
                    arr[j]=!arr[j];

                count++;
            }
        }

        int flag=0;

        for(i=0;ch[i]!='\0';i++)
            if(arr[i]==0)
            {
                flag=1;
                break;
            }

        if(flag==0)
            cout<<"Case #"<<c++<<": "<<count<<endl;
        else
            cout<<"Case #"<<c++<<": IMPOSSIBLE"<<endl;
    }

    return 0;
}
