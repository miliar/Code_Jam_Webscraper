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
    int N,Q;
    rs=sscanf(bf,"%d %d",&N,&Q);
    assert(rs==2);
    assert(Q==1);
    vector<double> vd;
    vector<double> vs;
    for(int i=0;i<N;i++) {
      fgets(bf,10000,stdin);
      int a,b;
      rs=sscanf(bf,"%d %d",&a,&b);
      assert(rs==2);
      vd.push_back(a);
      vs.push_back(b);
    }
    vector<int> vpos;
    vpos.resize(1);
    vpos[0]=0;
    for(int i=0;i<N;i++) {
      fgets(bf,10000,stdin);
      char *p=strtok(bf," \t");
      int rr=-1;
      int dd=0;
      int k=0;
      while(p) {
	if(atoi(p)>=0) {
	  dd=atoi(p);
	  assert(rr<0);
	  rr=k;
	}
	k++;
	p=strtok(NULL," \t");
      }
      if(i<N-1) {
	assert(rr>0);
	assert(rr==i+1);
	vpos.push_back(vpos[vpos.size()-1]+dd);
      }
    }

    {
      fgets(bf,10000,stdin);
      int aa,bb;
      rs=sscanf(bf,"%d %d",&aa,&bb);
      assert(rs==2);
      assert(aa==1);
      assert(bb==N);
    }

    vector<double> v;
    v.resize(N);
    for(int i=0;i<N;i++) {
      v[i]=9999999999999LL;
    }
    v[0]=0;
    for(int i=0;i<N;i++) {
      int dm=vd[i];
      for(int j=i+1;j<N;j++) {
	int d2=vpos[j]-vpos[i];
	if(d2>dm) break;
	double t2=v[i]+d2/vs[i];
	if(v[j]>t2)v[j]=t2;
      }
    }
    printf("Case #%d: %.7lf\n",tc,v[N-1]);
  }

  return 0;
}

