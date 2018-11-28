#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#include<queue>
#include<stack>
#include<map>
#include<vector>
const double PI = acos(-1.0);
const double e = exp(1.0);
template<class T> T gcd(T a, T b) {
	return b ? gcd(b, a % b) : a;
}
template<class T> T lcm(T a, T b) {
	return a / gcd(a, b) * b;
}
using namespace std;
#define ll __int64
int k;
char str[1010];

int main()
{
    int t;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        printf("Case #%d: ",cas++);
        int ans=0;
        scanf("%s%d",str,&k);
        int l=strlen(str);
        for(int i=0;i<l-k+1;i++)
        {
            if(str[i]=='-')
            {
                for(int j=i;j<=i+k-1;j++)
                {
                    if(str[j]=='+')str[j]='-';
                    else str[j]='+';
                }
                ans++;
            }
        }
        int flag=0;
        for(int i=l-k+1;i<l;i++){
            if(str[i]=='-')
                flag=1;

        }
        if(flag)printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);

    }
    return 0;
}
