#include <iostream>
#include <algorithm>

using namespace std;

int main() {

  int T;
  cin >> T;

  for(int t=1; t<=T; t++) {

    int N,C,M;
    cin >> N >> C >> M;

    int cust_counts[1005];
    int tick_counts[1005];

    for(int i=0; i<1005; i++) {
      cust_counts[i]=0;
      tick_counts[i]=0;
    }
    
    for(int i=0; i<M; i++) {
      int p,b;
      cin >> p >> b;
      cust_counts[b-1]++;
      tick_counts[p-1]++;
    }

    int max_cust=0;
    int max_tick=0;
    
    for(int i=0; i<C;i++) {
      max_cust=max(max_cust,cust_counts[i]);
    }
    int num_tick=0;
    for(int i=0; i<N; i++) {
      num_tick+=tick_counts[i];
      max_tick=max(max_tick,(num_tick+i)/(i+1));
    }
    int best=max(max_cust,max_tick);

    int promo=0;
    for(int i=0; i<N; i++) {
      promo+=max(0,tick_counts[i]-best);
    }
    cout << "Case #" << t <<": " << best << " " << promo <<endl;
  }
  return 0;
}
      
       
