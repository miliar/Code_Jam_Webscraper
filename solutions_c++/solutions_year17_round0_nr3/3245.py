#include <vector>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
typedef unsigned long long ull;

struct DD
{
	ull a;
	ull b;

	bool non_exist;
	DD(ull a, ull b) : a(a), b(b), non_exist(false) {}
	DD() { a = 0; b = 0; non_exist = true;  }

	bool is_same() { return a == b;  }
	bool exist() { return !non_exist; }

	int desc(DD& a1, DD& a2) {
		a1 = one_desc(a);
		a2 = one_desc(b);

		int cnt = 0;
		if (a1.a == a1.b) cnt++;
		if (a2.a == a2.b) cnt++;

		return cnt;
	}

	static DD one_desc(ull x) {
		if (x == 0) return DD(0, 0);
		if (x % 2 == 0) {
			return DD(x / 2, x / 2 - 1);
		}
		else return DD((x - 1) / 2, (x - 1) / 2);
	}
};
vector<ull> two_power_table()
{
	vector<ull> two_powers;
	ull two = 1;
	two_powers.push_back(1);
	for (int i = 0; i < 64; i++) {
		two *= 2;
		two_powers.push_back(two);
	}

	return two_powers;
}
int main() {
	ifstream in("C-large.in");
	ofstream out("out.txt");

	int T;
	string temp;
	getline(in, temp);
	T = stoi(temp);

	string s;
	int current = 1;

	const vector<ull> two_power = two_power_table();

	while (T) {
		getline(in, s);

		auto num_str = s.substr(0, s.find(" "));
		auto k_str = s.substr(s.find(" ") + 1);

		ull num = stoull(num_str);
		ull K = stoull(k_str);
		ull temp_K = K, ori_K = K;

		int power = 0;
		while (temp_K /= 2) {
			power++;
		}

		DD d = DD::one_desc(num);
		DD same, diff;
		
		ull num_same = 0, num_diff = 0;

		if (d.is_same()) {
			same = d;
			num_same++;
		}
		else {
			diff = d;
			num_diff++;
		}

		for (int i = 0; i < power; i++) {
			ull temp_same = 0, temp_diff = 0;
			DD a[4];
			if (same.exist()) {
				int c = same.desc(a[0], a[1]);
				temp_same += (c * num_same);
				temp_diff += ((2 - c) * num_same);
			}
			if (diff.exist()) {
				int c = diff.desc(a[2], a[3]);
				temp_same += (c * num_diff);
				temp_diff += ((2 - c) * num_diff);
			}
			
			num_same = temp_same;
			num_diff = temp_diff;

			same = DD();
			diff = DD();

			for (int i = 0; i < 4; i++) {
				if (a[i].exist() && a[i].is_same()) {
					same = a[i];
				}
				else if (a[i].exist() && !a[i].is_same()) {
					diff = a[i];
				}
			}

			K -= two_power[i];
		}
		/*
		if (ori_K > num / 2) {
			out << "Case #" << current << ": 0 0" << endl;
		}*/
		//else {
			if (same.a + same.b > diff.a + diff.b) {
				if (K <= num_same) {
					out << "Case #" << current << ": " << same.a << " " << same.b << endl;
				}
				else {
					out << "Case #" << current << ": " << diff.a << " " << diff.b << endl;
				}
			}
			else {
				if (K <= num_diff) {
					out << "Case #" << current << ": " << diff.a << " " << diff.b << endl;
				}
				else {
					out << "Case #" << current << ": " << same.a << " " << same.b << endl;
				}
			}
		//}

		T--;
		current++;
	}
}