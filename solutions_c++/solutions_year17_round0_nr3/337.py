#include <iostream> 
using namespace std;

void solve_case(int T){
	long long int N, K, power = 1, size, num;
	cin >> N;
  cin >> K;

  while (power <= K){
    power *= 2;
  }
  power = power/2;

  size = (N - power + 1)/power;
  num = N - power + 1 - size * power;
  if (K - power + 1 > num){
    cout << "Case #" << T << ": " << (size - 1) - (size - 1)/2 << " " << (size - 1)/2 << endl;
  } else {
    cout << "Case #" << T << ": " << size - size/2 << " " << size/2 << endl;
  }
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  	solve_case(i);
  	}
  	return 0;
}