#include <bits/stdc++.h>
typedef long long ll;
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a_large_out.txt","w",stdout);
    int t,C=1,k,i,j;
    scanf("%d",&t);
    while(t--)
    {
        string s;
        cin >> s>>k;
        int step=0,size=s.size();
        for(i=0;i<=(size-k);i++)
        {
            if(s[i]=='-')
            {
                for(j=i;j<(i+k);j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                //cout << s << endl;
                step++;
            }
        }
        int flag=0;
        for(i=0;i<size;i++)
        {
            if(s[i]!='+')
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
            printf("Case #%d: %d\n",C++,step);
        else
            printf("Case #%d: IMPOSSIBLE\n",C++);
    }
    return 0;
}
