#include <iostream>
#include <fstream>
#include <queue>

#define MIN(A,B) ((A<B)?A:B)
#define MAX(A,B) ((A>B)?A:B)

using namespace std;

int main(){
	ifstream infile;
	ofstream outfile;
	infile.open("input.txt");
	outfile.open("output.txt");
	int T, N, K, min, max, tmp, L, R;
	infile >> T;
	for (int j = 0; j<T; j++) {
    // cout << j+1 << endl;
    infile >> N >> K;
    priority_queue<unsigned long long> pq;
    pq.push(N);
    min = N; max = 0; tmp = 0;
    while(K){
      tmp = pq.top();
      pq.pop();
      R = tmp/2;
      L = (tmp % 2) ? tmp / 2 : tmp / 2 - 1;
      pq.push(R);
      pq.push(L);
      min = MIN(L,R);
      max = MAX(L,R);
      // cout << tmp << " " << L << " " << R << " min " << min << endl;
      K--;
    }
    outfile << "Case #" << j+1 <<": "<<max<<" "<<min<<endl;
  }
	infile.close();
	outfile.close();
}
