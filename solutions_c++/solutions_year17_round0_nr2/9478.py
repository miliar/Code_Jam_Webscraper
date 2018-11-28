#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <climits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <tuple>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long> vl;

#define ten(n) (1e##n)
#define COUT cout <<
#define SPACE_COUT << " "  <<
#define COMMA_COUT << ", " <<
#define ENDL << endl;

int
main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
      string s;
      cin >> s;
      if (s.size() > 1) {
	int reverse = -1;
	for (int i = 1; i < s.size(); ++i) {
	  if (s[i-1] <= s[i]) continue;
	    
	  reverse = i - 1;
	}

	if (reverse >= 0) {
	  int rewrite_index = 0;
	  for (int i = reverse; i > 0; i--) {
	    if ((s[i] - s[i-1]) > 0) {
	      rewrite_index = i;
	      break;
	    }	    
	  }
	  
	  if (rewrite_index == 0 && s[rewrite_index] == '1') {
	    for (int i = 0; i < s.size(); ++i) s[i] = '9';
	    s.pop_back();
	  } else {
	    s[rewrite_index] = ((s[rewrite_index] - '0') - 1) + '0';
	    for (int i = rewrite_index+1; i < s.size(); ++i) {
	      s[i] = '9';
	    }	   
	  }	  
	}
      } 
      printf("Case #%d: %s\n", t, s.c_str());
    }

    return 0;
}
