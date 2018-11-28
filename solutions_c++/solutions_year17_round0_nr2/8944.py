#include <iostream>
#include <string>

using namespace std;

int BeginOfFirstDrop(const string& N) {
  for (int i = 1; i < N.size(); ++i) {
    if (N[i] < N[i - 1]) return i - 1;
  }
  return -1;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    string N;
    cin >> N;
    int p = BeginOfFirstDrop(N);
    if (p != -1) {
	  int j = p;
	  while (j >= 0) {
		if (N[j] <= N[j + 1]) break;
		N[j] -= 1;
		--j;
	  }
      for (j = j + 2; j < N.size(); ++j) {
        N[j] = '9';
      }
    }
	p = 0;
	while (N[p] == '0') ++p;
	N = N.substr(p);
    cout << "Case #" << i + 1 << ": " << N << endl;
  }
  return 0;
}

/*
int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    string N;
    cin >> N;
    int p = BeginOfFirstDrop(N);
    while (BeginOfFirstDrop(N) != -1) {
		N = to_string(stoi(N) - 1);
	}
	cout << "Case #" << i + 1 << ": " << N << endl;
  }
  return 0;
}
*/