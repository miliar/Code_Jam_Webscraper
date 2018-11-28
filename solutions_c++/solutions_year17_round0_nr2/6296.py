#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool isTidy(int x) {
	int y = x % 10;
	x = (x - y) / 10;
	while (x > 0) {
		int z = x % 10;
		if (y < z)
			return false;
		y = z;
		x = (x - z) / 10;
	}
	return true;
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	#endif // ONLINE_JUDGE
	int T;
	int index = 1;
	cin >> T;
	while (T) {
		int N; 
		cin >> N;
		int ans = 0;
		for (int i = N; i >= 1 ; i--) {
			if (isTidy(i)) {
				ans = i;
				break;
			}
		}
		cout << "Case #" << index << ": " << ans << endl;
		--T;
		++index;
	}
}