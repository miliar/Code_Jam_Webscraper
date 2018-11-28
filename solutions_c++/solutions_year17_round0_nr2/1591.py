#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sci(fd) scanf("%d",&fd)
#define scll(fd) scanf("%lld",&fd)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define pii pair < int,int > 
#define pll pair < ll,ll >
#define fi first
#define se second
#define LOGN 20
const ll infi=1000000000000000009;
char str[109];
int main()
{
    int t,y=0;
    sci(t);
    while(t--)
    {
        int i,j;
        y++;
        
        scanf("%s",str);
        int n=strlen(str);
        for(i=n-2;i>=0;i--)
        {
            if(str[i]>str[i+1])
            {
                str[i]=str[i]-1;
                for(j=i+1;j<n;j++)
                str[j]='9';
            }
        }
        printf("Case #%d: ",y);
        if(str[0]!='0')
        printf("%c",str[0]);
        for(i=1;i<n;i++)
        printf("%c",str[i]);
        printf("\n");
    }
    return 0;
}