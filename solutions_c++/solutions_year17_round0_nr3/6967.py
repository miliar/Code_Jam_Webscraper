#include <fstream>
#include <string>
#include <utility>

enum Direction { LEFT, RIGHT };

std::string print_stalls(const bool * stalls, const int &n_stalls) {
	std::string s = "";

	for (int i = 0; i < n_stalls; i++) {
		s += stalls[i] ? "1" : "0";
	}

	return s;
}

//int taken(Direction d, int start, const bool * stalls, const int &n_stalls) {
//	int count = 0;
//	int old_start = start;
//
//	bool b = false;
//
//	if (d == LEFT) {
//		start = start % 2 ? start / 2 : start / 2 - 1;
//
//		while (!b) {
//			while (old_start > 0 && !stalls[start]) {
//				b = true;
//				count += (old_start - start);
//				old_start = start;
//				start = start % 2 ? start / 2 : start / 2 - 1;
//			}
//
//			if (b) break; // Remove line
//
//			start += old_start - start % 2 ? (old_start - start) / 2 : (old_start - start) / 2 + 1;
//		}		
//
//		return count;
//	}
//
//	else {
//		start += (n_stalls - start) % 2 ? (n_stalls - start) / 2 : (n_stalls - start) / 2 - 1;
//
//		while (start < n_stalls && !stalls[start]) {
//			count += (start - old_start);
//			old_start = start;
//			start += (n_stalls - start) % 2 ? (n_stalls - start) / 2 : (n_stalls - start) / 2 - 1;
//			if (old_start == start) start++;
//		}
//
//		return count;
//	}
//}

int taken(Direction d, int start, const bool * stalls, const int &n_stalls) {
	int count = 0;
	
	if (d == LEFT) {
		start--;
		while (start >= 0 && !stalls[start]) {
			count++;
			start--;
		}
	}

	else {
		start++;
		while (start < n_stalls && !stalls[start]) {
			count++;
			start++;
		}
	}

	return count;
}

//std::pair<int, int> assign_stall(bool * stalls, const int &n_stalls) {
//	int midpoint = n_stalls % 2 ? n_stalls / 2 : n_stalls / 2 - 1;
//	int freeL, freeR,
//		min = midpoint,
//		max = n_stalls - midpoint - 1;
//
//	while (stalls[midpoint]) {
//		freeL = taken(LEFT, midpoint, stalls, n_stalls);
//		freeR = taken(RIGHT, midpoint, stalls, n_stalls);
//
//		if (freeR < freeL) { min = freeR; max = freeL; }
//		else { min = freeL; max = freeR; }
//
//		//if (freeR > freeL) midpoint += (n_stalls - midpoint) % 2 ? (n_stalls - midpoint) / 2 : (n_stalls - midpoint) / 2 - 1;
//		//else midpoint = midpoint % 2 ? midpoint / 2 : midpoint / 2 - 1;
//
//		if (freeR > freeL) midpoint += freeR % 2 ? freeR / 2 + 1 : freeR / 2;
//		else midpoint -= freeL % 2 ? freeL / 2 : freeL / 2 + 1;
//	}
//
//	stalls[midpoint] = true;
//	return std::make_pair(min, max);
//}

std::pair<int, int> assign_stall(bool * stalls, const int &n_stalls, bool quiet) {
	int max_i = 0, max_len = -1;
	int i, len;

	for (int it = 0; it < n_stalls; it++) {
		i = it; len = 0;
		while (stalls[it] == false) {
			len++;
			it++;
		}

		if (len > max_len) {
			max_i = i;
			max_len = len;
		}
	}

	if (max_len == -1) return std::make_pair(-1, -1);

	int stall = max_i + (max_len % 2 ? max_len / 2 : max_len / 2 - 1);
	stalls[stall] = true;

	if (quiet) return std::make_pair(0, 0);
	
	int l = taken(LEFT, stall, stalls, n_stalls);
	int r = taken(RIGHT, stall, stalls, n_stalls);

	int min, max;
	if (r < l) { min = r; max = l; }
	else { min = l; max = r; }
	
	return std::make_pair(max, min);
}


std::pair<int, int> go_to_the_toilet(const int &n_stalls, const int &n_people) {
	bool * stalls = new bool[n_stalls]();

	for (int i = 0; i < n_people-1; i++) {
		assign_stall(stalls, n_stalls, true);
	}
		
	return assign_stall(stalls, n_stalls, false);
}

int main() {
	std::string name = "C-small-1-attempt0";
	std::ifstream fin(name + ".in");
	std::ofstream fout(name + ".out");

	if (!fin.is_open() || !fout.is_open())
		return - 2;

	int N; fin >> N;
	int n_stalls, n_people;
	std::pair<int, int> minmax;

	for (int i = 1; i <= N; i++) {
		fin >> n_stalls >> n_people;
		minmax = go_to_the_toilet(n_stalls, n_people);
		fout << "Case #" << i << ": " <<
			std::get<0>(minmax) << " " << std::get<1>(minmax);
		if (i != N)	fout << std::endl;
	}

	return 0;
}