#include <iostream>
#include <vector>
using namespace std;

bool doit()
{
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	char types[] = "RYB";
	int count[] = {R,Y,B};
	std::vector<char> ret(N, 0);
	int fillInPos = 0;
	for (int i = 0; i < 3; ++i) {
		int largest = 0;
		for (int j = 1; j < 3; ++j) {
			if (count[j] > count[largest])
				largest = j;
		}
		if (count[largest] > N / 2)
			return false;
		for (; count[largest] > 0; --count[largest]) {
			ret[fillInPos] = types[largest];
			fillInPos += 2;
			if (fillInPos >= N) {
				fillInPos = 1;
			}
		}
	}
	for (int i = 0; i < N; ++i) {
		if (ret[i] == ret[(i+1) % N])
			cout << "ERROR" << endl;
		cout << ret[i];
	}
	cout << endl;
	return true;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << (t+1) << ": ";
		if (!doit()) {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
