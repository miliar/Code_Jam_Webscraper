#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;


const int N = 1005;
int R, O, Y, G, B, V, n, a[3], b[3];
int c[3];
char s[N];
char mp[N];

int main() {
    int T;

    freopen("out2.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
       scanf("%d%d%d%d%d%d%d", &n, a + 0, c + 0, a + 2, c + 1, a + 1, c + 2) ;
       printf("Case #%d: ", cas + 1);
       if(a[0] + c[1] == n && a[0] == c[1]) {
           For(i, n) {
               if(i & 1) printf("R");
               else printf("G");
           }
           puts("");
           continue;
       }
       else if(a[1] + c[0] == n && a[1] == c[0]) {
            For(i, n) {
                if(i & 1) printf("B");
                else printf("O");
            }
            puts("");
            continue;
        }
       else if(a[2] + c[2] == n && a[2] == c[2]) {
            For(i, n) {
                if(i & 1) printf("Y");
                else printf("V");
            }
            puts("");
            continue;
        }


       bool fail = 0;
       For(i, 3) b[i] = a[i];
       b[0] -= c[1];
       b[1] -= c[0];
       b[2] -= c[2];
       For(i, 3) if(b[i] < 0) fail = 1;
       //printf("%d %d %d\n", b[0], b[1], b[2]);

       mp[0] = 'R';
       mp[1] = 'B';
       mp[2] = 'Y';
       int i = 0;
       int p = -1;
       while(i < n) {
           int mx = -1;
           For(j, 3) {
               if(j == p) continue;
               if(mx == -1 || b[j] > b[mx] || b[j] == b[mx] && i && s[0] == mp[j]) mx = j;
           }
           b[mx]--;
           if(b[mx] < 0) fail = 1;
           if(fail) break;

           p = mx;
           if(mx == 0) {
               if(c[1]) {
                   c[1]--;
                   s[i++] = 'R', s[i++] = 'G', s[i++] = 'R';
               }
               else s[i++] = 'R';
           }
           if(mx == 1) {
               if(c[0]) {
                   c[0]--;
                   s[i++] = 'B', s[i++] = 'O', s[i++] = 'B';
               }
               else s[i++] = 'B';
           }
           if(mx == 2) {
               if(c[2]) {
                   c[2]--;
                   s[i++] = 'Y', s[i++] = 'V', s[i++] = 'Y';
               }
               else s[i++] = 'Y';
           }
           //printf("mx = %d\n", mx);

       }
       s[i++] = 0;
       if(s[0] == s[n - 1]) fail = 1;
       if(fail) {
           puts("IMPOSSIBLE");
           cerr << a[0] << " " << a[1] << " " << a[2] << "\n";
       }
       else puts(s);
    }
	return 0;
}
