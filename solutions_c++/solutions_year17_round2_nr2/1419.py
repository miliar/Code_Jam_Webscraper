// ConsoleApplication1.cpp : �w�q�D���x���ε{�����i�J�I�C
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
	in.open("B-small-attempt0.in",ios::in); out.open("B-small-0.out",ios::out);
	//in.open("B-large.in",ios::in); out.open("B-large-0.out",ios::out);
	istream& input = in;
	ostream& output = out;

	ll case_id, total_case;

	input >> total_case;
	ll I, H, K, D, N, S;
	ll R, O, Y, G, B, V;
	string ans;
	for (case_id = 1; case_id <= total_case; case_id++)
	{
		input >> N;
		input >> R >> O >> Y >> G >> B >> V;
		vector<pair<ll, string>> p(3, make_pair(0, ""));
		p[0] = make_pair(R, "R");
		p[1] = make_pair(Y, "Y");
		p[2] = make_pair(B, "B");
		sort(p.begin(), p.end());
		/*cout<<p[0].first<<p[0].second<<endl;
		cout << p[1].first << p[1].second << endl;
		cout << p[2].first << p[2].second << endl;
		*/
		ans = "";
		if (p[2].first > p[1].first + p[0].first) {
			ans = "IMPOSSIBLE";
			goto ANS;
		}
		while (p[2].first) {
			ans = ans + p[2].second;
			p[2].first--;
			if (p[1].first) {
				ans = ans + p[1].second;
				p[1].first--;
			}
			else {
				ans = ans + p[0].second;
				p[0].first--;
			}

		}
		for (I = 1; p[0].first != 0;I+=2) {
			ans.insert(I, p[0].second);
			p[0].first--;
		}
ANS:
		output << fixed;
		output.precision(10);
		output << "Case #" << case_id << ": ";
		output << ans;
		output << endl;
	}
	return EXIT_SUCCESS;
}











