#include <bits/stdc++.h>
using namespace std;
const int maxn=100;

char number[maxn];
int T,N;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int kase=1;kase<=T;++kase)
    {
        scanf("%s",number);
        int pre=-1;
        int cur;
        N=strlen(number);
        for(int i=0;i<N;++i)
        {
            cur=number[i]-'0';
            if(cur<pre)
            {
                cur=pre;
                pre=i-1;
                while(pre-1>=0&&number[pre-1]-'0'==cur)
                    --pre;
                number[pre]--;
                for(int j=pre+1;j<N;++j)
                    number[j]='9';
                break;
            }
            pre=cur;
        }
        int beg=0;
        while(number[beg]=='0'&&beg<N-1)
            ++beg;
        printf("Case #%d: %s\n",kase,number+beg);
    }
    return 0;
}
