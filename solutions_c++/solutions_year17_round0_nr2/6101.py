#include <iostream>
#include <algorithm>

using namespace std;

string getTidyNumber(string s) {
	string sCopy = s;
	sort(sCopy.begin(), sCopy.end());

	if(sCopy == s) return s;

	int max = -1;
	int maxIndex = -1;

	int minNum = 9;
	
	int len = s.size();
	for(int i = len - 1; i >= 0; i--) {
		int num = s[i] - '0';
		if(num < minNum) {
			minNum = num;
			max = num;
		} else if(num >= max) {
			max = num;
			maxIndex = i;
		}
	}

	s[maxIndex] = s[maxIndex] == '0' ? '9': s[maxIndex] - 1;
	for(int i = maxIndex + 1; i < len; i++) {
		s[i] = '9';
	}
	int indFirstNonZero = s.find_first_not_of('0');
	s.erase(0, min(indFirstNonZero, len-1));
	
	return s;
}

int main() {
  int T;
  string N;
  cin >> T; 
  // cout << getTidyNumber("649") << endl;
  for (int i = 1; i <= T; i++) {
    cin >> N;
    cout << "Case #" << i << ": " << getTidyNumber(N) << endl;
  }
  return 0;
}