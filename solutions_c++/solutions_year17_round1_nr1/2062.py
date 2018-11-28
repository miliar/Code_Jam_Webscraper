#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#define ll long long
#define ull unsigned long long
#define rep(i,n) for(int i = 0;i < n; i++)
#define fil(a,b) memset((a),(b),sizeof(a))
#define cl(a) fil(a,0)
#define pb push_back
#define mp make_pair
#define exp 2.7182818
#define PI 3.141592653589793
#define inf 0x3f3f3f3f
#define fi first
#define se second
#define eps 1e-8
#define mod 2000000014ll
#define sign(x) ((x)>eps?1:((x)<-eps?(-1):(0)))
using namespace std;
double mysqrt(double x) { return max(0.0, sqrt(x)); }


int main(void)
{
    //freopen("1011.in","r",stdin);
    //freopen("001.out","w",stdout);
    int t,n,m;
    char tmp;
    cin>>t;
    for(int z=1;z<=t;++z)
    {
        cin>>n>>m;
        
        int hasha[30];
        char work[30][30];
        for(int i=1;i<=n;++i)
        {
            getchar();
            for(int j=1;j<=m;++j)
            {
                scanf("%c",&tmp);
                work[i][j]=tmp;
                
            }
        }
        for(int i=1;i<=n;++i)
        {
            int flag=0;
            for(int j=1;j<=m;++j)
            {
                if(work[i][j]!='?') {
                    int ta=j-1;
                    while(ta>=1&&work[i][ta]=='?') {work[i][ta]=work[i][j];ta--;}
                    ta=j+1;
                    while(ta<=m&&work[i][ta]=='?') {work[i][ta]=work[i][j];ta++;}
            }
            }
            /*
            for(int j=1;j<=m;++j)
            {
                if(work[i][j]=='?'&&flag) work[i][j]=tmp;
                
            }
            */
        }

        
        for(int j=1;j<=m;++j)
        {
            int flag=0;
            for(int i=1;i<=n;++i)
            {
                if(work[i][j]!='?') {
                    int ta=i-1;
                    while(ta>=1&&work[ta][j]=='?') {work[ta][j]=work[i][j];ta--;}
                    ta=i+1;
                    while(ta<=n&&work[ta][j]=='?') {work[ta][j]=work[i][j];ta++;}
                }
            }
            
        }
        
        
        printf("Case #%d:\n",z);
        for(int i=1;i<=n;++i)
        {
            for(int j=1;j<=m;++j)
            {
                printf("%c",work[i][j]);
            }
            cout<<endl;
        }

    }

    return 0;
}