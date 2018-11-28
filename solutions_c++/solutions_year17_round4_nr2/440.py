#include<bits/stdc++.h>
using namespace std;

long long peoplecount[1005];
long long poscount[1005];

void solve(){
	long long N, C, M;
	cin >> N >> C >> M;

	for(int i = 0; i < 1005; i++){
		peoplecount[i] = 0;
		poscount[i] = 0;
	}

	for(long long i = 0; i < M; i++){
		long long p, b;
		cin >> p >> b;
		b--; p--;
		peoplecount[b]++;
		poscount[p]++;
	}

	long long width = 0;
	for(int i = 0; i < 1005; i++){
		width = max(width, peoplecount[i]);
	}
	long long sumi = 0;
	for(int i = 0; i < 1005; i++){
		sumi += poscount[i];
		long long need;
		if(sumi % (i+1) == 0){
			need = sumi/(i+1);
		}else{
			need = sumi/(i+1) + 1;
		}
		width = max(width, need);
	}


	long long pre = 0;
	for(int i = 0; i < 1005; i++){
		if(poscount[i] <= width){
			continue;
		}else{
			pre += poscount[i] - width;
		}
	}
	cout << width << " " << pre << endl;

	return;
}

int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}

