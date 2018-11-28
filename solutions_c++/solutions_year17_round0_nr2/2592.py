#include <bits/stdc++.h>

using namespace std;

#define MP make_pair
#define PB push_back
typedef long long LL;
typedef pair<int,int> PII;
const double eps=1e-8;
const double pi=acos(-1.0);
const int K=1e6+7;
const int mod=1e9+7;


char ss[100];
int main(void)
{
    int t,cnt=1,len;
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&t);
    //cout<<t<<endl;
    while(t--)
    {
        scanf("%s",ss+1);
        len=strlen(ss+1);
        for(int i=len;i>1;i--)
        if(ss[i]<ss[i-1]||ss[i]=='0')
        {
            int j=i;
            while('9'>ss[j]&&j<=len)ss[j]='9',j++;
            ss[i]='9';
            if(ss[i-1]!='0')ss[i-1]--;
        }
        if(ss[1]>'0')
        {
            sort(ss+1,ss+1+len);
            printf("Case #%d: %s\n",cnt++,ss+1);
        }
        else
        {
            sort(ss+2,ss+1+len);
            printf("Case #%d: %s\n",cnt++,ss+2);
        }

    }
    return 0;
}
