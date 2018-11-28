#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <string>
#include <set>
#include <deque>
#include <cctype>
#include <bitset>
#include <regex>

using namespace std;

#define For(i, n) for(int (i) = 0; (i) < (n); (i)++)

class Pair
{
public:
	long long a, b;
	Pair(long long _a, long long _b){
		a = _a;
		b = _b;
	}

	bool operator<(const Pair & that) const {
		bool r = false;
		if(b - a > that.b - that.a) r = true;
		else if(b - a == that.b - that.a && a < that.a) r = true;
		return !r;
	}
	
};

void solve(int T){
	long long n, k;

	cin >> n >> k;

	priority_queue<Pair> pq;
	pq.push(Pair(0, n+1));

	k--;
	while(k--){
		Pair p = pq.top();
		pq.pop();

	//	cout << "p = " << p.a << " " << p.b << endl;
		if(p.b == p.a + 1) continue;
		long long mid = (p.b + p.a) / 2;
	//	cout << "mid = " << mid << endl;
		pq.push(Pair(p.a, mid));
		pq.push(Pair(mid, p.b));
	}

	Pair p = pq.top();
	long long mid = (p.b + p.a) / 2;
//			cout << "p = " << p.a << " " << p.b << endl;

//	cout << "mid = " << mid << endl;

	cout << "Case #" <<  T + 1 << ": " << p.b - mid - 1 << " " << mid - p.a - 1<< endl;
}

int main(){
	int T;
	cin >> T;
	For(i, T) solve(i);
	return 0;
}