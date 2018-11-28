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

string problem_name = "B-small-attempt1(1)";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

char u[511][511][511][3];
char res[10010];
int ok = 0;
int f;
void go(int r, int g, int b, int prev, int pos)
{
	if (u[r][g][b][prev]) return;
	if (ok) return ;
	if (r+g+b==0) 
	{
		ok= 1;
		return;
	}
	u[r][g][b][prev] = 1;
	if (r+g+b==1)
	{
		if (r && (res[0]=='R' || res[pos-1]=='R')) return;
		if (g && (res[0]=='Y' || res[pos-1]=='Y')) return;
		if (b && (res[0]=='B' || res[pos-1]=='B')) return;
		if (r) res[pos]= 'R';
		if (g) res[pos]= 'Y';
		if (b) res[pos]= 'B';
		ok = 1;
		return;		
	}

	if (r && res[pos-1]!='R')
	{
		res[pos] = 'R';
		go(r-1,g,b,0,pos+1);
	}

	if (ok) return ;
	if (g && res[pos-1]!='Y')
	{
		res[pos] = 'Y';
		go(r,g-1,b,1,pos+1);
	}

	if (ok) return ;
	if (b && res[pos-1]!='B')
	{
		res[pos] = 'B';
		go(r,g,b-1,2,pos+1);
	}

}

int main()
{	
	init();	

	int tst;
	cin >> tst;

	for (int cas = 1; cas<=tst; cas++)
	{
		
		memset(u,0,sizeof(u));
		int n,r,g,b,v;
		cin >> n >> r >> g >> g >> v >> b >> v;
		
		if (r)
		{
			r--;
			res[0] = 'R';
		} else
		if (g)
		{
			g--;
			res[0] = 'Y';
		} else
		if (b)
		{
			b--;
			res[0] = 'B';
		}
		
		ok = 0;
		if (r>=510 || g>=510 || b>=510) ok=0; else
		go(r,g,b,0,1);
		
		res[n] = 0;
		if (!ok) printf("Case #%d: IMPOSSIBLE\n",cas); else
		{
			printf("Case #%d: %s\n",cas,res);
		}
		
		//if (!ok) printf("Case #%d: IMPOSSIBLE\n",cas); else
//		printf("Case #%d: %s\n",cas,res.c_str());
	}
	

	return 0;
}