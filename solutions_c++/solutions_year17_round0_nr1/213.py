#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

int main() {
  char bf[10000];
  char p[10000];
  fgets(bf,9999,stdin);
  int N;
  int sr=sscanf(bf,"%d",&N);
  assert(sr==1);
  for(int i=0;i<N;i++) {
    fgets(bf,9999,stdin);
    int k;
    sr=sscanf(bf,"%s %d",p,&k);
    assert(sr==2);
    int l=strlen(p);
    assert(l<1100);
    int r=0;
    for(int u=0;u<=l-k;u++)
      if(p[u]=='-') {
	r++;
	for(int j=0;j<k;j++)
	  if(p[u+j]=='-') p[u+j]='+';
	  else p[u+j]='-';
      }
    for(int u=l-k;u<l;u++)
      if(p[u]=='-') {
	r=-1;
      }
    fprintf(stderr, "%d: l=%d k=%d r=%d %s\n",i+1,l,k,r,p);
    if(r<0)
      printf("Case #%d: IMPOSSIBLE\n",i+1);
    else
      printf("Case #%d: %d\n",i+1,r);
  }

}
