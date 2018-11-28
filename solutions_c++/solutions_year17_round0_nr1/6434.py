#include<bits/stdc++.h>
using namespace std;

char str[1005];
int s[1005];
int main() {
  int t,k,len;
  freopen("out.txt","w",stdout);
  scanf("%d",&t);
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d: ",i);
    scanf("%s%d",str,&k);
    len = strlen(str);
    memset(s,-1,sizeof s);
    for (int i = 0; i < len; ++i) {
      if (str[i] == '-') s[i] = 1;
      else if (str[i] == '+') s[i] = 0;
    }
    queue<int>q;
    int num = 0,flag = 1;
    for (int i = 0; i < len; ++i) {
      while (!q.empty() && q.front() < i) q.pop();
      int sum = s[i] + q.size();
      if (sum & 1) {
        num++;
        if ((i + k - 1) >= len) {
          flag = 0;
          break;
        }
        q.push(i + k - 1);
      }
    }
    if (flag) {
      printf("%d\n",num);
    }
    else printf("IMPOSSIBLE\n");
  }
}
