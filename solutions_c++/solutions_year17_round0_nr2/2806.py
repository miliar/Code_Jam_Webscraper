#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>

using namespace std;

int is_tidy_cif(long long nr) {
	if (nr == 0) return 0;
	int last = is_tidy_cif(nr / 10);
	if (last == -1) return -1;

	return last <= (nr % 10) ? (nr % 10) : -1;
}

bool is_tidy(long long nr) {
	return is_tidy_cif(nr) == -1 ? false : true;
}

long long get_tidy(long long left, long long right) {
	if (left > right) return -1;

	long long best = -1, middle = left + (right - left) / 2;
	if (is_tidy(middle)) {
		best = middle;
	}

	long long rtidy = get_tidy(middle + 1, right);
	if (rtidy == -1 && best == -1) {
		best = get_tidy(left, middle-1);
	}
	else if (rtidy != -1){
		best = rtidy;
	}
	return best;
}

vector<int>* divide_cifs(long long nr) {
	if (nr == 0) {
		return new vector<int>();
	}
	auto *v = divide_cifs(nr / 10);
	v->push_back(nr % 10);
	return v;
}

long long get_biggest_number(
	vector<int>* nr,
	vector<int>* result,
	bool is_max_cif,
	int min_cif,
	int index) {
	if (index == nr->size()) return nr->at(0) ? (nr->size () == result->size ()) : true;

	int max_cif = is_max_cif ? 9 : nr->at(index);
	if (max_cif < min_cif) return false;

	bool r;
	result->push_back(max_cif);
	while (min_cif <= max_cif && !(r = get_biggest_number(nr, result, is_max_cif | false, max_cif, index + 1))) {
		max_cif--;
		is_max_cif = true;
		result->pop_back();
		result->push_back(max_cif);
	}
	if (r == false) result->pop_back();
	return r;
}

long long get_tidy_big(long long nr) {
	if (nr == 0) return 0;

	auto *v = divide_cifs(nr);
	vector<int> res;
	if (!get_biggest_number(v, &res, false, 0, 0)) {
		get_biggest_number(v, &res, true, 0, 1);
	}
	long long result = 0;
	for (int i = 0; i < res.size(); i++) {
		result *= 10;
		result += res[i];
	}
	delete v;
	return result;
}

int main() {
	ifstream fin("B-large.in");
	ofstream fout("t22.out");

	for (int i = 0; i < 1000; i++) {
		assert(get_tidy(0, i) == get_tidy_big(i));
		std::cerr << "Test passed for number " << i << '\n';
	}

	long long n;
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> n;
		long long result = get_tidy_big(n);

		fout << "Case #" << i + 1 << ": " << result << '\n';
	}

	return 0;
}