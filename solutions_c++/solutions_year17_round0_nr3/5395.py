#include <bits/stdc++.h>
using namespace std;
pair<int,int> f(int s,const vector<int>& stalls){
	int r = 0,l = 0;
	for(int i=s+1;i<stalls.size();i++){
		if( stalls[i] ) break;
		r++;
	}
	for(int i=s-1;i>=0;i--){
		if( stalls[i] ) break;
		l++;
	}
	return make_pair(min(l,r),max(l,r));
}
tuple<int,int,int> in(const vector<int>& stalls){
	int N = stalls.size() - 2;
	vector<tuple<int,int,int>> ts;
	for(int i=1;i<=N;i++){
		// empty
		if(stalls[i] == 0){
			int mi,ma;
			tie(mi,ma) = f(i,stalls);
			ts.emplace_back(-mi,-ma,i);
		}
	}
	sort(ts.begin(),ts.end());
	cerr << "MaxLR:" << -get<1>(ts[0]) << " MinLR:" << -get<0>(ts[0]) << " => ";
	// return get<2>(ts[0]);
	return ts[0];
}
void solve(){
	long long N,K;
	cin >> N >> K;
	vector<int> stalls(N+2);
	stalls[0] = stalls[N+1] = 1;

	for(int i=0;i<K;i++){
		cerr << i << " person" << endl;
		int mi,ma,S;
		tie(mi,ma,S)  = in(stalls);
		mi = -mi;ma = -ma;

		cerr << "Enter Stall " << S << endl;
		stalls[S] = 1;
		if(i == K-1)cout << ma << " " << mi;
	}
}
int main(void){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		cout << "Case #" << i+1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}