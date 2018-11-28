
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef unsigned long long ull;
typedef pair<int, int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int INF = 987654321;

int bc(int n) { return n ? bc((n - 1)&n) + 1 : 0; }
#define PI 3.141592
int main() {
	string infile = "C-large.in";
	//string infile = "in.txt";
	string outfile = "out.txt";

	freopen(infile.c_str(), "r", stdin);
	freopen(outfile.c_str(), "w", stdout);
	int tt;

	cin >> tt;
	for (int tc = 1; tc <= tt; tc++) {

		unsigned long long k, n, maximum;
		cin >> k >> n;
		int i = 1;
		
		map<ull, ull> mm;
		mm.insert(make_pair(k, 1));
		for (unsigned long long i = 0; i < n - 1; i++) {
			if (mm.size() == 0) break;
			auto final_iter = mm.end();
			--final_iter;
			
			ull next = final_iter->first;
			ull num_of_next = final_iter->second;

			if (num_of_next <= n - 1 - i) {
				mm.erase(final_iter);
				i += num_of_next - 1;
			}
			else {
				num_of_next = n - 1 - i;
				i += num_of_next - 1;
				if (final_iter->second - num_of_next == 0)
					mm.erase(final_iter);
				else 
					final_iter->second = final_iter->second - num_of_next;
			}

			unsigned long long num = (next - 1) / 2;
			if (next % 2 == 0) {
				auto iter = mm.find(num + 1);
				if (iter != mm.end())
					iter->second += num_of_next;
				else
					mm[num + 1] = num_of_next;
				if (num > 0) {
					iter = mm.find(num);
					if (iter != mm.end())
						iter->second+= num_of_next;
					else
						mm[num] = num_of_next;
				}
			}
			else {
				if (num > 0) {
					auto iter = mm.find(num);
					if (iter != mm.end())
						iter->second += 2 * num_of_next;
					else
						mm[num] = 2 * num_of_next;
				}
			}
		}
		maximum = 0;

//		for (unsigned long long i = n - 1; i <= (n - 1) * 2 + 2; i++) {
//			printf("%d\n", buf[i]);
//			if (maximum < buf[i])
//				maximum = buf[i];
//		}
		if (mm.size() > 0) {
			auto final_iter = mm.end();
			--final_iter;
			maximum = final_iter->first;
		}

		if (maximum == 0)
			printf("Case #%d: 0 0\n", tc);
		else {
			unsigned long long a, b;
			a = maximum / 2;
			b = (maximum - 1) / 2;
			cout << "Case #" << tc << ": " << a << " " << b << "\n";
		}
	}
}

