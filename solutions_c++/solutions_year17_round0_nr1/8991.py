#include <bits/stdc++.h>

using namespace std;
#define mod  1000000007
typedef long long ll;
#define N 123456


int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("outALarge.txt","w",stdout);
    scanf("%d",&T);
    for (int _=1;_<=T;_++)
    {
        string s;
        int n;
        cin>>s;
        cin>>n;

        int num  = 0;
        int len = s.size();
        for (int i=0;i<len;i++)
        if (s[i]=='-')
        {
            if (i+n>len)
            {
                num = -1;
                break;
            }

            num++;
            for (int j=i;j<i+n;j++)
            {
                if (s[j]=='-') s[j]='+';
                else s[j]='-';
            }
        }

        if (num == -1)
        {
            // cout<<s<<endl;
             printf("Case #%d: IMPOSSIBLE\n",_);
        }
        else
        {
             printf("Case #%d: %d\n",_,num);
        }
    }
    return 0;
}
