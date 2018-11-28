// b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <vector>

using std::string;
using std::vector;
using std::ifstream;
using std::ofstream;

typedef long long Case_Type;

bool is_tidy(Case_Type in) {

	vector<Case_Type> rr;

	Case_Type tmp = in;

	while (tmp > 0) {
		Case_Type left = tmp / 10;
		Case_Type rem = tmp % 10;
		if ((rr.size() > 0) && (rem > rr.back()))
			return false;
		rr.push_back(rem);
		tmp = left;
	}

	/*for (int j = rr.size() - 1; j > 0; --j) {
		if (rr[j] > rr[j - 1])
			return false;
	}*/
	return true;
}
int get_size(Case_Type in) {
	return printf("%lld", in);
}

Case_Type get_biggest(Case_Type in) {
	int size = get_size(in);

	size--;
	string s;
	while (size--){
		s.push_back('9');
	} ;

	return atoll(s.c_str());
}

Case_Type solve_case(Case_Type in) {
	Case_Type tmp = in;
	Case_Type biggest = get_biggest(in);
	for(int i = 0;i < 1000 ; ++i, tmp--){
		if (is_tidy(tmp))
			return tmp;
		else if (tmp <= biggest)
			return biggest;
	} 

	return biggest;
}

int main()
{

	ifstream ifs("F:\\ttempp\\codejam_1\\Debug\\input.in");

	if (!ifs.is_open())
		return -1;

	int n_cases = 0;
	ifs >> n_cases;
	vector<Case_Type> data(n_cases);

	for (int i = 0; i < n_cases; ++i) {
		ifs >> data[i];
	}

	ofstream out("F:\\ttempp\\codejam_1\\Debug\\output.out");
	if (!out.is_open())
		return -1;

	for (int j = 0; j < data.size(); ++j) {
		Case_Type res = solve_case(data[j]);
		char sf[1024] = { 0 };
		sprintf_s(sf, "Case #%d: ", j + 1);
		out << sf << res << "\n";
	}

	return 0;
}

