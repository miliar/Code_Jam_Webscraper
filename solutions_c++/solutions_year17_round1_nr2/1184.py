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
	in.open("B-small-attempt1.in",ios::in); out.open("B-small-0.out",ios::out);
	//in.open("B-large.in",ios::in); out.open("B-large-0.out",ios::out);
	istream& input = in;
	ostream& output = out;

	ll case_id, total_case;

	input >> total_case;
	ll I, H, K, ans, R[51], N, P;
	for (case_id = 1; case_id <= total_case; case_id++)
	{
		input >> N >> P;
		//cout << "R ";
		for (I = 0; I < N; ++I) {
			input >> R[I];
			//cout << R[I];
		}
		//cout << endl;
		ans = 0;
		deque < pair <ll, ll> > v[51];
		for (I = 0; I < N; I++) {
			for (H = 0; H < P; ++H) {
				ll t, low, up;
				input >> t;
				//cout << t << " ";
				low = (t * 10) /( R[I] * 11);
				if ((t * 10) % (R[I] * 11)) low++;
				//if (t * 10 < R[I] * 9) continue;
				up = (t * 10) /( R[I] * 9);
				//cout << low << " " << up << endl;
				if (low <= up) {
					v[I].push_back(make_pair(low, up));
					//cout << "x" << endl;
				}
			}
			sort(v[I].begin(), v[I].end());
		}
		for (I = 0; I < N; ++I) {
			if (v[I].empty()) goto ANS;
		}
	
		ll srv = 1;
		while (!v[0].empty()) {
			bool s = false;
			for (srv = v[0][0].first; srv <= v[0][0].second; srv++) {
				for (I = 1; I < N; I++) {
					if (srv < v[I][0].first) break;
					if (srv > v[I][0].second) {
						v[I].pop_front();
						if (v[I].empty()) goto ANS;
						I--;
						continue;
					}
				}
				if (I != N) continue;
				ans++;
				for (I = 0; I < N; I++) {
					v[I].pop_front();
					if (v[I].empty()) goto ANS;
				}
				s = true;
			}
			if (!s) v[0].pop_front();
		}
		
		//output << fixed;
		//output.precision(10);
ANS:
		output << "Case #" << case_id << ": ";
		output << ans;
		output << endl;
	}
	return EXIT_SUCCESS;
}











