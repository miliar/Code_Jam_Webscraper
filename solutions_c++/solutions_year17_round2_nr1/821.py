#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <tuple>
#include <gmpxx.h>

typedef long long ll_t;

using namespace std;

int main() {
  char bf[10000];
  fgets(bf,10000,stdin);
  int ntc;
  int rs=sscanf(bf,"%d",&ntc);
  assert(rs==1);
  for(int tc=1;tc<=ntc;tc++) {
    fgets(bf,10000,stdin);
    int d,n;
    rs=sscanf(bf,"%d %d",&d,&n);
    assert(rs==2);
    
    double ma=-1;
    for(int i=0;i<n;i++) {
      fgets(bf,10000,stdin);
      int si,ki;
      rs=sscanf(bf,"%d %d",&ki,&si);
      assert(rs==2);
      double r=double(d-ki)/si;
      //cout<<r<<" " <<d/r<<endl;
      if(i==0 || ma>d/r) ma=d/r;
    }
    printf("Case #%d: %.7lf\n",tc,ma);
  }

  return 0;
}
