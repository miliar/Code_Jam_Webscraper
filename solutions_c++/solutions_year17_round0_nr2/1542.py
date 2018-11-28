using namespace std;
#include <cstdlib>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define rep(i,j,k) for(int i=j;i<k;i++)
#define Rep(i,j,k) for(int i=j;i>k;i--)
#define rep_(i,j,k) for(k::iterator i=j.begin();i!=j.end();i++)
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

string s;
bool f[20];
long long a;

void pp(int T)
{
	a=0;
	memset(f,0,sizeof(f));
	cin >> s;
	Rep(i,s.length()-1,0)
		if (s[i-1]>s[i]) s[i-1]--,f[i]=true;
	rep(i,0,s.length())
		a=a*10+((f[i])?9:s[i]-48),f[i+1]|=f[i];
	cout << "case #" << T << ": " << a << endl;
}

int main()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int TT;
	cin >> TT;
	rep(T,1,TT+1) pp(T);
	return 0;
}

/*
Usage:
	cin >> n;  rep(i,0,n);
	set<int> s;rep_(i,s,set<int>);
*/
