#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <cassert>
#include <stack>
#include <string>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>

using namespace std;

#define REP(i, a, b) for (int i = (a); i < (int)(b); i++)
#define REPE(i, a, b) for (int i = (a); i <= (int)(b); i++)
#define REPD(i, a, b) for (int i = (a); i >= (int)(b); i--)
#define ll long long
#define vl vector<long long>
#define vll vector<vector<long long>>
#define vi vector<int>
#define vii vector<vector<int>>
#define pll pair<long,long>
#define ppl pair<pll,pll>

#define DEBUG 10

#if DEBUG == 10
#define cout outfile
#define cerr outfile
#define clog outfile
#endif

pair<ll, ll> rl(vector<bool> stall, ll pos)
{
    int n = stall.size();
    int i = pos - 1, j = pos + 1, l = 0, r = 0;
    while (i >= 0)
    {
	if (stall.at(i))
	    break;
	i--;
	l++;
    };
    while (j < n)
    {
	if (stall.at(j))
	    break;
	j++;
	r++;
    };
    return make_pair(min(l, r), max(l, r));
}

int main(void)
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ifstream infile("infile");
    ofstream outfile("outfile.txt");
    long long testcases = 1;
    infile >> testcases;
    // cout<<111111111111111120-10<<endl;
    REPE(testcase, 1, testcases)
    {
	ll n, k;
	infile >> n >> k;
	ll pos = -1;
	pair<ll, ll> m;
	vector<bool> stall(n, false);
	REPE(j, 1, k)
	{
	    m = {INT_MIN, INT_MIN};
	    // cout << pos << "\t";
	    REP(i, 0, n)
	    {
			if(stall[i]) continue;
			if (m < rl(stall, i))
			{
				m = rl(stall, i);
				pos = i;
			};
	    };
	    stall[pos] = true;
	};
	// REP(i, 0, n)
	// cout << stall[i] << " ";
	// cout << endl;
    cout<<"Case #"<<testcase<<": ";
	cout << m.second << " " << m.first << endl;

	// REP(i, 0, n)
	// {
	//     if (m < rl(stall, i))
	//     {
	// 	m = rl(stall, i);
	// 	pos = i;
	//     };
	// };
	// cout << m.first << " " << m.second << endl;
    }
    return 0;
};