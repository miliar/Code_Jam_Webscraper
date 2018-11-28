#include <string.h>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <functional>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstdio>
using namespace std;
#define sz(a)  int((a).size())
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define CLR(a) memset((a), 0, sizeof(a))
#define INF (1 << 31) - 1
const int dh[8] = {-1, 1, 0, 0,1,1,-1,-1};
const int dw[8] = {0, 0, 1, -1,1,-1,1,-1};
typedef long long ll;
typedef pair<int, int> p;
typedef vector <int> VI;
typedef vector <string> VS;

int main(){

	int n;
	cin >> n;
	
	for(int i = 1; i <= n; i++){
		double d;
		cin >> d;
		double nh;
		cin >> nh;
		
		double t = 0;
		for(int j = 0; j < nh ; j++){
			double p,s;
			cin >> p;
			cin >> s;
			
			t = max(t, (d - p) / s);
		}
		
		std::cout << std::fixed;
		cout << "Case #" << i << ": " << setprecision(6) << d / t << endl;
	}
	return 0;	
}
