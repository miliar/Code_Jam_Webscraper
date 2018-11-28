// problemC.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Interval {
	int64_t length;
	int64_t count;

	Interval(int64_t length, int64_t count) : length(length), count(count) {}
};

struct CompareInterval {
	bool operator()(Interval& a, Interval& b) { return a.length < b.length; }
};

class MyQueue : public priority_queue<Interval, vector<Interval>, CompareInterval>
{
public:
	typedef priority_queue<Interval, vector<Interval>, CompareInterval>::container_type::iterator iterator;

	iterator end() { return this->c.end(); }
	iterator find(int64_t length)
	{
		auto first = this->c.begin();
		auto last = this->c.end();
		while (first != last) {
			if (first->length == length) return first;
			++first;
		}
		return last;
	}
};

static void add(MyQueue& pq, Interval interval)
{
	auto element = pq.find(interval.length);
	if (element == pq.end()) {
		pq.push(interval);
	}
	else {
		element->count += interval.count;
	}
}

void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int64_t n;
		int64_t k;
		cin >> n >> k;
		MyQueue pq;
		pq.push(Interval(n, 1));
		int64_t result_min = 0;
		int64_t result_max = 0;
		while (k > 0) {
			Interval largeInterval = pq.top();
			pq.pop();
			k -= largeInterval.count;
			result_max = largeInterval.length / 2;
			result_min = largeInterval.length - 1 - result_max;
			if (k <= 0) {
				break;
			}
			if (result_min == result_max) {
				add(pq, Interval( result_min, largeInterval.count * 2 ));
			} else {
				add(pq, Interval( result_max, largeInterval.count ) );
				add(pq, Interval( result_min, largeInterval.count ) );
			}
		}
		cout << "Case #" << i << ": " << result_max << " " << result_min << endl;
	}
}