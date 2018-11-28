#include<stdio.h>
#include<stdlib.h>
#include<istream>
#include<vector>
#include<math.h>
#include<stack>
#include<string.h>
#include<algorithm>
#define mod 10000009
#define maxn 10001
using namespace std;
char s[100005];
int q[5][100005];

int main()
{
	freopen("d:\\in.txt","r",stdin);
    int T;
    scanf("%d",&T);
    while(T)
    {
        scanf("%s",s);
        int len=strlen(s);
        memset(q,0,sizeof(q));
        int i;
        long long int ans=1;
        if((s[0]-'0')==1)
           q[2][0]=1;
        else
           q[3][0]=1;
        for(i=1;i<len;i++)
        {
            ans++;
            int t=s[i]-'0';
            if(t==1)
            {
                ans+=q[2][i-1];
                ans+=q[1][i-1];
                ans+=q[0][i-1];
                q[1][i]=q[3][i-1];
                q[0][i]=q[2][i-1];
                q[2][i]=q[0][i-1]+1;
                q[3][i]=q[1][i-1];
            }
            else
            {
                ans+=q[3][i-1];
                ans+=q[1][i-1];
                ans+=q[0][i-1];
                q[1][i]=q[2][i-1];
                q[0][i]=q[3][i-1];
                q[2][i]=q[1][i-1];
                q[3][i]=q[0][i-1]+1;
            }
        }
        printf("%lld\n",ans);
        T--;
    }
	return 0;
}
