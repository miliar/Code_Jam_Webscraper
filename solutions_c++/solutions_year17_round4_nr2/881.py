#include <iostream>
#include <algorithm>

using namespace std;

int Tickets[1000][1000],row_sum[1000];

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int N, C, M;
    cin >> N >> C >> M;
    for (int i=0; i<M; i++) {
      row_sum[i]=0;
      for (int j=0; j<C; j++)
	Tickets[i][j]=0;

    }
    for (int i=0; i<M; i++) {
      int P, B;
      cin >> P >> B;
      Tickets[--P][--B]++,row_sum[B]++;
    }
    
    if (C==2) {
      int rides = 0, promotions = 0;

      rides = max(max(row_sum[0],row_sum[1]),Tickets[0][0]+Tickets[0][1]);
      for (int i=0; i<N; i++)
	promotions += max(0, Tickets[i][0]+Tickets[i][1] - rides);
      
      cout << "Case #" << t << ": " << rides << " " << promotions << endl;
    }
    else
      cout << "I give up!" << endl;
  }
  return 0;
};
