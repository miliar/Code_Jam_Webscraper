#include<iostream>
#include<queue>
#include<map>

using namespace std;
int main() {
  int T;
  long long N;
  long long K;
  cin>>T;
  for (int t=1;t<=T;t++) {
    cin>>N>>K;
    map<long long, int> counts;
    priority_queue<long long> Q;
    Q.push(N);
    counts[N]=1;
    while(K>0) {
      long long curN = Q.top();
      Q.pop();
      //      cout<<curN<<' '<<K<<' '<<Q.size()<<endl;
      if (counts[curN] >=K) {
	cout<<"Case #"<<t<<": "<<curN/2<<' '<<(curN-1)/2<<endl;
	break;
      }
      K-=counts[curN];
      if (counts.find(curN/2) == counts.end()) {
	counts[curN/2]=0;
	Q.push(curN/2);
      }
      if (counts.find((curN-1)/2) == counts.end()) {
	counts[(curN-1)/2]=0;
	Q.push((curN-1)/2);
      }
      counts[curN/2]+=counts[curN];
      counts[(curN-1)/2]+=counts[curN];
    }    
  }
}
