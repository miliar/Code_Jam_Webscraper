#include <iostream>
#include <queue>

using namespace std;

typedef long long ll;

struct Range
{
  // inclusive
  ll from;
  // exclusive
  ll to;

  Range(ll from, ll to)
	: from(from)
	, to(to){}
  
  ll size() {
	return to - from;
  }
};

int main()
{
  int T;
  cin >> T;

  for(int t = 1; t <= T; t++)
  {
	ll n, k;
	cin >> n >> k;

	auto cmp = [](Range r1, Range r2) {
	  if(r1.size() != r2.size()) {
		return r1.size() < r2.size();
	  } else {
		return r1.from > r2.from;
	  }
	};
	
	priority_queue<Range, vector<Range>, decltype(cmp)> que(cmp);

	que.push(Range(1, n + 1));

	ll l = -1;
	ll r = -1;
	
	for(int i = 0; i < k; i++)
	{
	  auto range = que.top();
	  que.pop();

	  ll selected = range.from + (range.to - range.from - 1) / 2;

	  if(range.size() >= 3)
	  {
		que.push(Range(range.from, selected));
		l = selected - range.from;
	  }
	  else
	  {
		l = 0;
	  }
	  que.push(Range(selected + 1, range.to));
	  r = range.to - selected - 1;
	}
	cout << "Case #" << t << ": " << max(l, r) << " " << min(l, r) << endl;
  }
}
