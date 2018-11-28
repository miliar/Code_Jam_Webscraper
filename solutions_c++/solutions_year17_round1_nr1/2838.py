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
	string in_path = "..//pr.in";
	string out_path = "..//out.txt";

	std::ifstream in(in_path);
	std::ofstream out(out_path);
	int test_num;
	in >> test_num;
	for (int i = 0; i < test_num; ++i)
	{
		proc_test(i + 1, in, out);
	}
}

template <typename OutType, typename AnsType>
void print_ans(int test_num, OutType& out, AnsType ans)
{
	out << "Case #" << test_num << ": " << ans << endl;
}
template <typename OutType>
void print_ans(int test_num, OutType& out, vector<string> ans)
{
	out << "Case #" << test_num << ": " << endl;
	for (int i = 0; i < ans.size(); ++i)
		out << ans[i] << endl;
}

template<typename Grid>
void fill_in(Grid& gr, int i0, int j0, int ii, int jj, char t)
{
	for (int i = i0; i <= ii; ++i)
	{
		for (int j = j0; j <= jj; ++j)
			gr[i][j] = t;
	}
}
template<typename Grid>
bool check(Grid& gr, int i0, int j0, int ii, int jj,char t)
{
	for (int i = i0; i <= ii; ++i)
	{
		for (int j = j0; j <= jj; ++j)
			if (gr[i][j] != t&&gr[i][j]!='?')
				return false;
	}
	return true;
}

template <typename Grid>
void add_to_n(Grid& gr, int i, int j)
{
	char t = gr[i][j];
	if (i > 0)
	{
		if (gr[i - 1][j] == '?')
			gr[i - 1][j] = t;
	}
	if (i < gr.size()-1)
	{
		if (gr[i +1][j] == '?')
			gr[i + 1][j] = t;
	}
	if (j > 0)
	{
		if (gr[i][j-1] == '?')
			gr[i][j-1] = t;
	}
	if (j < gr[0].size() - 1)
	{
		if (gr[i][j+1] == '?')
			gr[i][j+1] = t;
	}
}


template<typename Grid>
bool solve(Grid& gr, vi& present, vi& cl,vi& cr,vi& cu,vi& cd)
{
	int c = gr[0].size();
	int r = gr.size();
	map<char, pair<int, int>> seen;
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			if (gr[i][j] != '?')
			{
				auto ss = seen.find(gr[i][j]);
				if ( ss!= seen.end())
				{
					int pr = gr[i][j] - 'A';
					if (!check(gr, cu[pr], cl[pr], cd[pr], cr[pr], pr + 'A'))
						return false;
				}
				else
				{
					seen[gr[i][j]] = make_pair(i, j);
				}
			}
			else
			{
				for (int pr = 0; pr < 25; ++pr)
				{
					if (present[pr])
					{
						gr[i][j] = pr + 'A';
						auto old_cu = cu[pr];
						auto old_cd = cd[pr];
						auto old_cr = cr[pr];
						auto old_cl = cl[pr];
						cu[pr] = min(cu[pr], i);
						cd[pr] = max(cd[pr], i);
						cl[pr] = min(cl[pr], j);
						cr[pr] = max(cr[pr], j);
						if (!check(gr, cu[pr], cl[pr], cd[pr], cr[pr],pr+'A'))
						{
						}
						else
						{
							if (solve(gr, present,cl,cr,cu,cd))
								return true;
						}

						cu[pr] = old_cu;
						cd[pr] = old_cd;
						cl[pr] = old_cl;
						cr[pr] = old_cr;
					}
				}
				gr[i][j] = '?';
				return false;
			}
		}
	}
	return true;
}

template<typename InType, typename OutType>
void proc_test(int test_num, InType& in, OutType& out)
{
	int r, c;
	in >> r >> c;
	vi present(25, 0);
	vector<string> grid(r,"");
	vi cu, cd, cl, cr;
	cu.resize(25, -1);
	cd.resize(25, -1);
	cl.resize(25, -1);
	cr.resize(25, -1);
	for (int i = 0; i < r; ++i)
	{
		grid[i].resize(c);
		for (int j = 0; j < c; ++j)
		{
			in >> grid[i][j];
			if (grid[i][j] == '?')
				continue;
			present[grid[i][j]-'A'] = 1;
			cl[grid[i][j] - 'A'] = cr[grid[i][j] - 'A'] = j;
			cu[grid[i][j] - 'A'] = cd[grid[i][j] - 'A'] = i;
		}
	}
	
	if (!solve(grid, present,cl,cr,cu,cd))
		throw std::runtime_error("");
	print_ans(test_num,out, grid);
}
