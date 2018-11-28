#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

void print_vec(vector<int>& vec)
{
#if 0
	cout << "--------------------------------------------------" << endl;
	vector<int>::iterator v = vec.begin();
	while( v != vec.end()) {
		cout << "value of v = " << *v << endl;
		v++;
	}
	cout << "--------------------------------------------------" << endl;
#endif
}

void break_place(int k, int& l, int& r)
{
	if (k <= 1) {
		l = r = 0;
		return;
	}

	if (k%2 == 1) l = r = k/2;
	else {
		l = k/2 -1;
		r = k/2;
	}
}

void find_pos(vector<int>& vec)
{
	print_vec(vec);
	int l = 0, r = 0;
	int max = *max_element(vec.begin(), vec.end());
	break_place(max, l, r);

#if 0
	vec.erase(remove(vec.begin(), vec.end(), max), vec.end());
#endif

		vector<int>::iterator pos = find(vec.begin(), vec.end(), max);
		vector<int>::iterator it = vec.begin();
		while (it != vec.end()) {
			if (it == pos) {
    				vec.erase(pos);
				break;
			}
			it++;
		}
		vec.push_back(l);
		vec.push_back(r);
		print_vec(vec);
}

int main()
{
	int T, n, k, max, l, r;
	vector<int> empty_place;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n >> k;
		empty_place.push_back(n);
		
		k -= 1;

		while (k--)
			find_pos(empty_place);
		max = *max_element(empty_place.begin(), empty_place.end());
		break_place(max, l, r);
		empty_place.clear();

		cout << "Case #" << i + 1 << ": " << r << " " << l << endl;
	}
	return 0;
}
