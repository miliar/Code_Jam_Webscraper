#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
#define LL long long

int n,d;

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        scanf("%d%d",&d,&n);
        double ans = 0;
        for (int i=0; i<n; i++) {
            int a,b;
            scanf("%d%d",&a,&b);
            ans = max(ans,(d-a)*1.0/b);
        }
        printf("Case #%d: %.9f\n",t,d/ans);

    }
	return 0;
}
