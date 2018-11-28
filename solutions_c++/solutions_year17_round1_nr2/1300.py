#include<iostream>
#include<vector>
#include<queue>
#include<utility>

using namespace std;

int main() {
  int T,N,P;
  cin>>T;
  for (int t=1;t<=T;t++) {
    cin>>N>>P;
    vector<int> Ri(N);
    vector<vector<int> > Qij(N);
    for (int i=0;i<N;i++) {
      cin>>Ri[i];
      //      vector<int> tmp(P);
      //      Qij[i] = tmp;
    }
    priority_queue<pair<int, int> > Qadd;
    priority_queue<pair<int, int> > Qrem;
    int ing,ingmax,ingmin;
    for (int i=0;i<N;i++) {
      for (int j=0;j<P;j++) {
	cin>>ing;
	//Qij[i][j]=ing;
	ingmax=ing*10/9/Ri[i];
	ingmin=(ing*9+Ri[i]*10-1)/10/Ri[i];
	//	cout<<i<<' '<<j<<' '<<ingmax<<' '<<ingmin<<endl;
	if (ingmax<ingmin) continue;
	if (ingmax == 0) continue;
	Qadd.push(make_pair(ingmax, i));
	Qrem.push(make_pair(ingmin, i));
      }
    }
    vector<int> active(N,0);
    vector<int> used(N,0);
    int kits = 0;
    while(!Qadd.empty()) {
      pair<int, int> topadd = Qadd.top();
      pair<int, int> toprem = Qrem.top();
      if (toprem.first > topadd.first) {
	Qrem.pop();
	int remi = toprem.second;
	if (used[remi] > 0) {
	  used[remi]--;
	}
	active[remi]--;
	continue;
      }
      Qadd.pop();
      int addi = topadd.second;
      active[addi]++;
      int ok=1;
      for (int i=0;i<N;i++) {
	if (active[i]<=used[i]) {
	  ok = 0;
	  break;
	}
      }
      if (ok) {
	kits++;
	for (int i=0;i<N;i++) {
	  used[i]++;
	}
      }
    }
    cout<<"Case #"<<t<<": "<<kits<<endl;
  }
}
    
