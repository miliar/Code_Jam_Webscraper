// c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <memory>


using std::string;
using std::vector;
using std::map;
using std::unordered_map;
using std::ifstream;
using std::ofstream;

class Bath {
	long long last_inserted;
	std::shared_ptr<vector<char>> cabs;
	map<long long, long long> mmap;
public:
	Bath(long long c_num)
		: last_inserted(-1)
		,cabs(new vector<char>(c_num+2))
	    ,mmap(){
		(*cabs)[0] = 1;
		(*cabs)[(c_num+2) - 1] = 1;

		mmap[0] = 1;
		mmap[(c_num + 2) - 1] = 1;
	}

	struct SEARCH {
		map<long long, long long>::iterator beg;
		map<long long, long long>::iterator end;
		long long diff;
	};

	void insert() {
		SEARCH s{};
		s.diff = -1;

		map<long long, long long>::iterator ib = mmap.begin();
		map<long long, long long>::iterator inext = mmap.begin();
		++inext;

		for (; inext != mmap.end(); ++ib, ++inext) {
			long long diff = inext->first - ib->first;
			if (diff > s.diff) {
				s.diff = diff;
				s.beg = ib;
				s.end = inext;
			}
		}

		long long new_key = (s.diff / 2) + s.beg->first;
		(*cabs)[new_key] = 1;
		mmap[new_key] = 1;
		last_inserted = new_key;
	}

	std::pair<long long, long long> get_min_max_for_last_inserted() {
		map<long long, long long>::iterator it = mmap.find(last_inserted);

		long long left = 0;
		if (it != mmap.begin()) {
			map<long long, long long>::iterator ileft = it;
			ileft--;
			left = (it->first - ileft->first)-1;
		}

		long long right = 0;
		if (it != mmap.end()) {
			map<long long, long long>::iterator iright = it;
			iright++;
			right = (iright->first - it->first)-1;
		}

		long long max = right >= left ? right : left;
		long long min = left < right ? left : right;
		
		return std::pair<long long, long long>(max,min);

	}
};

 

std::pair<long long, long long> solve_case(long long bath, long long people) {
	if (bath == people)
		return std::pair<long long, long long>(0, 0);

	Bath b(bath);

	for (int i = 0; i < people; ++i) {
		b.insert();
	}


	
	return b.get_min_max_for_last_inserted();
}

int main()
{

	ifstream ifs("F:\\ttempp\\codejam_1\\Debug\\input.in");

	if (!ifs.is_open())
		return -1;

	int n_cases = 0;
	ifs >> n_cases;

	ofstream out("F:\\ttempp\\codejam_1\\Debug\\output.out");
	if (!out.is_open())
		return -1;

	for (int i = 0; i < n_cases; ++i) {
		long long bath, people;
		ifs >> bath;
		ifs >> people;
		std::pair<long long, long long> res = solve_case(bath, people);
		out << "Case #" << i+1 << ": " << res.first << " " << res.second << "\n";
	}


	return 0;
}


