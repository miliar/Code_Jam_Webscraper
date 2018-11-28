#include <bits/stdc++.h>

#define i64 long long
#define u64 unsigned long long
#define i32 int
#define u32 unsigned int

#define pii pair<int, int>
#define pll pair<long long, long long>

#define ld long double
#define defmod 1000000007

#define mati64(a,b) vector<vector<i64>>(a, vector<i64>(b, 0));
using namespace std;
class comp
{
public:
    bool operator() (pll a, pll b)
    {
        if(a.first > b.first)
        	return false;
        else if(a.first < b.first)
        	return true;
        else{
        	return a.second > b.second;
        }
    }
};

void printpq(priority_queue<pll, vector<pll>, comp> pq){
	vector<pll> tt;
	cout << "pq: ";
	while(!pq.empty()){
		tt.push_back(pq.top());
		pq.pop();
		cout << tt.back().first << "," << tt.back().second << " "; 
	}
	cout << endl;
	for(auto f: tt){
		pq.push(f);
	}
}
void solve1(i64 n, i64 k){
	priority_queue<pll, vector<pll>, comp> pq;
	pq.push({n, 1});
	pll last;
	for(int i = 0; i < k; ++i){
		//printpq(pq);
		pll y = pq.top();
		pq.pop();
		last = y;
		//cout << y.first << " ";
		//if(y.first%2==1){
		//	cout << y.second+y.first/2 << " ";
		//}
		//else
		//	cout << y.second+y.first/2-1 << " ";
		if(y.first == 1)
			continue;
		if(y.first == 2){
			pq.push({1, y.second+1});
			continue;
		}
		pll a, b;
		if(y.first%2==1){
			a = {y.first/2, y.second};
			b = {y.first/2, y.second+y.first/2+1};
		}
		else{
			a = {y.first/2-1, y.second};
			b = {y.first/2, y.second+y.first/2};
		}
		
		pq.push(a);
		pq.push(b);
	}
	//cout << "vika " << last.first << endl;

	i64 a, b;
	last.first-=1;
	a = last.first/2;
	b = last.first-last.first/2;
	cout << max(a, b) << " " << min(a, b) << endl;
}

void solve2(i64 n, i64 k){
	unordered_map<i64, i64> lol;
	lol[n] = 1;
	i64 kj = k-1;
	i64 kl = k;
	while(kj > 0){
		kl = kj;
		unordered_map<i64, i64> l2;
		for(auto f: lol){
			i64 n2 = f.first-1;
			i64 a = n2/2;
			i64 b = n2-n2/2;
			if(a != 0){
				l2[a]+=f.second;
				kj-=f.second;
			}
			if(b != 0){
				l2[b]+=f.second;
				kj-=f.second;
			}
		}
		lol = l2;
		//cout << "lol nyt ";
		//for(auto f: lol)
		//	cout <<f.first << "," << f.second << " ";
		//cout << endl;
 	}
	vector<pll> fak;
	for(auto f: lol)
		fak.push_back(f);
	sort(fak.begin(), fak.end(), greater<pll>());
	for(int i = 0; i < fak.size(); ++i){
		kl-=fak[i].second;
		if(kl <= 0){
			
			pll last = fak[i];
			i64 a, b;
			last.first-=1;
			a = last.first/2;
			b = last.first-last.first/2;
			cout << max(a, b) << " " << min(a, b) << endl;
			return;
		}
	}
}

int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	int tests; cin >> tests;
	for(int i = 1; i <= tests; ++i){
		cout << "Case #" << i << ": ";
		i64 n, k; cin >> n >> k;
		solve2(n, k);
	}
	return 0;
}
