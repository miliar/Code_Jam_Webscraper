#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;

int T, k, n;
int main()
{
    scanf("%d", &T);
    int cas = 0;
    while(T--){
        scanf("%d %d", &n, &k);
        priority_queue<int> Q;
        Q.push(n);
        int a0, a1;
        while(k--) {
            int x = Q.top(); Q.pop();
            a0 = x/2, a1 = (x-1)/2;
            Q.push(a0); Q.push(a1);
        }
        printf("Case #%d: %d %d\n", ++cas, a0, a1);
    }
    return 0;
}
