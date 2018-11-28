#include<iostream>
#include<vector>
#include<queue>
#include<utility>
#include<algorithm>
#include<iomanip>
#define PI 3.1415926535
using namespace std;

int main() {
  int T,N,P;
  cin>>T;
  for (int t=1;t<=T;t++) {
    cin>>N>>P;
    int packs=0;
    vector<int> ps(4,0);
    int gi;
    for (int i=0;i<N;i++){
      cin>>gi;
      ps[gi%P]++;
    }
    packs+=ps[0];
    if (P==2) {
      packs+=(ps[1]+1)/2;
    }
    if (P==3) {
      int a = min(ps[1],ps[2]);
      int b = max(ps[1],ps[2]);
      packs+=a+(b-a+2)/3;
    }
    if (P==4) {
      int a = min(ps[1], ps[3]);
      int b = max(ps[1], ps[3])-a;
      int c = ps[2];
      packs+=a;
      int d = min(c,b/2);
      packs+=d;
      b-=d*2;
      c-=d;
      packs+=c/2;
      c=c%2;
      packs+=b/4;
      b%=4;
      if (b || c) {
	packs++;
      }
    }
    cout<<"Case #"<<t<<": "<<packs<<endl;
  }
}
    
