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
char str[1009];
int main()
{
    int t;
    sci(t);
    int c=0;
    while(t--)
    {
        int n,r,o,y,g,b,v,tot=0,i,j,k;
        c++;
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        printf("Case #%d: ",c);
        ll ar[3];
        ar[0]=r;
        ar[1]=y;
        ar[2]=b;
        char ch[3];
        ch[0]='R';
        ch[1]='Y';
        ch[2]='B';
        for(i=0;i<3;i++)
        {
            if(ar[i]>0)
            {
                str[0]=ch[i];
                ar[i]--;
                break;
            }
        }
        for(i=1;i<n;i++)
        {
            ll maxx=max(ar[0],max(ar[1],ar[2]));
            ll minn=min(ar[0],min(ar[1],ar[2]));
            ll lol=ar[0]+ar[1]+ar[2]-maxx-minn;
            for(j=0;j<3;j++)
            {
                if(ar[j]==maxx)
                break;
            }
            if(i==0||ch[j]!=str[i-1])
            {
                str[i]=ch[j];
                ar[j]--;
                continue;
            }
            for(k=0;k<3;k++)
            {
                if(k!=j&&ar[k]==lol)
                break;
            }
            if(ar[k]==0)
            break;
            ar[k]--;
            str[i]=ch[k];
        }
        str[n]='\0';
        if(i<n||str[0]==str[n-1])
        printf("IMPOSSIBLE\n");
        else
        printf("%s\n",str);
    }
    return 0;
}