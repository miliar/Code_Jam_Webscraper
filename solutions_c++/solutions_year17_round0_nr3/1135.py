#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main() {
	ifstream in;
	ofstream out;

	in.open("C:\\works\\in.txt");
	out.open("C:\\works\\out.txt");

	int n;

	in >> n;

	for (int i = 0; i < n; i++) {;
		unsigned long long n, k;
		in >> n >> k;
		map<unsigned long long, unsigned long long> segments;
		segments[n] = 1;
		unsigned long long res = 0;
		while (true) {
			auto cur = prev(segments.end());
			unsigned long long remain = cur->second;
			unsigned long long val = cur->first;
			if (remain >= k) {
				res = val;
				break;
			}
			unsigned long long left = (val - 1) / 2;
			unsigned long long right = val - (val - 1) / 2 - 1;
			segments.erase(cur);
			segments[left] += remain;
			segments[right] += remain;
			k -= remain;
		}
		out << "Case #" << i + 1 << ": ";
		out << (res - (res - 1) / 2 - 1) << " " << (res - 1) / 2;
		out << endl;
	}
}