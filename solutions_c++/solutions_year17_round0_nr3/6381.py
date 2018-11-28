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

using namespace std;

typedef long long ll;

struct range{
	ll left, right;
	range(ll l, ll r) : left(l), right(r){}

	ll value() const {
		return right - left - 1;
	}

	void print(ostream& out) const {
		out << left << " " << right << endl;
	}
};

struct comparator{
	bool operator()(const range& a, const range& b){
		if(a.value() < b.value())
			return true;
		if(a.value() == b.value())
			return a.left < b.left;
		return false;
	}
};

int main(){
	int t, count = 1;
	cin >> t;
	while(count <= t){
		
		ll n, k;
		cin >> n >> k;

		set<range, comparator> occupied;
		occupied.insert(range(0, n+1));

		ll next = -1;
		range *nextl = NULL, *nextr = NULL;
		for(int i = 0; i < k; ++i){
			range mRange = *occupied.rbegin();
			ll l = mRange.left;
			ll r = mRange.right;
			ll maxRange = mRange.value();
			next = (maxRange%2 == 0) ? l + maxRange/2 : l + maxRange/2 + 1;
			//cout << "erasing " << occupied.size() << endl;
			occupied.erase(mRange);
			//cout << "after erasing " << occupied.size() << endl;
			nextl = new range(next, r);
			nextr = new range(l, next);	
			//cout << "adding " << occupied.size() << endl;
			occupied.insert(*nextl);
			occupied.insert(*nextr);
			//cout << "after adding " << occupied.size() << endl;
		}

		ll ls = nextr->value();
		ll rs = nextl->value();

		ll y = max(ls, rs);
		ll z = min(ls, rs);

		cout << "Case #" << count << ": " << y << " " << z << endl;
		count++;
	}
}