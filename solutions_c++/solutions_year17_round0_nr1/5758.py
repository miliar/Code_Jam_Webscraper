#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

class Problem1 {
public:
	Problem1(string input_file) {
		
		fs.open(input_file, std::fstream::in);
		ofs.open("p1_output.txt");
	}
	~Problem1() {
		fs.close();
		ofs.close();
	}
	void Problem1::run() {
		char line[1024];
		int idx = 0;
		int q = 0;
		char cc;
		fs >> q;
		for (idx = 1; idx <= q; idx++) {
			fs.getline(line, 1024);
			if (idx == 1) fs.getline(line, 1024);
			string str_line(line);
			int pos = str_line.find(" ");
			string pancakes = str_line.substr(0, pos);
			string str_l = str_line.substr(pos + 1);
			int l = atoi(str_l.c_str());
			int ans = minFlip(pancakes, l);
			ofs << "Case #" << idx << ": ";
			if (ans != -1) {
				ofs << ans << endl;
			}
			else {
				ofs << "IMPOSSIBLE" << endl;
			}
		}
	}
private:
	fstream fs;
	ofstream ofs;
	int Problem1::minFlip(string pancakes, int l) {
		int n = pancakes.size(), ans = 0;
		for (int i = 0; i < n - l + 1; i++) {
			if (pancakes[i] == '-') {
				ans++;
				for (int j = i; j < i + l; j++) {
					pancakes[j] = pancakes[j] == '+' ? '-' : '+';
				}
			}
		}
		bool done = true;
		for (int i = 0; i < n; i++) {
			if (pancakes[i] == '-') {
				done = false;
				break;
			}
		}
		if (done) return ans;
		return -1;
	}
};

int main()
{
	Problem1 p1("A-large.in");
	p1.run();
}
