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

int tests,len;
string st;
int ts;

int find_minus(string st)
{
	for (int i=0;i<st.size();i++)
	{
		if (st[i]=='-')
			return i;
	}
	return -1;
}

int solver(string st,int len)
{
	int res=0;

	while (true)
	{
		int fp=find_minus(st);
		if (fp==-1)
			break;
		if (fp+len>st.size())
		{
			return -1;
		}
		++res;
		for (int i=fp;i<fp+len;i++)
		{
			if (st[i]=='-')
				st[i]='+';
			else
				st[i]='-';
		}
	}
	return res;
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
		cin>>len;
		int here=solver(st,len);
		++ts;
		cout<<"Case #"<<ts<<": ";
		if (here==-1)
			cout<<"IMPOSSIBLE";
		else
			cout<<here;
		cout<<endl;
	}

	cin.get(); cin.get();
	return 0;
}
