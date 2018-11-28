#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <list>
#include <queue>

#include <math.h>
#include <set>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long
#define ull unsigned long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;

char get(int id) {
	if(id==0)return 'R';
	else if(id==1) return 'Y';
	else if(id==2) return 'B';
	return ' ';
}

string solve(int r,int y,int b) {
	int n = r+y+b;
	list<int> q;
	vector<pair<int,int> > ft;
	ft.push_back(make_pair(r,0));
	ft.push_back(make_pair(y,1));
	ft.push_back(make_pair(b,2));
	sort(ft.begin(),ft.end(), greater< pair<int,int> >());

	vector<int> tmp;
	vector<int> cur;

	for(int i = 0; i < ft.size();++i) {
		int t = ft[i].first;
		for(int j = 0; j < cur.size();++j) {
			tmp.push_back(cur[j]);

			int next_it = j + 1;
			if(next_it == cur.size() ) {
				next_it = 0;
			}
			if(t>0 && cur[j]==cur[next_it]) {
				tmp.push_back(ft[i].second);
				t--;
			}
		}
		cur = tmp;
		tmp.clear();

		for(int j = 0; j < cur.size();++j) {
			tmp.push_back(cur[j]);

			int next_it = j + 1;
			if(next_it == cur.size() ) {
				next_it = 0;
			}
			if(t>0 && cur[j]!=cur[next_it] && cur[j] != ft[i].second && cur[next_it] != ft[i].second) {
				tmp.push_back(ft[i].second);
				t--;
			}
		}

		cur = tmp;
		tmp.clear();

		while(t>0) {
			cur.push_back(ft[i].second);
			t--;
		}

		/*
		for(int j = 0; j < cur.size();++j){
			printf("%d ",cur[j]);
		}
		printf("\n");
		*/
	}

	string ans;
	for(int i = 0; i < cur.size();++i) {
		ans += get(cur[i]);
		int next_it = i + 1;
		if(next_it == cur.size() ) {
			next_it = 0;
		}
		if(cur[i] == cur[next_it]) {
			return "IMPOSSIBLE";
		}
	}

	return ans;
}


int main()
{
	int T;
	cin>>T;
	fr(ca,0,T) {
		int n;
		cin>>n;
		int r,o,y,g,b,v;
		cin>>r>>o>>y>>g>>b>>v;
		if(o==0&&g==0&&v==0) {
			printf("Case #%d: %s\n",ca+1,solve(r,y,b).c_str());
		}
	}
}
