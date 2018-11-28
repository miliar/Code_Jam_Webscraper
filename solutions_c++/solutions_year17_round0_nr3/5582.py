#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<climits>
#include<string>
#include<set>
#include<map>
#include<iostream>
using namespace std;
#define rep(i,n) for(int i = 0;i<((int)(n));i++)
#define reg(i,a,b) for(int i = ((int)(a));i<=((int)(b));i++)
#define irep(i,n) for(int i = ((int)(n)-1);i>=0;i--)
#define ireg(i,a,b) for(int i = ((int)(b)-1);i>=((int)(a));i--)
typedef long long int lli;
typedef pair<int, int> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define pque(type) priority_queue<type,vector<type>,greater<type> >
#define memst(a,b) memset(a,b,sizeof(a))

//#include <fstream>

int main(void){
	//ifstream in("C-small-2.txt");
	//cin.rdbuf(in.rdbuf());
	int t; cin >> t;
	rep(c, t){
		lli n, k; cin >> n >> k;
		if(n==k){cout << "CASE #" << c+1 << ": 0 0" << endl; continue;}
		priority_queue<int> q; q.push(n); int p;
		rep(i, k){
			p = q.top(); q.pop(); p--;
			if(p == 0) continue;
			else{
				if(p/2 != 0) q.push(p/2);
				if(p - p/2 != 0) q.push(p - p/2);
			}
		}
		cout << "CASE #" << c+1 << ": " << p - p/2 << " " << p/2 << endl;
	}

	return 0;
}