#include <bits/stdc++.h>
using namespace std;

int main()
{
  int t;
  scanf("%d",&t);
  for(int cs=1;cs<=t;cs++){
    char s[1010];
    int k;
    scanf("%s%d",s,&k);
    int n=strlen(s);
    bool B[1010];
    for(int i=0;i<n;i++){
      B[i]=(s[i]=='+');
    }
    int C=0;
    for(int i=0;i<=n-k;i++){
      if(!B[i]){
	C++;
	for(int j=0;j<k;j++){
	  B[i+j]^=1;
	}
      }
    }
    bool F=0;
    for(int i=n-k+1;i<n;i++){
      if(!B[i]){
	F=1;
	break;
      }
    }
    printf("Case #%d: ",cs);
    if(F){
      printf("IMPOSSIBLE\n");
    }
    else{
      printf("%d\n",C);
    }
  }
  return 0;
}
