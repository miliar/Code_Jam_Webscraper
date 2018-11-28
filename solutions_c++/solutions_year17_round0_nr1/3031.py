#include <iostream>
#include <string>

using namespace std;

bool flipped[1500];

int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    string s;
    cin >> s;
    int k;
    cin >> k;
    for(int i=0; i<s.length(); i++) {
      flipped[i]=(s.at(i)=='+');
    }
    int num=0;
    for(int i=0; i<=s.length()-k; i++) {
      if (!flipped[i]) {
	for(int j=i; j<i+k; j++) {
	  flipped[j] = !flipped[j];
	}
	num++;
      }
    }
    bool all_good=true;
    for(int i=0; i<s.length(); i++) {
      all_good = all_good && flipped[i];
    }
    if (all_good) {
      cout << num << endl;
    }
    else
      cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}
      

    
    
