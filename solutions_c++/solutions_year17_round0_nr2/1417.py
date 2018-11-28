#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

void solve(int prim){
	string s;
	cin >> s;
	for(int i = s.length()-1;i>=1;i--){
		if(s[i]>=s[i-1])continue;
		s[i-1]--;
		FORR(j,i,s.length())s[j]='9';
	}
	int stnul;
	for(stnul=0;s[stnul]=='0';stnul++);
	cout << "Case #"<<prim<<": ";
	FORR(i,stnul,s.length())cout<<s[i];cout<<"\n";
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
