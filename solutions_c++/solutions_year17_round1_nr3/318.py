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

int mh, ma, hh, ha;
int b, d;
//unordered_map<pair< pair<int, int>, pair<int, int> >, int , pair_hash> a;
map<pair< pair<int, int>, pair<int, int> >, int> a;
queue<int> q1, q2, q3, q4;

/*struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        return h1 ^ h2;  
    }
};*/

void go(int h1, int a1, int h2, int a2, int v) {
	pair<int, int> p1=make_pair(h1, a1);
	pair<int, int> p2=make_pair(h2, a2);
	if (a.count(make_pair(p1, p2))) return;
	a[make_pair(p1, p2)]=v;
	q1.push(h1);q2.push(a1);q3.push(h2);q4.push(a2);
}

int main() {
	freopen("play_the_dragon.in","r",stdin);
	freopen("play_the_dragon.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		cin>>mh>>ma>>hh>>ha>>b>>d;
		while (!q1.empty()) q1.pop();
		while (!q2.empty()) q2.pop();
		while (!q3.empty()) q3.pop();
		while (!q4.empty()) q4.pop();
		a.clear();
		go(mh, ma, hh, ha, 0);
		bool ok=false;
		cout<<"Case #"<<nt++<<": ";
		while (!q1.empty()) {
			int h1=q1.front();q1.pop();
			int a1=q2.front();q2.pop();
			int h2=q3.front();q3.pop();
			int a2=q4.front();q4.pop();
			int c=a[make_pair(make_pair(h1, a1), make_pair(h2, a2))];
			if (h2<=a1) {
				cout<<c+1<<endl;
				ok=true;
				break;
			}
			if (h1>a2) {
				go(h1-a2, a1, h2-a1, a2, c+1);
			}
			if (mh>a2) {
				go(mh-a2, a1, h2, a2, c+1);
			}
			if (b!=0 && h1>a2 && a1<100000) {
				go(h1-a2, a1+b, h2, a2, c+1);
			}
			if (d!=0 && h1>max(0, a2-d) && a2>0) {
				go(h1-max(0, a2-d), a1, h2, max(0, a2-d), c+1);
			}
		}
		if (!ok) cout<<"IMPOSSIBLE"<<endl;
	}
}
