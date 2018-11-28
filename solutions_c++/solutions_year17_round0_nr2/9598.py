#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool comp(string::value_type &a, string::value_type & b) {
	return a < b;
}

void Step(string::iterator &beg, string::iterator &end) {
	while (true) {
		auto cur = is_sorted_until(beg, end);
		auto cur_prev = cur - 1;
		if (cur == end)
			return;
		else {
			for (auto it = cur; it != beg;) {
				--it;
				if (*it != '0') {
					*it -= 1;
					for (auto it2 = it + 1; it2 != end; ++it2)
						*it2 = '9';
					break;
				}
			}
		}
	}
}

void Solver() {
	string str;
	getline(cin, str);
	Step(str.begin(), str.end());
	str.erase(0, min(str.find_first_not_of('0'), str.size() - 1));
	cout << str << endl;
}

int main() {
	FILE *stream;
	freopen_s(&stream, "in.txt", "rt", stdin);
	freopen_s(&stream, "out.txt", "wt", stdout);
	size_t NumOfTasks;
	cin >> NumOfTasks;
	cin.ignore();
	for (size_t Task = 1; Task <= NumOfTasks; ++Task) {
		cout << "Case #" << Task << ": ";
		Solver();
	}

}

