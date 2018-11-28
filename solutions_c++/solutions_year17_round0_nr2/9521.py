#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>

using namespace std;

auto isTidy(auto num) {
//	auto x = num;
	int count = 0;
	std::vector<int> v;
	while(num) {
		v.push_back(num%10);
		num = num/10;	
		count++;
	} 

	vector<int> temp(count);
	copy(begin(v), end(v), begin(temp));
	sort(begin(temp), end(temp), [](int ele1, int ele2){return ele1 > ele2;});

	if (v == temp) {
		return true;
	}
	return false;
}

int main(int argc, char const *argv[])
{
	int t, n;
	cin >> t;
	assert(t>=1 && t<=100);
	for (int cs = 1; cs <= t; ++cs) {
		cin >> n;
		assert(n>=1 && n<=1000);
		while (1) {
			if (isTidy(n)) {
				cout << "CASE #" << cs << ": " << n << endl;
				break;
			}
			n--;
		}
	}
	return 0;
}
		
