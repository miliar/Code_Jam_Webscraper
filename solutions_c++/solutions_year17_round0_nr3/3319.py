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

template <typename OutType, typename T>
void print_ans_(OutType& out, T& arg)
{
	out << " " << arg;
}

template <typename OutType, typename T, typename ...Args>
void print_ans_(OutType& out, T& arg, Args& ...argss)
{
	out << " " << arg;
	print_ans_(out, argss...);
}

template <typename OutType, typename ...AnsType>
void print_ans(int test_num, OutType& out, AnsType ...ans)
{
	out << "Case #" << test_num << ":";
	print_ans_(out,ans...);
	out << endl;
}


//ls = min_max rs = max_ds
void f(ll n, ll k, ll& ls, ll& rs)
{
	ll lsa, rsa,lsa1,rsa1;
	if (k == 1ll)
	{
		ls = (n - 1ll) / 2ll;
		rs = n - 1ll - ls;
		return;
	}
	if (n == 1ll)
	{
		ls = 0;
		rs = 0;
	}
	if (n == 2ll)
	{
		if (k == 1ll)
		{
			ls = 0;
			rs = 1ll;
		}
		else
		{
			ls = 0;
			rs = 0;
		}
	}
	if (n % 2ll == 1ll)
	{
		f(n / 2ll, k / 2ll, lsa, rsa);
		ls = lsa;
		rs = rsa;
	}
	else
	{
		if ((k-1ll) %2ll == 1ll)
		{
			f(n/2ll, k/2ll, lsa, rsa);
		}
		else
		{
			f(n / 2ll -1ll, k / 2ll, lsa, rsa);
		}
		ls = lsa;
		rs = rsa;
	//	f((n -1ll)/ 2ll, (k-1ll) / 2ll, lsa, rsa);
	//	f(n - (n - 1ll) / 2ll, k - (k - 1ll) / 2ll, lsa1, rsa1);
	//	if (max(lsa, rsa) < max(lsa1, rsa1))
	//	{
	//		ls = lsa;
	//		rs = rsa;
	//	}
	//	else
	//	{
	//		if (max(lsa, rsa) < max(lsa1, rsa1))
	//		{
	//			ls = lsa1;
	//			rs = rsa1;
	//		}
	//		else
	//		{
	//			ls = lsa;
	//			rs = rsa;
	//		}
	//	}
	}
}

void brute_force(ll n, ll k, ll& lsa, ll& rsa);

template<typename InType, typename OutType>
void proc_test(int test_num, InType& in, OutType& out)
{
	ll n, k;
	in >> n >> k;
	ll ls, rs;
	f(n, k, ls, rs);
	ll lsa, rsa;
	lsa = max(ls, rs);
	rsa = min(ls, rs);
	print_ans(test_num, out, lsa, rsa);
	//ll lsab, rsab;
	//brute_force(n, k, lsab, rsab);
		//print_ans(test_num, out, "bruteforce:", lsab, rsab);

}

void brute_force(ll n, ll k, ll& lsa, ll& rsa)
{
	vector<bool> st(n + 2, false);
	st[0] = true;
	st[n + 1] = true;


	for (; k>0;--k )
	{
		ll max_min = -1;
		ll max_ds = -1;
		ll st_best;
		for (int j = 1; j <= n ; ++j)
		{
			if (st[j])
				continue;
			int ls = j-1;
			int rs = j+1;
			while (!st[ls])
				ls--;
			while (!st[rs])
				rs++;
			ls = j - ls-1;
			rs = rs - j-1;
			if (max_min < min(ls, rs))
			{
				max_min = min(ls, rs);
				max_ds = max(ls, rs);
				st_best = j;
			}
			else
			{
				if ((max_min == min(ls, rs))&&max_ds < max(ls, rs))
				{
					max_min = min(ls, rs);
					max_ds = max(ls, rs);
					st_best = j;
				}
			}
		}
		st[st_best] = true;
	/*	cout << st << endl;
		system("pause");*/
		if (k == 1)
		{
			rsa = max_min;
			lsa = max_ds;
		}
	}

}
