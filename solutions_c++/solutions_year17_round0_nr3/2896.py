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

string problem_name = "C-large";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

map <long long, long long>  mp;

int main()
{	
	init();	

	int tst;
	cin >> tst;

	for (int cas = 1; cas<=tst; cas++)
	{
		
		mp.clear();
		long long n,k;
		cin >> n >> k;
		mp[n] = 1;
		
		while (1)
		{
			map <long long, long long> ::iterator it = mp.end();
			it--;
			pair <long long, long long> val;
			val.first = (*it).first;
			val.second = (*it).second;
		
			val.first--;
			if (val.second>=k)
			{
				printf("Case #%d: %lld %lld\n",cas,val.first - val.first/2,val.first/2);			
				break;
			} else
			{
				k-=val.second;
				mp.erase(it);
				
				mp[val.first/2]+=val.second;
				mp[val.first - val.first/2]+=val.second;
				
				
			}
		}
		
	
		//if (!ok) printf("Case #%d: IMPOSSIBLE\n",cas); else
//		printf("Case #%d: %s\n",cas,res.c_str());
	}
	

	return 0;
}