#include <bits/stdc++.h>
using namespace std;

long long T;
long long N, K;


#define ls first.first
#define rs first.second
#define x second

pair<long long,long long> split(long long x){
	if (x%2==1) return make_pair(x/2, x/2);
	return make_pair((x-1)/2, x/2);
}

int main(){
	cin >> T;
	for (long long q = 1; q<=T; q++){
		cout << "Case #" << q << ": ";

		cin >> N >> K;

		queue<pair<pair<long long, long long>, long long> > pq;

		pq.push(make_pair(split(N), 1));

		while(!pq.empty()){
			pair< pair <long long, long long>, long long> state = pq.front();
			long long cnt = state.x;
			pq.pop();

			while (!pq.empty() && pq.front().first == state.first){
				cnt += pq.front().x;
				pq.pop();
			}

			K -= cnt;

			if (K <= 0){
				cout << state.rs << " " << state.ls << endl;
				break;
			}
			
			if (state.ls == state.rs){
				if (state.ls > 0) pq.push(make_pair(split(state.ls), cnt*2));
			}
			else{
				if (state.rs > 0) pq.push(make_pair(split(state.rs), cnt));
				if (state.ls > 0) pq.push(make_pair(split(state.ls), cnt));
			}
		}
	}
}