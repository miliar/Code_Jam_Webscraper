/*
  Task: bathroom stalls
  Category: 
  Sources:
file:///Volumes/ELIAS/SOI/Aufgaben_Sammlung/Tasks/template_de.pdf
file:///Volumes/ELIAS/SOI/Aufgaben_Sammlung/Tasks/template_en.pdf
file:///Volumes/ELIAS/SOI/Aufgaben_Sammlung/Tasks_Samples/template_samples.zip
*/

#include <iostream>
#include <queue>
#include <math.h>

#ifdef DEBUG
#  define DEB(x) cerr << "DEB: " << x << '\n'
#else
#  define DEB(x)
#endif

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  long long T;

  cin >> T;

  for (long long t = 0; t < T; ++t) {
    long long N;
    long long K;
    
    cin >> N >> K;

    priority_queue<pair<long long, long long> > pq;

    pq.push({N, 1});

    for (long long k = 0; k < K-1;) {
      long long space, count;
      tie(space, count) = pq.top();

      if (k+count >= K) {
	break;
      }
      
      pq.pop();

      --space;
      
      if (space%2 == 0) {
	pq.push({space/2, count * 2});
      } else {
	pq.push({ceil(space/2.0), count});
	pq.push({floor(space/2.0), count});
      }
      k+=count;
    }
    
    long long space, count;
    tie(space, count) = pq.top();

    --space;
    
    cout << "Case #" << t+1 << ": " << ceil(space/2.0) << " " << floor(space/2.0) << "\n";
  }
  
  return 0;
}
