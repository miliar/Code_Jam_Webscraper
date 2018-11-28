#include <iostream>
#include <algorithm>
#include <string>
#include <deque>

using namespace std;
using Pancake = pair<size_t, size_t>;
using Stack = deque<Pancake>;


void process(const int K, Stack& stack) {
	sort(stack.begin(), stack.end(), [] (const Pancake& l , const Pancake& r) {
		return l.second*l.first > r.first*r.second;
	});
	size_t max = 0;
	for (size_t j = 0; j < stack.size() ; ++j) {
		Pancake& p = stack[j];
		size_t total =2*p.first*p.second;
		size_t R = p.first;
		Stack s = stack;
		s.erase(s.begin()+j);
		remove_if(s.begin(), s.end(), [&p] (const Pancake& pancake) {
			return pancake.first < p.first;
		});
		for (size_t i = 0; i < K-1; ++i) {
			R = std::max(R, s[i].first); 
			total += 2*s[i].first*s[i].second;
		}
		total += R*R;
		if (total > max) max = total;
	}
	double d = 3.14159265359;
	d *= max;
	cout << to_string(d) << endl;
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
	try {
		size_t N, K, R, H;
		cin >> N >> K;
		Stack stack;
		stack.resize(N);
		for (size_t i = 0; i < N; ++i) {
			cin >> R >> H;
			stack[i] = make_pair(R, H);
		}		
		cout << "Case #" << inputNumber << ": ";
		process(K, stack);
		} catch (...) {}
	}
	return 0;
}
