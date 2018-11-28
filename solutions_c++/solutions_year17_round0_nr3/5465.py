#include <iostream>
#include <queue>

#define MAX(a, b) (a < b ? b : a)
#define MIN(a, b) (a < b ? a : b)
#define N 1000

using namespace std;

class aside {
public:
	int max, min;
	aside() : max(0), min(0) {}
	aside(int n) {
		if (n % 2 == 0) {
			this->max = n / 2;
			this->min = n / 2 - 1;
		}
		else
			this->max = this->min = (n - 1) / 2;
	}
};

ostream& operator<<(ostream& os, const aside& obj) {
	os << obj.max << " " << obj.min;
	return os;
}

int T, Nt, Kt;

int main() {
	int e;
	
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int k = 1;
		priority_queue<int> queue_gen;
		aside curr;
		
		cin >> Nt >> Kt;

		queue_gen.push(Nt);
		while (k <= Kt) {
			e = queue_gen.top();
			queue_gen.pop();

			curr = aside(e);
			queue_gen.push(curr.max);
			queue_gen.push(curr.min);
			k++;
		}

		cout << "Case #" << t << ": " << curr << endl;
	}

	return 0;
}