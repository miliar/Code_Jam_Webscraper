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
	//in.open("B-small-attempt0.in",ios::in); out.open("B-small-0.out",ios::out);
	in.open("B-large.in",ios::in); out.open("B-large-0.out",ios::out);
	istream& input = in;
	ostream& output = out;

	ll case_id, total_case;

	input >> total_case;
	ll I, K, N, ans, AC, AJ, C, D, TC, TJ;
	for (case_id = 1; case_id <= total_case; case_id++)
	{
		// false =  C, true = J
		vector<tuple<ll, ll, bool>> v;
		input >> AC >> AJ;
		TC = TJ = 0;
		for (I = 0; I < AC; I++) {
			input >> C >> D;
			v.push_back(make_tuple(C, D, false));
			TC += D - C;
		}
		for (I = 0; I < AJ; I++) {
			input >> C >> D;
			v.push_back(make_tuple(C, D, true));
			TJ += D - C;
		}
		sort(v.begin(), v.end());
		bool overnight = false;
		ll minC, minJ, IC, IJ;
		while (true) {
			minC = minJ = 1440;
			for (I = 0; I < v.size(); ++I) {
				if (get<2>(v[I]) == get<2>(v[(I + 1) % v.size()])) {
					if (I != v.size() - 1) {
						if (get<2>(v[I]) == false && minC > get<0>(v[I+1]) - get<1>(v[I]) ) {
							minC = get<0>(v[I + 1]) - get<1>(v[I]);
							IC = I;
						}
						else if (get<2>(v[I]) && minJ > get<0>(v[I + 1]) - get<1>(v[I])) {
							minJ= get<0>(v[I + 1]) - get<1>(v[I]);
							IJ = I;
						}
					}
					else if (!overnight){
						if (get<2>(v[I]) == false && minC > 1440 + get<0>(v[0]) - get<1>(v[I])) {
							minC = 1440 + get<0>(v[0]) - get<1>(v[I]);
							IC = I;
						}
						else if (get<2>(v[I]) && minJ > 1440 + get<0>(v[0]) - get<1>(v[I])) {
							minJ = 1440 + get<0>(v[0]) - get<1>(v[I]);
							IJ = I;
						}
					}
				}
			}
			if (TC + minC <= 720) {
				//cout << 1 << " " << IC << endl;
				TC = TC + minC;
				if (IC != v.size() - 1) {
					get<1>(v[IC]) = get<1>(v[IC + 1]);
					v.erase(v.begin() + IC + 1);
				}
				else {
					overnight = true;
					get<0>(v[0]) = 0;
					get<1>(v[v.size() - 1]) = 1440;
				}
			} else if (TJ + minJ <= 720) {
				//cout << 2 << " " << IJ << endl;
				TJ = TJ + minJ;
				if (IJ != v.size() - 1) {
					get<1>(v[IJ]) = get<1>(v[IJ + 1]);
					v.erase(v.begin() + IJ + 1);
				}
				else {
					overnight = true;
					get<0>(v[0]) = 0;
					get<1>(v[v.size() - 1]) = 1440;
				}
			}
			else {
				break;
			}
		}
		ans = v.size();
		for (I = 0; I < v.size(); ++I) {
			if (get<2>(v[I]) == get<2>(v[(I + 1) % v.size()])) {
				ans++;
			}
		}
		if (overnight) ans-=2;
		output << fixed;
		output.precision(10);
		output << "Case #" << case_id << ": ";
		output << ans;
		output << endl;
	}
	return EXIT_SUCCESS;
}











