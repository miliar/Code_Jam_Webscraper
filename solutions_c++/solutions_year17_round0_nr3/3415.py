#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cstring>
#include <unordered_map>

using namespace std;
typedef long long LL;

int n, k;
multiset<int, greater<int> > s;
multiset<int, greater<int> >::iterator it;

int main() {
	freopen("bathroom_stalls.in","r",stdin);
	freopen("bathroom_stalls.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		cin>>n>>k;
		s.clear();
		s.insert(n);
		for (int i=0;i<k-1;i++) {
			it=s.begin();
			int x=(*it-1)/2;
			int y=(*it-1)-x;
			s.insert(x);
			s.insert(y);
			s.erase(it);
		}
		it=s.begin();
		cout<<"Case #"<<nt++<<": "<<((*it-1)-(*it-1)/2)<<" "<<((*it-1)/2)<<endl;
	}
}
