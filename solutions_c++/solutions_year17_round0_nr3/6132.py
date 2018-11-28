#include <iostream>
#include <set>
#include <map>
#include <fstream>
using namespace std;

pair<int,int> maxMin(int a){
	return make_pair(a/2, (a-1)/2);
}

pair<int,int> popSet(set<pair<int,int>> &X, map<int,int> &numberUsed){
	pair<int,int> res;
	set<pair<int,int>>::iterator it = X.end();
	it--;
	res = maxMin(it -> first);
	X.erase(it);
	X.insert(make_pair(res.first, numberUsed[res.first]++));
	X.insert(make_pair(res.second, numberUsed[res.second]++));
	return res;
}

void printSet(set<pair<int,int>> S){
	cout << "set ";
	for(set<pair<int,int>>::iterator it = S.begin(); it != S.end(); it++){
		cout << it -> first << " ";
	}
	cout << endl;
}

int main(){
	ifstream testcase("test.in");
	ofstream output("out");
	int T, N, K;
	map<int,int> numberUsed;
	//cin >> T;
	testcase >> T;
	set<pair<int,int>> stall;
	pair<int,int> res;
	for(int i = 1; i <= T; i++){
		//cin >> N >> K;
		testcase >> N >> K;
		stall.insert(make_pair(N,0));
		for(int j = 0; j < K; j++){
			res = popSet(stall, numberUsed);
			//printSet(stall);
		}
		//cout << "Case #" << i << ": " << res.first << " " << res.second << endl;
		output << "Case #" << i << ": " << res.first << " " << res.second << endl;
		stall.clear();
		numberUsed.clear();
	}
}
