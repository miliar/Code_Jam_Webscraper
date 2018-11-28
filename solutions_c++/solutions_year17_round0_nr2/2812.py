#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large(5)";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

int dp[111][11][2];

string res;
string s;
void go(string cur, int pos, int last, int e)
{
	if (pos==sz(s))
	{
		if (sz(res)) return;
		res = cur;
	}
	if (dp[pos][last][e]!=0) return;
	dp[pos][last][e] = 1;

	int mx = 9;
	if (e) mx = s[pos]-'0';

	for (int i=mx;i>=last;i--)
	{
		go(cur+string(1,'0'+i), pos+1,i,e && (i==s[pos]-'0'));	
	}

	
	return ;
}

int main()
{	
	init();	

	int tst;
	cin >> tst;

	for (int cas = 1; cas<=tst; cas++)
	{
		
		
		memset(dp,0,sizeof(dp));

		cin >> s;
		s="0"+s;
		res="";
		go("",0,0,1);
		while (res[0]=='0') res.erase(res.begin());

		//if (!ok) printf("Case #%d: IMPOSSIBLE\n",cas); else
		printf("Case #%d: %s\n",cas,res.c_str());
	}
	

	return 0;
}