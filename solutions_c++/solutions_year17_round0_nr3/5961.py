#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

class Problem3 {
public:
	Problem3(string input_file) {

		fs.open(input_file, std::fstream::in);
		ofs.open("p3_output.txt");
	}
	~Problem3() {
		fs.close();
		ofs.close();
	}
	void Problem3::run() {
		char line[1024];
		int idx = 0;
		int q = 0;
		char cc;
		fs >> q;
		for (idx = 1; idx <= q; idx++) {
			long long n, k;
			fs >> n >> k;
			long long min_lr = (n - 1) / 2, max_lr = (n - 1) / 2;
			long long man = 1, tot = 0;;
			while (tot + man < k) {
				max_lr = (max_lr - 1) / 2;
				min_lr = (min_lr - 1) / 2;
				tot += man;
				man *= 2;
			}
			long long distance_k = k - tot;
			long long distance_n = (n+1) % (man * 2);
			if (n + 1 < man * 2) distance_n = 0;
			if (distance_n >= distance_k) {
				max_lr++;
			}
			if (distance_n - man >= distance_k) {
				min_lr++;
			}
			ofs << "Case #" << idx << ": " << max_lr << " " << min_lr << endl;
		}
	}
private:
	fstream fs;
	ofstream ofs;
	
};

int main()
{
	Problem3 p3("C-small-1-attempt0.in");
	p3.run();
}
