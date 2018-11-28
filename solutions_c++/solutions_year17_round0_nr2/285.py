#include <bits/stdc++.h>
using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    char s[20];
    scanf("%s",s);
    printf("Case #%d: ",cs);
    int n=strlen(s);
    int g=n;
    for(int i=0;i+1<n;i++){
      if(s[i]>s[i+1]){
	g=i;
	break;
      }
    }
    if(g==n){
      for(int i=0;i<n;i++){
	putchar(s[i]);
      }
    }
    else{
      char c=s[g];
      while(g>0&&s[g-1]==c){
	g--;
      }
      for(int i=0;i<g;i++){
	putchar(s[i]);
      }
      if(g>0||c!='1'){
	putchar(c-1);
      }
      for(int i=g+1;i<n;i++){
	putchar('9');
      }
    }
    putchar('\n');
  }
  return 0;
}
