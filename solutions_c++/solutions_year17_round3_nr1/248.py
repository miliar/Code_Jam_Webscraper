#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <math.h>
#include <iostream>
#include <tuple>
//#include <gmpxx.h>

typedef long long ll_t;

using namespace std;

int main() {
  char bf[10000];
  fgets(bf,10000,stdin);
  int ntc;
  int rs=sscanf(bf,"%d",&ntc);
  assert(rs==1);
  for(int tc=1;tc<=ntc;tc++) {
    int k,n;
    fgets(bf,10000,stdin);      
    rs=sscanf(bf,"%d %d",&n,&k);
    //fprintf(stderr,"n=%d k=%d\n",n,k);
    assert(rs==2);
    set<int> rads;
    multiset<pair<ll_t,ll_t> > mm;
    for(int i=0;i<n;i++) {
      fgets(bf,10000,stdin);
      int rad,h;
      rs=sscanf(bf,"%d %d",&rad,&h);
      assert(rs==2);
      //printf("%d %d\n",rad,h);
      mm.insert(make_pair(-ll_t(h)*rad,rad));
      rads.insert(rad);
    }
    double r=0;
    for(auto &rad:rads) {
      //printf("R %d\n",rad);
      ll_t mmx=0;
      auto it=mm.begin();
      for(;it!=mm.end();++it) {
	if(it->second!=rad) continue;
	mmx=-it->first;
	break;
      }
      assert(it!=mm.end());

      int l=1;
      if(k>1) {
	auto jt=mm.begin();
	for(;jt!=mm.end();++jt) {
	  if(it==jt) continue;
	  if(jt->second>rad) {continue;}
	  mmx+=-jt->first;
	  l++;
	  if(l==k) break;
	}
      }
      if(l==k) {
	double rr=M_PI*rad*rad+mmx*M_PI*2;
	//fprintf(stderr,"AA %d %d %Ld %f\n",rad,l,mmx,r);
	if(r<rr) r=rr;
      }
    }
    printf("Case #%d: %.7lf\n",tc,r);
    //cout<<"Case #"<<tc<<": ";    cout<<r<<endl;
  }

  return 0;
}
