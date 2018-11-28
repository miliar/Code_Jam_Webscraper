#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,w;
    cin>>t;
    for(w=1;w<=t;w++)
    {
        char str[1005];
        cin>>str;
        int k;
        int l=strlen(str),count=0;
        cin>>k;
        for(int i=0;i<l;i++)
        {
            if(str[i]=='-')
            {
                count++;
                int runit=k,j=i;
                if(j+runit<=l)
                {
                while(runit--)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                    j++;
                }
            }
            }
        }
        int flag=0;
        for(int i=0;i<l;i++)
        {
            if(str[i]=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            printf("Case #%d: IMPOSSIBLE\n",w);
        }
        else
         {
            printf("Case #%d: %d\n",w,count);
         }
       
    }   
    return 0;
} 
