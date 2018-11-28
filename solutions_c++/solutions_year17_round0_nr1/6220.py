#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large (3).in","r",stdin);
    freopen("temp_big.out","w",stdout);
    int t;
    scanf("%d",&t);
    int test=0;
    while(t--)
    {
        test++;
        string str;
        cin >> str;
        int k,coun=0;
        scanf("%d",&k);
        int lo=0,hi=k-1;
        int n=str.size();
        while(hi<n-1)
        {
            if(str[lo]=='+')
            {
                lo++;
                hi++;
            }
            else
            {
                coun++;
                for(int i=lo;i<=hi;i++)
                {
                    if(str[i]=='+')
                    str[i]='-';
                    else
                        str[i]='+';
                }
                lo++;
                hi++;
            }
        }
        char prev=str[lo];
        int siz=1;
        //printf("lo=%d hi=%d str[lo]=%c\n",lo,hi,prev);
        for(int i=lo+1;i<=hi;i++)
        {
            //printf("str[i]=%c\n",str[i]);
            if(str[i]==prev)
                siz++;
        }
        if(siz==k && prev=='+')
            printf("Case #%d: %d\n",test,coun);
        else if(siz==k && prev=='-')
            printf("Case #%d: %d\n",test,coun+1);
        else
            printf("Case #%d: IMPOSSIBLE\n",test);

    }
    return 0;
}
