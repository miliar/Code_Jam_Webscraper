#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <vector>

bool same_digit(std::string str)
{
	for (int i = 1; i < str.size(); ++i)
	if (str[i] != str[0]) return false;
	return true;
}

bool true_digit(std::string str)
{
	for (int i = str.size() - 1; i > 0; --i)
	if (str[i] < str[i - 1])
		return false;
	return true;
}

int main()
{
	std::ifstream ifs("B-small-attempt7.in");
	std::ofstream ofs("res.txt");
	std::vector<std::string> v;
	std::string line;
	int T;
	//std::cin >> T;
	ifs >> T;

	while (ifs >> line) v.push_back(line);

	for (int i = 1; i <= T; ++i) {
		long long int num;
		std::string snum;
		//std::cin >> snum;
		snum = v[i - 1];
		num = std::stoll(snum);
		if (num < 10) { ofs << "Case #" << i << ": " << num << '\n'; }
		else if (num == 10) { ofs << "Case #" << i << ": " << num - 1 << '\n'; }
		else if ((num / 10) % 10 == 0 && (num / 10) * 10 == num) { ofs << "Case #" << i << ": " << num - 1 << '\n'; }
		else if (true_digit(snum) || same_digit(snum)) { ofs << "Case #" << i << ": " << num << '\n'; }
		else{
			std::string y = snum;
			y[y.size() - 1] += 1;
			if (same_digit(y) && y[0] == '1') {
				y.resize(y.size() - 1);
				for (int i = 0; i < y.size(); ++i)
					y[i] = '9';
				ofs << "Case #" << i << ": " << y << '\n';
			}
			else {
				if (snum.size() == 2) {
					snum[0] -= 1;
					snum[1] = '9';
					ofs << "Case #" << i << ": " << snum << '\n';
				}
				else {
					for (int i = 2; i < snum.size(); ++i) {
						snum[i] = '9';
					}
					snum[1] -= 1;
					if (snum[1] < snum[0]) {
						snum[1] = '9';
						snum[0] -= 1;
						if (snum[0] == '0')
							snum = snum.substr(1, snum.size());
					}
					ofs << "Case #" << i << ": " << snum << '\n';
				}
			}
		}
	}
}