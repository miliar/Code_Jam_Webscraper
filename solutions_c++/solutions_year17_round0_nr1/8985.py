#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;

int solve(vector<bool> bits, int N) {
  queue<int> flips;
  int moves = 0;

  for (int i = 0; i < bits.size(); ++i) {
    if (!flips.empty() && flips.front() <= i - N)
      flips.pop();

    if ((bits[i] ^ (flips.size() % 2 == 0)) == 1) {
      if (i > bits.size() - N)
        return -1; // IMPOSSIBLE

      moves++;
      flips.push(i);
    } 
  }

  return moves;
}

int a, i, s, ans;
string f;
int main() {
	i = 0;
	cin >> a;
	while(a--) {
		cin >> f >> s;		
		vector<bool> v;
		for(auto e: f) {
			if(e == '+') v.push_back(1);
			else v.push_back(0);
		}
		printf("Case #%d: ",++i);
		ans = solve(v, s);
		if(ans == -1) puts("IMPOSSIBLE");
		else cout << ans << endl;
	}
	return 0;
}
