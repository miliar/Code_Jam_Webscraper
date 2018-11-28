#include <iostream>
#include <queue>
#include <iomanip>

using namespace std;

int N;

long long roads[110][110];
double one_way[110][110];

double horses[110][2]; // distance, speed


void update(int s) {
  // update one_way_dist[s][i];
  for(int i=0; i<N; i++) {
    one_way[s][i]=-1;
  }
  priority_queue<pair<long long, long long> > q;
  q.push(make_pair(-0,s));

  while (!q.empty()) {
    pair<long long,long long> now = q.top();
    q.pop();
    if (one_way[s][now.second]>-.5) {
      continue;
    }
    one_way[s][now.second]=-now.first/horses[s][1];
    for(int i=0; i<N; i++) {
      if (one_way[s][i]<-.5
	  && roads[now.second][i]>=0
	  && (-now.first+roads[now.second][i]<=horses[s][0])) {
	q.push(make_pair(-(-now.first+roads[now.second][i]),i));
      }
    }
  }

  /*  cout << s << " to all: ";
  for(int i=0; i<N; i++)
    cout << " " << one_way[s][i];
    cout << endl;*/
  
}
	
void floyd() {
  for(int k=0; k<N; k++) {
    for(int i=0; i<N; i++) {
      for(int j=0; j<N; j++) {
	if (i==j || i==k || j==k)
	  continue;
	if (one_way[i][k]<0 || one_way[k][j]<0)
	  continue;
	if (one_way[i][j]<0 || one_way[i][j]>one_way[i][k]+one_way[k][j]) {
	  one_way[i][j]=one_way[i][k]+one_way[k][j];
	}
      }
    }
  }
  /*  cout << "New Grid:" << endl;
  for(int i=0; i<N; i++) {
    for(int j=0; j<N; j++) {
      cout << one_way[i][j] << " ";
    }
    cout << endl;
    }*/
}
	 




int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++) {
    cin >> N;
    int Q;
    cin >> Q;
    for(int i=0; i<N; i++) {
      cin >> horses[i][0] >> horses[i][1];
    }

    for(int i=0; i<N; i++) {
      for(int j=0; j<N; j++) {
	cin >> roads[i][j];
	one_way[i][j]=-1;
      }
    }

    for(int i=0; i<N; i++) {
      update(i);
    }
  
    floyd();

    cout << "Case #" << t <<":";
    for(int i=0; i<Q; i++) {
      int U,V;
      cin >> U >> V;
      cout << " " << setprecision(9) << one_way[U-1][V-1];
    }
    cout << endl;
  }
  return 0;
}
  
