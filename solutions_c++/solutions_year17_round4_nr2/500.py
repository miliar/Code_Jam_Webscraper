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
const ll linf = 987654321987654321;

int tcn;
int n,c,m;
int a[1010];
int b[1010];
int p[1010];
int person[1010];

int ti[1010][1010];
int main(){
    scanf("%d", &tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d: ", tc);
        scanf("%d%d%d",&n,&c,&m);
        for(int i=0;i<=c;i++){
            for(int j=0;j<=n;j++){
                ti[i][j]=0;
            }
        }
        int minr = 0;
        for(int i=0;i<=n;i++){
            a[i]=0;
        }
        for(int i=0;i<=c;i++){
            person[i]=0;
        }
        for(int i=0;i<m;i++){
            scanf("%d%d",&p[i], &b[i]);
            a[p[i]]++;
            person[b[i]]++;
        }
        int sum = 0;
        for(int i=1;i<=n;i++){
            sum+=a[i];
            minr = max(minr, sum/i + (sum%i?1:0));
        }
        for(int i=1;i<=c;i++){
            minr = max(minr, person[i]);
        }
        int ans=0;
        for(int i=1;i<=n;i++){
            if(a[i] > minr){
                ans+=a[i]-minr;
            }
        }
        printf("%d %d\n",minr, ans);








    }
}
