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
//#include <gmpxx.h>

typedef long long ll_t;

using namespace std;

double score(vector<double> &r,vector<double> &r2)
{
  
  return 0;
}

int main() {
  char bf[10000];
  fgets(bf,10000,stdin);
  int ntc;
  int rs=sscanf(bf,"%d",&ntc);
  assert(rs==1);
  for(int tc=1;tc<=ntc;tc++) {
    int n,k;
    cin>>n;
    cin>>k;
    double u;
    cin>>u;
    multiset<double> R;
    vector<double> r(n);
    for(int i=0;i<n;i++) {
      cin>>r[i];
      R.insert(-r[i]);
    }

    R.insert(-1);
    if(k==n) {
      double bpr=0;
      for(auto it=R.begin();it!=R.end();it++) {
	double tt=0,ttr=0;
	auto b=-*it;
	int k=0;
	for(auto jt=it;jt!=R.end();jt++) {
	  auto a=-*jt;
	  ttr+=a;
	  tt+=b-a;
	  k++;
	}
	double m=u+ttr;
	m/=k;
	double pr=1;
	bool um=0;
	//printf("%lf %lf\n",b,m);
	if(m<b-0.000000001) continue;
	for(auto jt=R.begin();jt!=R.end();jt++) {
	  if(jt==it) um=1;
	  if(um==0) pr*=-*jt;
	  else pr*=m;
	}
	if(pr>bpr) bpr=pr;
      }

      printf("Case #%d: %.7lf\n",tc,bpr);
    }
    /*
    vector<double> r2(n);
    double l=u;
    for(int i=0;i<n;i++) {
      double x=1-r[i];
      if(x<l) r2[i]=x;
      l-=r2[l];
    }
    */
      
    //cout<<"Case #"<<tc<<":";    cout<<endl;
  }

  return 0;
}
