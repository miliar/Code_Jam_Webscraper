#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
//#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <malloc.h>

//#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <cctype>
#include <cmath>
#include <cstdlib>
//#include <stdint.h>
#include <unistd.h>
#include <ctime>
#include <climits>
using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define T           top()
#define P           pop()
#define NL 			printf("\n")

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vstr;
typedef long long LL;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("salida.out","w",stdout);
	int t,k,count;
	string s;
	cin>>t;
	F(i,t)
	{
		cin>>s>>k;
		count = 0;
		F(j,s.S) {
			if(s[j] == '-') {
				if((j + k) <= s.S) {
					FOR(m, j, j + k) {
						if(s[m] == '-') {
							s.replace(m,1,'+');
						} else {
							s.replace(m,1,'-');
						}
					}
					count++;
				} else {
					count = -1;
				}
			}
		}
		if(count >= 0) {
			printf("Case #%d: %d\n",i+1, count);
		} else {
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}
	}
}
