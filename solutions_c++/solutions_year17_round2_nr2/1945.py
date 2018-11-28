#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define min3(x, y, z) x > y ? (y > z ? z : y) : (x > z? z: x)
#define max3(x, y, z) x < y ? (y < z ? z : y) : (x < z? z: x)
#define abs(x) x >= 0 ? x : -x

using namespace std;
typedef long long int ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef pair<int, int> PI;
const ll mod = 1e9 + 7;

int main(void){
ll T;
  cin >> T;
  REP(t, 1, T+1)
    {
      bool impossible = false;
      int N;
      cin >> N;
      int R, O, Y, G, B, V;
      cin >> R >> O >> Y>>G>>B>>V;
      int n1, n2, n3;
      char c1, c2, c3;
      priority_queue<pair<int, char> >pq;
      pq.push(pair<int, char>(R, 'R'));
      pq.push(pair<int, char>(Y, 'Y'));
      pq.push(pair<int, char>(B, 'B'));
      pair<int, char> p1 = pq.top();
      pq.pop();
      n1 = p1.first;
      c1= p1.second;
      pair<int, char> p2 = pq.top();
      pq.pop();
      n2 = p2.first;
      c2= p2.second;
      pair<int, char> p3 = pq.top();
      pq.pop();
      n3 = p3.first;
      c3= p3.second;
      cout << "Case #"<<t<<": ";
      string pattern = "";
      if (n1 > n2 + n3)
	impossible = true;
      else
	{
	  REP(i, 0, n1)
	    {
	      pattern += c1;
	      if (i < n2)
		pattern += c2;
	      if (i >= n1 - n3)
		pattern += c3;
	    }
	}
      if (impossible)
	cout << "IMPOSSIBLE";
      else
	cout << pattern;
      cout<<endl;
    }
}
