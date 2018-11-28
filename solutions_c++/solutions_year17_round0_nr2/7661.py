#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(vector<int>& nmbr, int index){
	if(index == 0){
		nmbr[0] -= 1;
		for(int i=1; i != nmbr.size(); i++) nmbr[i] = 9;
		return;
	}
	nmbr[index] -= 1;
	if(nmbr[index-1] <= nmbr[index]) {
		for(int i=index+1; i != nmbr.size(); i++) nmbr[i] = 9;
		return;
	}
	else solve(nmbr, index-1);
	return;
}

void getItDone(vector<int>& arr){
	int len = arr.size();
	for(int i=0; i < len-1; i++){
		if(arr[i] > arr[i+1]) solve(arr, i);
	}
	return ;
}


int main(void){
	ofstream fout("output.txt");
	ifstream fin("input.txt");
	int t;
	fin>> t;
	for(int i=1; i <= t; i++){
		ll inp;
		fin>> inp;
		ll tmpi = inp;
		int pw = 0;
		while(tmpi) {
			tmpi /= 10;
			pw++;
		}
		// re-assignment
		tmpi = inp;
		vector<int> toproc(pw);
		for(int j = pw-1; j != -1; j--){
			toproc[j] = tmpi % 10;
			tmpi /= 10;
		}

		getItDone(toproc);
		ll ans = 0;
		for(int h=0; h != toproc.size(); h++){
			ans *= 10LL;
			ans += toproc[h];
		}
		fout<<"Case #" << i << ": " << ans << "\n";
	}
	return 0;
}