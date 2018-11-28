#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<iostream>
using namespace std;
int a[1100],n,k;
char s[1100];
const char* problem = "A-large";
int main()
{
    char infile[60],outfile[60];
    snprintf(infile,60,"%s.in",problem);
    snprintf(outfile,60,"%s.out",problem);
    freopen(infile,"r",stdin);
    freopen(outfile,"w",stdout);
    int t,cas=0;
    cin>>t;
    while(t--)
    {
        scanf("%s %d",s,&k);
        n=strlen(s);
        for(int i=0;i<n;++i)
            a[i]=s[i]=='+'?1:0;
        int ans=0;
        bool flag=false;
        for(int i=0;i+k<=n;++i)
        {
            if(!a[i])
            {
                int cnt=0,lim=i+k;
                for(int j=i;j<lim;++j)
                    cnt+=a[j];
                if(cnt<k)
                {
                    for(int j=i;j<lim;++j)
                        a[j]^=1;
                    ++ans;
                }
            }

        }
        for(int i=0;i<n;++i)
            if(!a[i])
        {
            flag=true;
            break;
        }
        printf("Case #%d: ",++cas);
        if(flag) puts("IMPOSSIBLE");
        else cout<<ans<<endl;
    }
}

