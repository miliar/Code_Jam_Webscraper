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
#define rep_(i,j,k) for(k::iterator i=j.begin();i!=j.end();i++)
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

long long a,p,q,k;

void pr(int T,long long a)
{
	a-=2;
	cout << "case #" << T << ": " << (a+1)/2 << ' ' << a/2 << endl;
}

void pp(int T)
{
	p=1;q=0;
	cin >> a >> k;
	while (1)
	{
		if ((k-=p)<=0) {pr(T,a+1);return;}
		if ((k-=q)<=0) {pr(T,a);return;}
		if (a&1) p+=p+q;
		else q+=p+q;
		a>>=1;
		// cout << a << p << q << endl;
	}
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
