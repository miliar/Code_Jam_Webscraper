#include <iostream>
#include <set>

using namespace std;

typedef struct Range{
	int a, b;
	bool operator < (const Range& r) const {
		if(b - a == r.b - r.a){
			return a < r.a;
		}
		return b - a > r.b - r.a;
	}
} Range;

int n, k;
int R, L;

void solve(){
	set<Range> s[2];
	set<Range> l;
	int c = 0;
	Range start; start.a = 1; start.b = n;
	s[c].insert(start);

	while(1){
		if(s[c].empty()) break;
		set<Range>::iterator it = s[c].begin();
		while(it != s[c].end() ){
			Range r1, r2;
			int mid = (it->b + it->a)/2;
			r1.a = it->a; r1.b = mid-1;
			r2.a = mid+1; r2.b = it->b;
			L = mid - it->a; R = it->b - mid;
			if(r1.b - r1.a > 0) s[(c+1)%2].insert(r1);
			else if(r1.b - r1.a == 0) l.insert(r1);
			if(r2.b - r2.a > 0) s[(c+1)%2].insert(r2);
			else if(r2.b - r2.a == 0) l.insert(r2);
			it++; k--;
			if(k == 0) return;
		}
		s[c].clear();
		c++; c%=2;
	}
	R = L = 0;

}

int main(){
	freopen("C-small-2-attempt0.in", "rt", stdin);
	freopen("output", "wt", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> n >> k;
		solve();
		if(R < L){
			int temp = R; R = L; L = temp;
		}
		cout <<"Case #"<<i+1<<": ";
		cout << R << " " << L << endl;
	}

	return 0;
}