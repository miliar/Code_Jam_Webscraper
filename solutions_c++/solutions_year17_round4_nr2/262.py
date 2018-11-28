#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

int main()
{
#ifdef ACMTUYO
	freopen("B-large(1).in","r",stdin);
	freopen("B-large(1)).out","w",stdout);
#endif
	int C;
	cin >> C;
	forn(tc, C) {
		int n, c, m;
		cin >> c >> n >> m;
		//cout << n << ' ' << c << ' ' << m << endl;
		vector<int> tickets(c, 0);
		vector<int> people(n, 0);
		
		forn(i, m) {
			int s, b;
			cin >> s >> b;
			s--;b--;
			//cout << s << ' ' << b << endl;
			tickets[s]++;
			people[b]++;
		}
		
		int ans = 0;
		forn(i, n) {
			ans = max(ans, people[i]);
		}
		
		int top=m, bot=ans-1;
		while(top-bot>1){
			int mid =(top+bot)/2;
			int left = 0, anda = 1;
			forn(i, c) {
				left += mid - tickets[i];
				if(left<0) anda = 0;
			}
			
			if(anda) {
				top = mid;
			}
			else
			{
				bot = mid;
			}
		}
		
		int move = 0;
		forn(i, c) {
			move += max(0, tickets[i]-top);
		}
		
		cout << "Case #" << tc+1 << ": "; 
		cout << top << ' ' << move << endl;
	}
}
