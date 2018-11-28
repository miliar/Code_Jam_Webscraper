#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>

using namespace std;

pair<long long, long long> solve(long long n, long long k) {
	multiset<long long> segments;
	pair<long long, long long> answer;
	segments.insert(n);
	for (int i = 0; i < k; ++i) {
		long long segment = *segments.rbegin();
		auto ptr = segments.find(segment);		
		segments.erase(ptr);
		if (segment > 2) {
			long long l = (segment - 1) / 2;
			long long r = segment - 1 - l;
			segments.insert(l);
			segments.insert(r);
			answer.first = r;
			answer.second = l;
		}
		else if (segment == 2) {
			segments.insert(1);
			answer.first = 1;
			answer.second = 0;
		}
		else {
			answer.first = 0;
			answer.second = 0;
		}
	}
	return answer;
}

int main(int argc, char* argv[])
{
	srand(13);
	ios_base::sync_with_stdio(false);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		long long n, k;
		cin >> n >> k;

		auto answer = solve(n, k);
		cout << "Case #" << test << ": " << answer.first << ' ' << answer.second << '\n';
	}

	return 0;
}

