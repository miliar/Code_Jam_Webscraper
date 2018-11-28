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
	//ifstream in("B-large.txt");
	//cin.rdbuf(in.rdbuf());
	
	int t; cin >> t;
	rep(c, t){
		lli n, m; cin >> n;
		vector<int> v;
		while(n!=0){
			v.push_back(n%10);
			n/=10;
		}
		reverse(v.begin(), v.end());
		rep(cc, 20) rep(i, v.size()-1) if(v[i] > v[i+1]){
			v[i] = v[i] - 1;
			reg(j, i+1, v.size()-1) v[j] = 9;
			break;
		}
		cout << "CASE #" << c+1 << ": ";
		rep(i, v.size()) if(!(i==0&&v[i]==0)) cout << v[i];
		cout << endl;
	}

	return 0;
}