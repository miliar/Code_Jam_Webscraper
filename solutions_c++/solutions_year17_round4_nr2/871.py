#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

using namespace std;

void solve() {
	int N,C,M;
	cin >> N >> C >> M;
	vector<int> p(M),b(M),m(M,1),r(M);
	vector<set<int> > s(N+1,set<int>());
	for(int i = 0; i < M; i++) {
		cin >> p[i] >> b[i];
		s[p[i]].insert(b[i]);
		r[i] = i;
	}
	sort(r.begin(),r.end(),[&p,&s](int i,int j){
			if(p[i]==1 && p[j]!=1) return true;
			if(p[i]!=1 && p[j]==1) return false;
			return s[p[i]].size() > s[p[j]].size();
			});
	vector<int> p1(M),b1(M);
	for(int i = 0; i < M; i++) {
		p1[i] = p[r[i]];
		b1[i] = b[r[i]];
		//cout << p1[i] << " " << b1[i] << endl;
	}
	p = p1;
	b = b1;
	int x,y;
	x = y = 0;
	for(int i = 0; i < M; i++) if(m[i]==1 && b[i]==1) {
		for(int j = i+1; j < M; j++) if(m[j]) {
			if(b[i]!=b[j] && p[i]!=p[j]) {
				x++;
				m[i] = m[j] = 0;
				break;
			}
		}
	}
	for(int i = 0; i < M; i++) if(m[i]) {
		for(int j = i+1; j < M; j++) if(m[j]) {
			if(b[i]!=b[j] && p[i]!=p[j]) {
				x++;
				m[i] = m[j] = 0;
				break;
			}
		}
	}
	for(int i = 0; i < M; i++) if(m[i]) {
		for(int j = i+1; j < M; j++) if(m[j]) {
			if(b[i]!=b[j] && p[i]==p[j] && p[i]>1) {
				x++;
				y++;
				m[i] = m[j] = 0;
				break;
			}
		}
	}
	for(int i = 0; i < M; i++) if(m[i]) {
		x++;
		m[i] = 0;
	}
	cout << x << " " << y << endl;

}

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		solve();
	}
}

