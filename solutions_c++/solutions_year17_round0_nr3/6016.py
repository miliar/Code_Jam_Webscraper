#include <iostream>
#include <queue>

using namespace std;

string getLastStall(long long n, long long k) {
	if(n == k) return "0 0"; // short circuit just for performance

	priority_queue<long long> q;
	q.push(n);
	long long L;
	long long R;
	while(k--) {
		long long temp = q.top();
		q.pop();
		L = temp/2;
		R = (temp-1)/2;
		q.push(L);
		q.push(R);
		// cout << L << " " << R << endl;
	}
	return to_string(L) + " " + to_string(R);
}

int main() {
  int T;
  long long N, K;
  cin >> T; 
  // cout << getLastStall(9,9) << endl;
  for (int i = 1; i <= T; i++) {
    cin >> N >> K;
    cout << "Case #" << i << ": " << getLastStall(N, K) << endl;
  }
  return 0;
}