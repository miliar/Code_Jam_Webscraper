#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <string>
#include <gmpxx.h>
#include <map>
#include <iostream>
using namespace std;

int main() {
  char bf[10000];
  fgets(bf,9999,stdin);
  int N;
  int sr=sscanf(bf,"%d",&N);
  assert(sr==1);
  for(int i=0;i<N;i++) {
    mpz_class n;cin>>n;
    mpz_class k;cin>>k;
    cerr<<n<<" "<<k<<endl;
    assert(k>0 && k<=n);
    map<mpz_class,mpz_class> mm;
    mm[n]=1;
    mpz_class r1=-1,r2=-1;
    while(k>0) {
      mpz_class ll;
      {
	map<mpz_class,mpz_class>::reverse_iterator it=mm.rbegin();
	assert(it!=mm.rend());
	ll=it->first;
	mpz_class kk=it->second;
	assert(kk>0);
	assert(ll>0);
	mpz_class ll1=(ll-1)/2;
	mpz_class ll2=(ll)/2;
	//cerr<<ll1<<" "<<ll2<<endl;
	r1=ll2;
	r2=ll1;
	assert(ll==ll1+ll2+1);
	if(kk<=k) {
	  k-=kk;
	  mm[ll]=0;
	  mm[ll1]+=kk;
	  mm[ll2]+=kk;
	} else {
	  k=0;
	  mm[ll]-=k;
	  mm[ll1]+=k;
	  mm[ll2]+=k;
	}
      }
      if(mm[ll]==0) mm.erase(ll);
    }
    cout<<"Case #"<<i+1<<": "<<r1<<" "<<r2<<endl;
  }
  return 0;
}
