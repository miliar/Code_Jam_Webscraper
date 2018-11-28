/*
*/

#pragma GCC optimize("O3")
#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>

#include <memory.h>
#include <assert.h>

#define y0 sdkfaslhagaklsldk

#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define norm asdfasdgasdgsd
#define have adsgagshdshfhds
#define ends asdgahhfdsfshdshfd

#define eps 1e-12
#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 200

#define ldouble long double

using namespace std;

long long INF = 1e9;
const int N = 500031;

int tests,ts;
string st;

string get_st(int dig,int len)
{
	string res="";
	for (int i=0;i<len;i++)
	{
		res+=char(dig+48);
	}
	return res;
}

bool is_ok(string st)
{
	for (int i=1;i<st.size();i++)
	{
		if (st[i]<st[i-1])
		return false;
	}
	return true;
}

string make_eval(string st,int ps,int val)
{
	for (int i=ps+1;i<st.size();i++)
	{
		st[i]='9';
	}
	st[ps]=val+48;
	return st;
}

int main(){
	//freopen("tree.in","r",stdin);
	//freopen("tree.out","w",stdout);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	//cin.tie(0);

	cin>>tests;
	for (;tests;--tests)
	{
		cin>>st;
		++ts;
		cout<<"Case #"<<ts<<": ";
		if (is_ok(st))
		{
			cout<<st<<endl;
			continue;
		}
		if (get_st(1,st.size())>st)
		{
			string temp=get_st(9,st.size()-1);
			cout<<temp<<endl;
			continue;
		}

		int found=0;

		for (int i=st.size()-1;i>=0;--i)
		{
			for (int j=9;j>=0;--j)
			{
				if (j+48>=st[i])
					continue;
				string here=make_eval(st,i,j);
				if (!is_ok(here))
					continue;
				if (found)
					continue;
				found=1;
				cout<<here<<endl;
			}
		}

	}

	cin.get(); cin.get();
	return 0;
}
