#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
int R[100];
int Q[100][100];
pair<int,int> Q2[100][100];
multiset<pair<int,int>> nexts[100];
pair<int,int> match(pair<int,int> p1, pair<int,int>p2){
	return {max(p1.first, p2.first), min(p1.second,p2.second)};
}
void main2(){
	int N,P;
	cin >> N >> P;
	for(int i=0;i<N;i++){
		cin >> R[i];
	}
	// cout << endl;
	for(int i=0;i<N;i++){
		for(int j=0;j<P;j++){
			cin >> Q[i][j];
			double qt=R[i];
			double mn = ceil(Q[i][j]/(qt*1.1));
			double mx = floor(Q[i][j]/(qt*0.9));
			Q2[i][j] = {mn,mx};

			// cout << mn << " " << mx << " | ";
			if(mn<=mx){
				nexts[i].insert({mn,mx});
			}
		}
		// cout << endl;
	}
	// cout << endl;
	int tot=0;
	while(true){
		int bad=0;
		pair<int,int> rng = {-100000100, 100000100};
		for(int i=0;i<N;i++){
			if(nexts[i].size()==0){
				bad=-1;
				break;
			}
			auto pr= *nexts[i].begin();
			rng=match(pr,rng);
			if(pr.second < nexts[bad].begin()->second){
				bad=i;
			}
		}
		if(bad==-1){
			break;
		}
		if(rng.first <= rng.second){
			tot++;
			for(int i=0;i<N;i++){
				nexts[i].erase(nexts[i].begin());
			}
		} else {
			nexts[bad].erase(nexts[bad].begin());
		}
	}
	cout << tot;
}

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		main2();
		cout << endl;
	}
	return 0;
}