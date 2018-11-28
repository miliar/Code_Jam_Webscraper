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

//template <typename OutType, typename AnsType>
//void print_ans(int test_num, OutType& out, AnsType ans)
//{
//	out << "Case #" << test_num << ": " << ans << endl;
//}
template <typename OutType>
void print_ans(int test_num, OutType& out, double ans)
{
	out << "Case #" << test_num << ": ";
	out<< std::fixed<<setprecision(7)<< ans << endl;
}
template <typename OutType>
void print_ans(int test_num, OutType& out, vector<string> ans)
{
	out << "Case #" << test_num << ": " << endl;
	for (int i = 0; i < ans.size(); ++i)
		out << ans[i] << endl;
}

bool check(vector<pair<int, int>>& h, int d, double t,vector<double>& pr)
{
	double eps = 1e-10;
	int n = h.size();

	for (int i = 0; i < n; ++i)
	{
		if (t < pr[i])
			return false;
	}
	return true;
}

template<typename InType, typename OutType>
void proc_test(int test_num, InType& in, OutType& out)
{
	ll N, D;
	vll k, s;

	in >> D>> N;
	vector<pair<int, int>> h(N);
	int speed, position;
	for (int i = 0; i < N; ++i)
	{

		in >> position >> speed;
		h[i] = make_pair(position,speed);
	}
	
	sort(h.rbegin(), h.rend());
	vector<double> pr(N);
	for (int i = 0; i < N; ++i)
	{
		pr[i] = (D - h[i].first) / (double)(h[i].second);
	}
	double max_p = 0;
	for (int i = 0; i < N; ++i)
		max_p = max(pr[i], max_p);
	double time_l = 0;
	double time_h = 1000000001;
	double m;
	double t_min = (1e9)+1;
	/*for (int i = 0; i < N; ++i)
	{
		t_min = min(t_min, (D - h[i].first) / (double)h[i].second);
	}*/
	//while (abs(time_h - time_l) > 1e-7)
	//{
	//	m = (time_l + time_h) / 2.0;
	//	if (check(h, D, m,pr))
	//	{
	//		time_h = m;
	//	}
	//	else
	//		time_l = m;
	//}
	double ans = D / max_p;
	print_ans(test_num, out, ans);
}
