#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++) {
        string s;
        int k;
        int a[1100],b[1100];
        cin>>s>>k;
        printf("Case #%d: ",cas);
        int n=s.size();
        for (int i=0;i<n;i++) {
            if (s[i]=='-') a[i]=0;
            else a[i]=1;
        }
        memset(b,0,sizeof(b));
        bool flag=true;
        int cnt=0;
        for (int i=0;i<n;i++) {
            if (i>0) b[i]+=b[i-1];
            if ((a[i]+b[i])&1) continue;
            if (i+k-1>=n) {
                flag=false;
                break;
            } else {
                b[i]++;
                b[i+k]++;
                cnt++;
            }
        }
        if (!flag) printf("IMPOSSIBLE\n");
        else printf("%d\n",cnt);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
