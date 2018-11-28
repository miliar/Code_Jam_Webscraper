
/*****************************************
Author: lizi
Email: lzy960601@outlook.com
****************************************/
  
#include<bits/stdc++.h>
  
using namespace std;
  
const double eps=1e-10;
const double pi=3.1415926535897932384626433832795;
const double eln=2.718281828459045235360287471352;
  
#define LL long long
#define IN freopen("Al.in", "r", stdin)
#define OUT freopen("Al.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%d: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))

int T,k;
string s;

int main()
{
    IN;OUT;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>s>>k;
        int l=s.length();
        int ans=0;
        for(int i=0;i<=l-k;i++)
        {
            if(s[i]=='+')continue;
            ans++;
            for(int j=i;j<i+k;j++)
                if(s[j]=='-')s[j]='+';else s[j]='-';
        }
        for(int i=0;i<l;i++)
            if(s[i]!='+')ans=-1;
        prr(t);
        if(ans<0)printf("IMPOSSIBLE\n");else printf("%d\n",ans);
    }
    return 0;
}
