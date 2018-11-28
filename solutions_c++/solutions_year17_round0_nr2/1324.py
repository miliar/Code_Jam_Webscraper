#include"bits/stdc++.h"
using namespace std;
typedef long long LL;
char a[100];
int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("out22.txt", "w", stdout);
    int n;
    cin >> n;
    for(int cas = 1; cas <= n; cas ++){
        cin >> a;
        int len = strlen(a);
        for(int i = len - 1; i >= 1; i --){
            int k = i;
            while(i >= 1 && a[i - 1] <= a[i]){
                i --;
            }
            if(i == 0) break;
            a[i - 1] --;
            for(int j = i; j <= k; j ++){
                a[j] = '9';
            }
        }
        LL ans = 0;
        for(int i = 0; i < len; i ++){
            ans *= 10;
            ans += a[i] - '0';
        }
        printf("Case #%d: ", cas);
        cout << ans << endl;

    }
    return 0;
}
