#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;
#define int long long
vector<int> nums;
int nextSmallest(int i) {
	int tracker = i;
	while (tracker >= 0 && nums[tracker] >= nums[tracker+1]) {
		if (tracker == 0) return -1;
		tracker--;
	}
	return tracker + 1;
}
#undef int
int main() {
	#define int long long
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int cases; cin >> cases >> ws;
	string line;
	for (int i = 1; i <= cases; i++) {
		bool firstNumRevoked  = false;
		cin >> line >> ws;
		nums.clear();
		for (auto x : line) nums.push_back(x - '0');
		if (nums.size() > 1) {
			for (int j = nums.size() - 2; j >= 0; j--) {
				if (nums[j] > nums[j+1]) {
					int nn = nextSmallest(j);
					if (nn == -1) {
						nn = 0;
						if (nums[nn] == 1)
							firstNumRevoked = true;
					}
					nums[nn]--;
					for (int c = nn + 1; c < nums.size(); c++) nums[c] = 9;
					if (firstNumRevoked) break;
				}
			}
		}
		cout << "Case #" << i << ": ";
		for (int j = (firstNumRevoked ? 1 : 0); j < line.size(); j++) 
				cout << nums[j];

		cout << "\n";
	}
	
	return 0;
}