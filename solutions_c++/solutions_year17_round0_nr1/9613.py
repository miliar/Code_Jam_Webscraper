#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,cs=0,k,i,c,j,flag;
    string s;
    freopen("C:\\Users\\RHT\\Downloads\\A-large.in","r",stdin);
    freopen("C:\\Users\\RHT\\Downloads\\output.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        cs++;
        c = 0;
        flag = 0;
        cin >> s >> k;
        for(i=0; i<s.size(); i++)
        {
            if(s[i]=='-')
            {
                if((s.size()-i)<k)
                {
                    flag = 1;
                    break;
                }
                for(j=i+1; (j-i)<k; j++)
                {
                    if(s[j]=='-')   s[j] = '+';
                    else    s[j] = '-';
                }
                c++;
            }
        }
        if(flag)   printf("Case #%d: IMPOSSIBLE\n",cs);
        else    printf("Case #%d: %d\n",cs,c);
    }
    return 0;
}
