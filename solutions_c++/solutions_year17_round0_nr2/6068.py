#include <bits/stdc++.h>
using namespace std;
#define lli long long int
#define li long int
void solve(int tc) {
     char s[128];
     lli n, i;
     int k;
     cin >> s;
     n = strlen(s);
     int m = 1;
     int n1 = n;
     printf("Case #%d: ", tc );
     if(n == 1) {
          cout << s;
     }
     else  {
          while(m != 0) {
               m = 0;
               i = 0;
               while(i < n1 - 1) {
                    if(s[i] > s[i + 1]) {
                         s[i] = s[i] - 1;
                         m = 1;
                         for(int j = i + 1; j < n1; j++) {
                              s[j] = '9';
                         }
                         n1 = i + 1;
                         break;
                    }
                    i++;
               }
          }
          for(k = 0; k < n; k++) {
               if(s[k] != '0') {
                    break;
               }
          }
          if(k == n) {
               k = k - 1;
          }
          for(int i = k; i < n; i++) {
               printf("%c", s[i]);
          }
     }
     
     printf("\n");
}
int main() {
     int t;
     scanf("%d", &t);
     for(int i = 1; i <= t; i++) {
          solve(i);
     }
     return 0;
}