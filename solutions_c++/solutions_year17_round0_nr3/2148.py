#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

long long N, K;

int Getlog2(long long X){
	int res = 0;
	while(X > 1){
		X /= 2;
		++res;
	}
	return res;
}

void solve(){
	int mi = Getlog2(K);
	long long LevelMax = N;	

	for(int i = 0; i < mi; ++i){
		LevelMax /= 2;
	}
	long long LevelNum = 1;
	for(int i = 0; i < mi; ++i){
		LevelNum = LevelNum * 2;
	}	
	long long left = N - LevelNum + 1;
	//cout << "left: " << left << endl;
	long long LevelMaxNum = (left - LevelNum * (LevelMax - 1));
	//cout << "LevelMaxNum: " << LevelMaxNum << endl;
	K = K - LevelNum + 1;
	long long ChooseLen;
	if(K <= LevelMaxNum) ChooseLen = LevelMax;
	else ChooseLen = LevelMax - 1;
	cout << ChooseLen / 2 << " "  << (ChooseLen - 1) / 2 << endl;  
}

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		cin >> N >> K;
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
