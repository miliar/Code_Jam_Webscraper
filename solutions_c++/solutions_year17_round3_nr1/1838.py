#define _USE_MATH_DEFINES
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
#include <cmath>
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
void print_ans(int test_num, OutType& out, double ans)
{
	out << "Case #" << test_num << ": ";
	out<< std::fixed<<setprecision(9)<< ans << endl;
}
template <typename OutType>
void print_ans(int test_num, OutType& out, vector<string> ans)
{
	out << "Case #" << test_num << ": " << endl;
	for (int i = 0; i < ans.size(); ++i)
		out << ans[i] << endl;
}


template<typename InType, typename OutType>
void proc_test(int test_num, InType& in, OutType& out)
{
	int n, k;
	in >> n >> k;
	
	typedef vector<pair<ll, ll>> vvp;
	vvp p(n);
	int r, h;
	for (int i = 0; i < n; ++i)
	{
		in >> r >> h;
		p[i].first = r;
		p[i].second = h;
	}

	sort(p.begin(), p.end());
	priority_queue<pair<ll,ll>> q;
	multiset<ll> rmax;
	double ans = 0;
	ll bsum = 0;
	ll rmaxx = 0;
	for (int i = 0; i < n; ++i)
	{
		if (i < k-1)
		{
			q.push(make_pair(-p[i].first*p[i].second,p[i].first));
			rmax.insert(p[i].first);
			bsum += p[i].first*p[i].second;
		}
		else
		{
			rmaxx = p[i].first;
			
			ans = max(ans, M_PI*(2*bsum +
						2*p[i].first*p[i].second 
						+ rmaxx*rmaxx));
			if (q.empty())
				continue;

			if (-q.top().first < p[i].first*p[i].second)
			{
				bsum += q.top().first;
				q.pop();
				q.push(make_pair(-p[i].first*p[i].second, p[i].first));
				bsum += p[i].first*p[i].second;
			}
		}
	}
	print_ans(test_num, out, ans);
}	