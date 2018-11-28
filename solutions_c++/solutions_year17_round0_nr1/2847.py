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

string problem_name = "A-large(8)";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}


int main()
{	
	init();	

	int tst;
	cin >> tst;

	for (int cas = 1; cas<=tst; cas++)
	{
		string s;
		int k;
		cin >> s >> k;
		int res = 0;
		int ok = 1;
		for (int i=0;i<sz(s);i++)
			if (s[i]=='-')
			{
				res++;
				if (sz(s)-i<k) ok=0; else
					for (int j=i;j<i+k;j++)
						if (s[j]=='+') s[j]='-'; else
							s[j] = '+';
			}
	
		if (!ok) printf("Case #%d: IMPOSSIBLE\n",cas); else
		printf("Case #%d: %d\n",cas,res);
	}
	

	return 0;
}
