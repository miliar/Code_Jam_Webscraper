/*
By oAT * : ))
LANG: C++
*/
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <string>
using namespace std;

#define INF (1<<31)-1
#define minusINF 1<<31
#define EFF 1e-6
#define FOR(i , u , v) for(__typeof(v)i = u; i < v; i++)
#define TR(it , c) for(__typeof((c).end()) it = (c).begin(); it != (c).end(); it++)
#define pii pair<int , int >
#define vi vector<int >
#define vii vector<pii >
#define si set<int >
#define sii set<pii >
#define qi queue<int >
#define qii queue<pii >

#define x first
#define y second

#define mp make_pair
#define pb push_back

// memset(a , 0 , n*sizeof(a[0]));
// fill(a , a+n , INF);

bool chk (string s)
{
	int lastPos = 0;
	TR(it , s)
	{
		int thisPos = *it+'0';
		if(*it < '0' || *it > '9') return false;
		if(lastPos > thisPos)
		{
			return false;
		}
		lastPos = thisPos;
	}
	return true;

}
void solve(int tt)
{
	string in ;
	printf("Case #%d: ",tt);
	cin >> in;
	char out[100];
	strcpy(out, in.c_str());
	
	int s = in.size()-1;
	while(s > 0)
	{
		// cout << out << endl;
		if(chk(out)) break;
		out[s] = '9';
		out[s-1]--;
		s--;
	}
	in = out;
	
	if(out[0] == '0') in = in.substr(1);

	cout << in << endl;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int tCase;
	cin >> tCase;
	FOR(tt , 0 , tCase)
		solve(tt+1);
	return 0;
}
