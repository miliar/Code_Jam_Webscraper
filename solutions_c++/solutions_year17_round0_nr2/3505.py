#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
string s;
int n;
int ans[20];
bool dfs(int po,int pre,bool flag) {
    if (po>=n) return true;
    int now=s[po]-'0';
    if (po==0) {
        ans[0]=now;
        return dfs(po+1,now,flag);
    }
    if (now<pre&&(!flag)) return false;
    if (flag) {
        for (int i=9;i>=pre;i--) {
            ans[po]=i;
            if (dfs(po+1,i,flag)) return true;
        }
    } else {
        for (int i=now;i>=pre;i--) {
            ans[po]=i;
            if (i<now) {
                if (dfs(po+1,i,true)) return true;
            } else {
                if (dfs(po+1,i,flag)) return true;
            }
        }
    }
    return false;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++) {
        cin>>s;
        n=s.size();
        memset(ans,0,sizeof(ans));
        printf("Case #%d: ",cas);
        if (dfs(0,-1,false)) {
            for (int i=0;i<n;i++) printf("%d",ans[i]);
            printf("\n");
        } else {
            ans[0]=s[0]-'1';
            if (s[0]-'0'>1) printf("%d",s[0]-'1');
            for (int i=1;i<n;i++) printf("9");
            printf("\n");
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
