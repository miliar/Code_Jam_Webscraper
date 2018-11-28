#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <limits>

using namespace std;

int main(){
	int t, count = 1;
	cin >> t;
	while(count <= t){
		int n;
		double d;
		cin >> d >> n;
		double maxTime = 0;
		for(int i = 0; i < n; ++i){
			double k, s;
			cin >> k >> s;
			double t = (d-k)/s;
			if(maxTime < t)
				maxTime = t;
		}

		double cruise = d/maxTime;

		cout.precision(6);
		cout << "Case #" << count << ": " << fixed << cruise << endl;
		count++;
	}
}