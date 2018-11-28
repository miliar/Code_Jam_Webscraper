#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <algorithm>
#include <cstdio>
//#include <intrin.h>
#include <iomanip>
#include <string>
using namespace std;



typedef long long ll;

template<typename InType, typename OutType>
void p_test(int test_num, InType& in, OutType& out);

int main()
{
	string in_path = "..//..//input.in";
	string out_path = "..//..//output.txt";

	std::ifstream in(in_path.c_str());
	ofstream out(out_path.c_str());
	int test_num;
	in >> test_num;
	for (int i = 0; i < test_num; ++i)
	{
		p_test(i+1,in,out);
	}
}

template <typename OutType, typename T>
void p_ans_(OutType& out, T& arg)
{
	out << " " << arg;
}

template <typename O, typename T, typename ...A>
void p_ans_(O& out, T& arg, A& ...argss)
{
	out << " " << arg;
	p_ans_(out, argss...);
}

template <typename O, typename ...A>
void print_ans(int test_num, O& out, A ...ans)
{
	out << "Case #" << test_num << ":";
	p_ans_(out,ans...);
	out << endl;
}
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

	}
}


template<typename InType, typename OutType>
void p_test(int test_num, InType& in, OutType& out)
{
	ll n, k;
	in >>n>>k;
	ll ls, rs;
	f(n, k, ls, rs);
	ll lsa, rsa;
	lsa = max(ls, rs);
	rsa = min(ls, rs);
	print_ans(test_num, out, lsa, rsa);
}



