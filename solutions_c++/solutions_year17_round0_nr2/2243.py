#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
const int maxn = 110;
int a[maxn];
int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T, cas = 0; 
    scanf("%d", &T);
    while (T--) {
        long long n;
        cin >> n;
        
        n++;
        //memset(a,0,sizeof(a));
        long long tmp = n;
        int tot = 0;
        while (tmp) {
            a[++tot] = tmp%10;
            tmp /= 10;
        }
        
        long long now = 0;
        long long ans = 0; 
        for (int i = tot; i >= 1; i--) {
            now = now*10;
            if (a[i] != 0 && (i == tot || a[i]-1 >= a[i+1])) {
                long long tmp = now+a[i]-1;
                for (int j = i-1; j >= 1; j--) {
                    tmp = tmp * 10 + 9;
                }
                if (tmp > ans) ans = tmp;
            }
            if (i < tot && a[i] < a[i+1]) break;
            now += a[i];
        }
        printf("Case #%d: ", ++cas);
        cout << ans << endl;
    }
}