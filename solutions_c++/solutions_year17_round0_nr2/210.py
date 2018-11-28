#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <string>
using namespace std;

int l;
char w[100];
char p[10000];
string r;

bool rec(int i=0,bool xx=1) {
  w[i]=0;
  int min='0';
  if(i) min=w[i-1];
  if(i==l) {
    r=w;
    return 1;
  }
  
  int max='9';
  if(xx) max=p[i];
  fprintf(stderr,"%s %c %c\n",w,max,min);
  bool xx2=xx;
  for(int k=max;k>=min;k--) {
    w[i]=k;
    if(rec(i+1,xx2)) return 1;
    xx2=0;
  }
  return 0;
}
  

int main() {
  char bf[10000];
  fgets(bf,9999,stdin);
  int N;
  int sr=sscanf(bf,"%d",&N);
  assert(sr==1);
  for(int i=0;i<N;i++) {
    fgets(bf,9999,stdin);
    sr=sscanf(bf,"%s",p);
    assert(sr==1);
    l=strlen(p);
    assert(l<20);
    
    fprintf(stderr, "%d: l=%d %s\n",i+1,l,p);
    int rr=rec();
    assert(rr);
    fprintf(stderr, "%d: l=%d %s\n",i+1,l,r.c_str());
    int pp=0;
    while(r.c_str()[pp]=='0') pp++;
    if(r.c_str()[pp]==0) pp--;
    fprintf(stderr, "%d: l=%d %s\n",i+1,l,r.c_str()+pp);

    printf("Case #%d: %s\n",i+1,r.c_str()+pp);
  }

}
