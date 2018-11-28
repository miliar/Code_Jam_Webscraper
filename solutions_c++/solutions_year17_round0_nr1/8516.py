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
#include <sstream>
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
#define MAX 1000
set<pair<int , string> > heap;
set<string > found;
char in[MAX+5];
void solve(int tt)
{
	int k , len;
	stringstream ss;
	printf("Case #%d: ",tt);
	cin >> in;
	cin >> k;
	len = strlen(in);
	string goal = "";
	FOR(i , 0 , len)
		goal += '+';
	goal[len] = in[len];
	// cout << "AA " << goal << endl;
	heap.clear();
	found.clear();
	// ss << goal;
	// string tmp ;
	// ss >> tmp;
	heap.insert(mp(0 , in));
	found.insert(in);
	while(!heap.empty())
	{
		pair<int , string> pp = *heap.begin();
		// cout << pp.x << " " << pp.y << endl;
		heap.erase(heap.begin());
		if(goal.compare(pp.y) == 0)
		{
			cout << pp.x << endl;
			return;
		}
		FOR(i , 0 , len-k+1)
		{
			string tmp = pp.y;
			FOR(j , i , i+k)
				tmp[j] = (tmp[j] == '+')?'-':'+';
			int cnt_found = found.size();
			found.insert(tmp);
			if(cnt_found < found.size())
				heap.insert(mp(pp.x+1 , tmp));
		}
	}
	cout << "IMPOSSIBLE" << endl;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);
	int tCase;
	cin >> tCase;
	FOR(tt , 0 , tCase)
		solve(tt+1);
	return 0;
}
