#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define ll long long
#define pii pair<int,int>
#define tii tuple <int,int,int>
#define N 100005
#define mod 2000003
#define X first
#define Y second
#define eps 0.0000000001
#define all(x) x.begin(),x.end()
#define tot(x) x+1,x+n+1
using namespace std;
int sol,cnt[1010],n,t,T,k;
char s[1010];
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);

    for(int t=1; t<=T; t++) {
        scanf("%s%d",&s,&k);
        n=strlen(s);
        sol=0;
        memset(cnt,0,sizeof(cnt));
         int j;
        for( j=n-k; j>=0; j--) {
            cnt[j+k-1]+=cnt[j+k];

            if((s[j+k-1]=='-'&&cnt[j+k-1]%2==0)||(s[j+k-1]=='+'&&cnt[j+k-1]%2==1)) {
                cnt[j+k-1]++;
                sol++;
                cnt[j-1]--;
            }
        }
        for(j=k-2;j>=0;j--)
            cnt[j]+=cnt[j+1];

        for(j=0; j<n; j++)
            if((s[j]=='+'&&cnt[j]%2==0)||(s[j]=='-'&&cnt[j]%2==1))
                ;
            else
                break;

        if(j!=n)
            printf("Case #%d: IMPOSSIBLE\n",t);
        else
            printf("Case #%d: %d\n",t,sol);
    }

    return 0;
}
