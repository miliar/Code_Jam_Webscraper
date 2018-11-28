#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		double dist, num;
		double min = 0;
		cin >> dist >> num;
		for (int j = 0; j < num; j++) {
			double pos, speed;
			cin >> pos >> speed;
			double calc = (dist - pos) / speed;
			if (calc > min) {
				min = calc;
			}
		}
		cout << "Case #" << i + 1 << ": " << setprecision(6) << fixed << dist / min << endl;
	}
	return 0;
}