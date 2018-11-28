#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("ainput.txt","r",stdin);
   freopen("input123.out","w",stdout);
    int t,tc,i,j,k,l,cnt,m;
    string str;
    cin>>tc;
    t=0;
    //getchar();
    while(tc--)
    {
        t++;
        cin>>str>>k;
        l=str.length();

        cnt=0;
        m=0;
        for(i=0;i<l-k+1;i++)
        {
            if(str[i]=='-')
            {
                for(j=i;j<i+k;j++)
                {
                    if(str[j]=='-'){
                        str[j]='+';
                    }
                    else str[j]='-';
                }
                cnt++;
            }
        }
       // cout<<str<<endl;
        for(i=l-k;i<l;i++)
        {
            if(str[i]=='-')
            {
                m=1;
                break;
            }
        }
        if(m==0)
            printf("Case #%d: %d\n",t,cnt);
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
