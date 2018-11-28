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

#include <limits>
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
	ll I, H, K, ans, R, C;
	char c[26][26];
	for (case_id = 1; case_id <= total_case; case_id++)
	{
		input >> R >> C;
		for (I = 0; I < R; ++I)
			for (H = 0; H < C; ++H)
				input >> c[I][H];
		bool start = false;
		for (I = 0; I < R; ++I) {
			char first = 0;
			for (H = 0; H < C; ++H) {
				if (c[I][H] != '?') {
					first = c[I][H];
					break;
				}
			}
			if (first == 0) {
				if (!start) continue;
				else {
					for (H = 0; H < C; ++H) c[I][H] = c[I - 1][H];
				}
				continue;
			}
			char t = 0;
			for (H = 0; H < C; ++H) {
				if (c[I][H] == '?') {
					if (t != 0) c[I][H] = t;
					else {
						c[I][H] = first;
					}
				}
				else {
					t = c[I][H];
				}
			}
			if (!start) {
				for (K = 0; K < I; ++K)
					for (H = 0; H < C; H++)
						c[K][H] = c[I][H];
				start = true;
			}
		}
		//output << fixed;
		//output.precision(10);
		output << "Case #" << case_id << ": " <<endl;
		//output << ans;
		for (I = 0; I < R; I++) {
			for (H = 0; H < C; H++) {
				output << c[I][H];
			}
			output << endl;
		}
		//output << endl;
	}
	return EXIT_SUCCESS;
}











