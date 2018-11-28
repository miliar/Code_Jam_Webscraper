#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main() {
  int t;
  scanf("%d\n", &t);
  for (int i = 1; i <= t; ++i) {
  	int count = 0;
  	string s = "";
  	char temp;

  	scanf("%c ", &temp);
  	while (temp == '+' || temp == '-') {
  		if (temp == '+') s+= '1';
  		else s+= '0';
  		scanf("%c", &temp);
  	}
  	int k;
  	scanf("%d\n", &k);
  	int len = s.size();

  	// cout << s << endl;
  	for (int j = 0; j < len - k + 1; j++) {
  		if (s[j] == '0') {
  			count ++;
  			for (int a1 = 0; a1 < k; a1++) {
  				if (s[a1+j] == '1') s[a1+j] = '0';
  				else s[a1+j] = '1';
  				// cout << s << endl;
  			}
  		}
  	}
  	for (int j = len-k; j < len; j++) {
  		if (s[j] == '0') {
  			count = -1;
  		}
  	}

  	if (count == -1)
  		cout << "Case #" << i << ": IMPOSSIBLE" << endl;
  	else
  		cout << "Case #" << i << ": " << count << endl;
  }
  return 0;
}