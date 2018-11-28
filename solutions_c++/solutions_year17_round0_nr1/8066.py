#include <iostream>
#include <stdio.h>
#include <cstring>
#include <string>
using namespace std;
int casos,k,tama,con,x,ban;
string cks;
int main()
{
    freopen("i.in","r",stdin);
    freopen("o.out","w",stdout);
    x=0;
    scanf("%d",&casos);
    while(casos--)
    {
        x++;
        ban=0;
        con=0;
        cin>>cks;
        scanf("%d",&k);
        tama=cks.size();
        for(int i=0;i<tama-k+1;i++)
        {
            if(cks[i]=='-')
            {
                con++;
                for(int j=0;j<k;j++)
                {
                    if(cks[i+j]=='-')
                    {
                        cks[i+j]='+';
                    }
                    else
                       cks[i+j]='-';
                }

            }
        }
        for(int i=tama-k+1;i<tama;i++)
        {
            if(cks[i]=='-')
                ban=1;
        }
        if(ban==1)
            printf("case #%d: IMPOSSIBLE\n",x);
        else
            printf("case #%d: %d\n",x,con);
    }

}
