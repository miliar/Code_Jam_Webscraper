#include<bits/stdc++.h>
#define MX 10005
using namespace std;
typedef long long ll;

int main(){
     freopen("in1.in", "r", stdin);
     freopen("out1.txt", "w", stdout);
     string str;
     int i, j, k;
     int t, T, l, cnt;
     cin >> T;
     for(t=1; t<=T; ++t){
          cin >> str >> k;
          l=str.length();
          cnt=0;
          for(i=0; i<l-k+1; ++i){
               if(str[i]=='-'){
                    cnt++;
                    for(j=0; j<k; ++j) str[i+j]=(str[i+j]=='-')?'+':'-';
               }
          }
          for(; i<l; ++i) if(str[i]=='-') break;
          printf("Case #%d: ", t);
          if(i<l) printf("IMPOSSIBLE\n");
          else printf("%d\n", cnt);
     }
     return 0;
}

