#include <iostream>
#include <iomanip>
#include <cmath>
#include <stdio.h>
#include <string>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int N=1;
    cin>>N;
    for(int i=1;i<=N;i++)
    {
        int x=0,sz=1;
        string pancake;
        cin>>pancake;
        cin>>sz;
        for(int j=pancake.size()-1;j>=sz-1;j--)
        {
            if(pancake[j]=='-')
            {
                for(int k=0;k<sz;k++)
                {
                    if(pancake[j-k]=='+')
                    {
                        pancake[j-k]='-';
                    }
                    else
                    {
                        pancake[j-k]='+';
                    }
                }
                x++;
            }

        }
        int a;
        bool chk=0;
        for(a=0;a<sz;a++)
        {
            if(pancake[a]=='-')
               {
                 chk=1;
                 break;
               }
        }
        if(chk==1||sz==0)
        {
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": "<<x<<endl;
        }

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
