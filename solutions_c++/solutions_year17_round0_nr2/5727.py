#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

class Problem2 {
public:
	Problem2(string input_file) {

		fs.open(input_file, std::fstream::in);
		ofs.open("p2_output.txt");
	}
	~Problem2() {
		fs.close();
		ofs.close();
	}
	void Problem2::run() {
		char line[1024];
		int idx = 0;
		int q = 0;
		char cc;
		fs >> q;
		for (idx = 1; idx <= q; idx++) {
			fs.getline(line, 1024);
			if (idx == 1) fs.getline(line, 1024);
			string str_num(line);
			string ans = getMaxTidy(str_num);
			ofs << "Case #" << idx << ": " << ans.c_str() << endl;
		}
	}
private:
	fstream fs;
	ofstream ofs;
	string Problem2::getMaxTidy(string num) {
		int pos1 = -1, pos2 = -1, pos3 = -1;
		int n = num.size();
		for (int i = 0; i < n - 1; i++) {
			if (num[i] < num[i + 1]) {
				pos1 = i;
				pos2 = i;
			}
			else if (num[i] == num[i + 1]) {
				pos2 = i;
			}
			else {
				pos3 = i;
				break;
			}
		}
		if (pos2 == n - 2 || n == 1) {
			return num;
		}
		pos1++;
		num[pos1] -= 1;
		for (int i = pos1 + 1; i < n; i++) {
			num[i] = '9';
		}
		string ans = num;
		if (num[0] == '0') {
			ans = num.substr(1);
		}
		return ans;
	}
};

int main()
{
	Problem2 p2("B-large.in");
	p2.run();
}
