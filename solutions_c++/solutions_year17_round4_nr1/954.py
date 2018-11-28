#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int N, P, G;
    cin >> N >> P;
    vector<int> g(P,0);
    for (int i=0; i<N; i++) {
      cin >> G;
      g[ G % P]++;
    };
    long long answer = g[0];
    if (P==2) answer += ( g[1]+1 ) / 2;
    if (P==3) {
	int c = min(g[1],g[2]);
	g[1] -= c, g[2] -= c, answer += c;
	answer += (g[1]+2)/3;
	answer += (g[2]+2)/3;
      };
    if (P==4) {
	int c = min(g[1],g[3]);
	g[1] -= c, g[3] -= c, answer += c;
	c = g[2]/2;
	g[2] -= 2*c, answer += c;
	if (g[2]==0) {
	  answer += (g[1]+3)/4;
	  answer += (g[3]+3)/4;
	} else { // g[2] == 1
	  if (g[1]>0) // & g[3] =0 0
	    answer += (g[1]+5)/4;
	  else // g[1] == 0 && g[3]>0
	    answer += (g[3]+5)/4;
	}
      };
    cout << "Case #" << t << ": " << answer << endl;
  }
  return 0;
};
