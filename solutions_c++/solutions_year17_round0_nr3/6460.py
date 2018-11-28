#include <iostream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <fstream>
using namespace std;

typedef  unsigned long long int tt;

struct segment {
	tt length;
	tt index;

	segment(tt _n, tt _index) :length(_n), index(_index) {}
	bool operator<(segment const& b) const
	{
		return length < b.length || length == b.length && index > b.index;
	}
};
void a() {
	priority_queue < segment, vector<segment>> q;
	q.push(segment(10, 0));
	q.push(segment(10, 5));
	q.push(segment(6, 0));
	q.push(segment(6, 10));

	while (!q.empty()) {
		segment s = q.top();
		q.pop();
		cout << s.length << "  " << s.index << endl;
	}

}
void solve(tt n, tt k) {
	priority_queue < segment, vector<segment>> q;
	q.push(segment(n,0));
	int ls=0;
	int rs=0;
	for (tt i = 0; i < k; i++) {
		segment s = q.top();
		q.pop();
		ls = (s.length - 1) / 2;
		rs = s.length - ls - 1;

		segment s0(ls, s.index);
		segment s1(rs, s.index + ls + 1);
		q.push(s0);
		q.push(s1);
	}
	cout << rs << " " << ls << "\n";
}

int main() {
#ifdef REDIRECT
	std::ifstream in("c://user/khalefa/downloads/in.txt");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("c://user/khalefa/downloads/out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "Case #" << tc << ": ";
		long long n;
		cin >> n;
		long long k;
		cin >> k;
		solve(n,k);		
	}
#ifdef REDIRECT
	std::cin.rdbuf(cinbuf);   //reset to standard input again
	std::cout.rdbuf(coutbuf); //reset to standard output again
#endif
}

