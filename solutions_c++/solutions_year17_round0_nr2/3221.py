#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <set>
#include <fstream>
#include <map>
#include <queue>
#include <unordered_map>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <intrin.h>
#include <iomanip>
#include <bitset>
#include <unordered_set>
using namespace std;


template <typename A, typename B> ostream& operator<<(ostream& stream, const pair <A, B> &p) { stream << "{" << p.first << "," << p.second << "}"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const vector <A> &v) { stream << "["; for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " "; stream << "]"; return stream; }
template <typename A, typename B> ostream& operator<<(ostream &stream, const map <A, B> &v) { stream << "["; for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " "; stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const set <A> &v) { stream << "["; for (auto itr = v.begin(); itr != v.end(); itr++)stream << *itr << " "; stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const stack <A> &v) { stack <A> st = v; stream << "["; while (!st.empty()) { stream << st.top() << " "; st.pop(); }stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const priority_queue <A> &v) { priority_queue <A> q = v; stream << "["; while (!q.empty()) { stream << q.top() << " "; q.pop(); }stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const queue <A> &v) { queue <A> q = v; stream << "["; while (!q.empty()) { stream << q.front() << " "; q.pop(); }stream << "]"; return stream; }
template <typename A> ostream& operator<<(ostream &stream, const deque <A> &v) { deque <A> q = v; stream << "["; while (!q.empty()) { stream << q.front() << " "; q.pop_front(); }stream << "]"; return stream; }

typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef vector<vector<char>> vvc;

template<typename InType, typename OutType>
void proc_test(int test_num, InType& in, OutType& out);

int main()
{
	string in_path = "../pr.in";
	string out_path = "../out.txt";

	std::ifstream in(in_path);
	std::ofstream out(out_path);
	int test_num;
	in >> test_num;
	for (int i = 0; i < test_num; ++i)
	{
		proc_test(i+1,in,out);
	}
}

template <typename OutType, typename AnsType>
void print_ans(int test_num, OutType& out, AnsType ans)
{
	out << "Case #" << test_num << ": " << ans << endl;
}

bool ok(string& num)
{
	bool ans = true;
	for (int i = 0; i < num.size()-1; ++i)
		ans&=(num[i] <= num[i + 1]);
	return ans;
}

template<typename InType, typename OutType>
void proc_test(int test_num, InType& in, OutType& out)
{
	string last;
	in >> last;
	if (last.size() == 1)
	{
		print_ans(test_num, out, last);
		return;
	}
	while (!ok(last))
	{
		for (int i = 1; i < last.size(); ++i)
		{
			if (last[i] < last[i - 1])
			{
				for (int j = i; j < last.size(); ++j)
					last[j] = '9';
				last[i - 1]--;
			}
		}
	}
	string ans;
	if (last[0] == '0')
	{
		for (int i = 1; i < last.size(); ++i)
			ans += last[i];

	}
	else
		ans = last;
	print_ans(test_num, out, ans);
}
