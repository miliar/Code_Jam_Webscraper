#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int maxn=50;

char a[maxn][maxn];
int m,n;


int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%d%d",&m,&n);
        for(int i=1; i<=m; ++i) scanf("%s",a[i]+1);
        for(int i=1; i<=m; ++i){
            char last='@';
            for(int j=1; j<=n; ++j){
                if(a[i][j]!='?') last = a[i][j];
                if(last!='@') a[i][j]=last;
            }
            last='@';
            for(int j=n; j>=1; --j){
                if(a[i][j]!='?') last = a[i][j];
                if(last!='@') a[i][j]=last;
            }
        }
        int lastRow=0;
        for(int i=1; i<=m; ++i){
            if(a[i][1]!='?') lastRow=i;
            if(a[i][1]=='?' && lastRow) for(int j=1; j<=n; ++j) a[i][j]=a[lastRow][j];
        }
        lastRow=0;
        for(int i=m; i>=1; --i){
            if(a[i][1]!='?') lastRow=i;
            if(a[i][1]=='?' && lastRow) for(int j=1; j<=n; ++j) a[i][j]=a[lastRow][j];
        }
        printf("Case #%d:\n",tt);
        for(int i=1; i<=m; ++i) printf("%s\n",a[i]+1);
    }

}
