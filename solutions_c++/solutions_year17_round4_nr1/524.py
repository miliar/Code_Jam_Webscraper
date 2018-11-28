#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int mod = 1000000007;
const int inf = 2147483647;
const ll linf = 1987654321987654321;

int tcn;
int n,p;

int g[111];
int a[5];
int main(){
    scanf("%d", &tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d: ", tc);
        scanf("%d%d",&n,&p);
        for(int i=0;i<p;i++)a[i]=0;
        for(int i=0;i<n;i++){
            scanf("%d",&g[i]);
            a[g[i]%p]++;
        }

        int ans=0;
        int x;
        ans+=a[0];
        if(p==2){
            ans+=(a[1]+1)/2;
        }
        else if(p==3){
            x=min(a[1],a[2]);
            ans+=x;
            a[1]-=x;
            a[2]-=x;
            if(a[1])ans+=(a[1]-1)/3+1;
            if(a[2])ans+=(a[2]-1)/3+1;
        }
        else if(p==4){
            x=0;
            if(a[2])ans+=a[2]/2;
            a[2]%=2;
            x = min(a[1],a[3]);
            ans+=x;
            a[1]-=x;
            a[3]-=x;
            if(a[2]){
                ans++;
                a[2]=0;
                a[1] = max(0,a[1]-2);
                a[3] = max(0,a[3]-2);
            }
            if(a[1])ans+=(a[1]-1)/4+1;
            if(a[3])ans+=(a[3]-1)/4+1;
        }

        printf("%d\n",ans);


    }
}
