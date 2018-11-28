#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<math.h>
#include<algorithm>
#include<iomanip>


using namespace std;

int main() {
	int t;
	ofstream ofs("out.txt");
	ifstream ifs("in.txt");
	ifs >> t;
	for (int i = 0; i < t; i++) {
		long long n, k;
		ifs >> n >> k;
		map<long long, long long> b;
		ofs << "Case #" << (i + 1) << ": ";
		b[-n] = 1;
		for (long long j = 0; j < k; j++) {
			if (b.size() == 0) {
				ofs << 0 << " " << 0 << endl;
				break;
			}
			auto it = b.begin();
			long long c = -it->first, num = it->second;
			//cout << j << endl;
			if (c % 2 == 0) {
				b.erase(-c);
				if(c / 2 > 0)
					b[-c / 2] += num;
				if(c / 2 > 1)
					b[-c / 2 + 1] += num;
				j += num - 1;
				if (j >= k - 1) {
					ofs << c / 2 << " " << c / 2 - 1 << endl;
				}
				continue;
			}
			else {
				b.erase(-c);
				if (c / 2 > 0) {
					b[-c / 2] += num*2;
				}
				j += num - 1;
				if (j >= k - 1) {
					ofs << c / 2 << " " << c / 2 << endl;
				}
				continue;
			}
		}

	}
	return 0;
}