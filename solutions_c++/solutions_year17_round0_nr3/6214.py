#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef struct node_s {
	int min;
	int max;
	int value;
} node_t;

vector<node_t> v;

void split(int L, int R) {
	//Quebrar os vetores como o mergesort e adicionar no vector o node_t correspondente ao nó removido
	node_t n;

	n.value = ceil((L + R - 1) / 2.0);
	n.min = n.value - L;
	n.max = R - n.value;

	//cout << "Value: " << n.value << " Min: " << n.min << " Max: " << n.max << "\n";

	if (n.min < 0 || n.max < 0)
		return;

	v.push_back(n);

	if (L == R)
		return;

	split(L, n.value - 1);
	split(n.value + 1, R);

}

bool compFunction(node_t a, node_t b) {

	if (a.min != b.min)
		return (a.min > b.min);
	if (a.max != b.max)
		return (a.max > b.max);
	return (a.value < b.value);
}

int main(int argc, char const *argv[]) {

	int T, N, k;
	int c = 0;

	cin >> T;

	while (T--) {
		cin >> N;
		cin >> k;


		split(1, N);

		sort(v.begin(), v.end(), compFunction);

		cout << "Case #" << ++c << ": " << v[k - 1].max << " " << v[k - 1].min << '\n';

		//cout << v.size();
		//for (int i = 0; i < (int)v.size(); ++i) {
		//	cout << "Value: " << v[i].value << " Min: " << v[i].min << " Max: " << v[i].max << "\n";
		//}


		v.clear();
	}

	return 0;
}