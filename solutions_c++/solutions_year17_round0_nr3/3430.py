#include <iostream>
#include <utility>
#include <queue>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		long long N;
		long long K;
		cin >> N >> K;

		priority_queue< pair< long long, long long> > used;
		used.push(make_pair(N+1, 0));

		long long next_min = 0;
		long long next_max = 0;

		for (int j = 0; j < K; ++j)
		{
			next_min = -1;
			next_max = -1;

			pair< long long, long long> best = used.top();

			long long k = (best.first / 2) - best.second;
			long long ls = k + best.second;
			long long rs = best.first - best.second - k;
			
			next_min = min(ls, rs);
			next_max = max(ls, rs);

			used.pop();
			used.push(make_pair(ls, best.second));
			used.push(make_pair(rs, -k));
		}

		cout << "Case #" << i << ": " << (next_max - 1) << " " << (next_min - 1) << endl;
	}
	return 0;
}