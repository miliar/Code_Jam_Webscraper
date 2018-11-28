#include<cstdio>
#include<algorithm>
using namespace std;
const int MAX = 1000 + 10;
int rec[MAX];
int main(){ 
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++) {
        printf("Case #%d: ", casen);
        int n, m;
        scanf("%d %d", &n, &m);
        for(int i = 0 ; i < n ; i++){ 
            scanf("%d", &rec[i]);
        }
        if(m == 2) {
            int a = 0, b = 0;
            for(int i = 0 ; i < n ; i++) {
                if(rec[i] % 2 == 0) a++;
                else b++;
            }
            printf("%d\n", a + (b+1)/2);
        } else if(m == 3) {
            int a = 0, b = 0, c = 0, ans = 0;
            for(int i = 0 ; i < n ; i++) {
                if(rec[i] % 3 == 0) a++;
                else if(rec[i] % 3 == 1) b++;
                else c++;
            }
            ans += a;
            ans += min(b, c);
            b = b+c-2*min(b,c);
            ans += (b+2)/3;
            printf("%d\n", ans);
        } else {
            int a = 0, b = 0, c = 0, d = 0, ans = 0;
            for(int i = 0 ; i < n ; i++) {
                if(rec[i] % 4 == 0) a++;
                else if(rec[i] % 4 == 1) b++;
                else if(rec[i] % 4 == 2) c++;
                else d++;
            }
            ans += a;
            ans += min(b, d);
            b = b+d-2*min(b,d);
            c += b/2;
            ans += c/2;
            ans += ((b%2)+(c%2)) > 0 ? 1 : 0;
            printf("%d\n", ans);
        }
    }

    return 0;
}
