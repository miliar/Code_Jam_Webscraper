// ConsoleApplication1.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<sstream>
#include<string>
#include<iterator>
#include<functional>
#include<time.h>
#include<iomanip>
#include<queue>
#include<utility>
#include<array>
#include<deque>
#include<tuple>
#include <limits>
#include<numeric>
using namespace std;
typedef long long int ll;
typedef long double ld;
#define INF 100000000000000000LL

ll diff(ll a, ll b)
{
	return a > b ? a - b : b - a;
}
/*
#define COMB_NUM 3001L
ld comb[COMB_NUM][COMB_NUM];
//need init_comb();
void init_comb()
{
	comb[0][0] = 1;
	ll i, j;
	for (i = 1; i < COMB_NUM; i++)
	{
		comb[i][0] = comb[i][i] = 1;
		for (j = 1; j < i; j++)
			comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1];
	}
}
*/

#define print(a)      for(int i=0;i<a.size();i++) cout<<a[i]<<" "; cout<<endl;
#define print2n(a,n)      for(int i=0;i<=n;i++) cout<<a[i]<<" "; cout<<endl;

void llFromString(const string &s, ll &a, ll &b)
{
	string replacedString = s;
	replace_if(replacedString.begin(),
		replacedString.end(),
		bind2nd(equal_to<char>(), '.'),
		' ');

	istringstream buffer(replacedString);
	buffer >> a;
	if (buffer.good())
	{
		buffer >> b;
	}
	else
	{
		b = 0;
	}
}


template<class T>
vector<T> split(const std::string &s) {

	string replacedString = s;
	replace_if(replacedString.begin(),
		replacedString.end(),
		bind2nd(equal_to<char>(), '.'),
		' ');

	vector<T> ret;
	istringstream buffer(replacedString);
	copy(istream_iterator<T>(buffer),
		istream_iterator<T>(), back_inserter(ret));
	return ret;
}// vector<ll> k = split<ll>(s);

int main()
{
	fstream in, out;
	//in.open("test.in.txt", ios::in);	out.open("test.out.txt", ios::out);
	//in.open("A-small-attempt0.in",ios::in); out.open("A-small-0.out",ios::out);
	in.open("A-large.in",ios::in); out.open("A-large-0.out",ios::out);
	istream& input = in;
	ostream& output = out;

	ll case_id, total_case;

	input >> total_case;
	ll I, K, N, ans1, ans2, ans;
	ll R[1001], H[1001], rmax;
	for (case_id = 1; case_id <= total_case; case_id++)
	{
		input >> N >> K;
		rmax = 0;
		for (I = 0; I < N; ++I) {
			input >> R[I] >> H[I];
			if (R[I] > R[rmax] || (R[I] == R[rmax] && H[I] > H[rmax])) rmax = I;
		}
		ll index[1001];
		iota(index, index + N, 0);
		sort(index, index + N, [&](ll a, ll b) {return  R[a] * H[a] > R[b] * H[b]; });
		bool isIn = false;
		ll nr = 0;
		ans1 = 0;
		ans2 = 0;
		for (I = 0; I < K; I++) {
			ans1 += 2*R[index[I]] * H[index[I]];
			if (index[I] == rmax) isIn = true;
			if (R[index[I]] > nr) nr = R[index[I]];
		}
		if (isIn == false) {
			ans2 = ans1 - 2*R[index[K-1]] * H[index[K-1]];
			ans2 += 2* R[rmax] * H[rmax];
			ans2 += R[rmax] * R[rmax];
		}
		else {
			ans2 = ans1;
		}
		ans1 += nr*nr;
		ans = max(ans1, ans2);
	ANS:
		ld PI = 3.14159265358979323846264338327950288419716939937510;
		output << fixed;
		output.precision(10);
		output << "Case #" << case_id << ": ";
		output << (ld) ans * PI;
		output << endl;
	}
	return EXIT_SUCCESS;
}











