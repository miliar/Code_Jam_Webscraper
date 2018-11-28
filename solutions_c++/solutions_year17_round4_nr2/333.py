#include<iostream>
#include<vector>
#include<queue>
#include<utility>
#include<algorithm>
#include<iomanip>
#define PI 3.1415926535
using namespace std;

int main() {
  int T,N,C,M;
  cin>>T;
  for (int t=1;t<=T;t++) {
    cin>>N>>C>>M;
    vector<int> custrides(C,0);
    int maxcust=0;
    vector<int> customers(N,0);
    int a,b;
    for (int i=0;i<M;i++) {
      cin>>a>>b;
      a--;b--;
      customers[a]++;
      custrides[b]++;
      maxcust = max(maxcust,custrides[b]);
    }
    int minrides = M;
    int minpromo = 0;
    for (int r=maxcust;r<=M;r++) {
      int free = 0;
      int promo = 0;
      int ok=1;
      for (int j=0;j<N;j++) {
	free+=r;
	free-=customers[j];
	promo+=max(0,customers[j]-r);
	if (free<0) {
	  ok=0;
	  break;
	}
      }
      if (ok) {
	cout<<"Case #"<<t<<": "<<r<<' '<<promo<<endl;
	break;
      }
    }
  }
}
    
