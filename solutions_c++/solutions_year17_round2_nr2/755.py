										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int n, cnt[6];
string str = "ROYGBV";

string getSimple(){
	int arr[3] = {cnt[0], cnt[2], cnt[4]};
	sort(arr, arr + 3);

	int mx = arr[2];
	int sum = cnt[0] + cnt[2] + cnt[4];
	if(mx > sum - mx)
		return "IMPOSSIBLE";

	string res = "";
	for(int i = 0; i < arr[0]; i++)
		res += "RYB";
	
	for(int i = arr[0]; i < arr[1]; i++)
		for(int j = 0; j < 6; j += 2)
			if(cnt[j] >= arr[1])
				res += str[j];
	
	for(int i = 0; i < 6; i += 2){
		for(int j = arr[1]; j < cnt[i]; j++){
			for(int k = 0; k < res.length(); k++){
				if(res[k] != str[i] && res[(k + 1) % res.length()] != str[i]){
					res = res.substr(0, k + 1) + str[i] + res.substr(k + 1);
					break;
				}
			}
		}
	}
	return res;
}

string getComplex(){
	for(int i = 1; i < 6; i += 2){
		int j = (i + 3) % 6;
		if(cnt[i] == 0) continue;
		if(cnt[i] > cnt[j])
			return "IMPOSSIBLE";
		if(cnt[i] == cnt[j]){
			if(n > cnt[i] + cnt[j])
				return "IMPOSSIBLE";
			string res = "";
			for(int k = 0; k < cnt[i]; k++){
				res += str[i];
				res += str[j];
			}
			return res;
		}
	}

	for(int i = 1; i < 6; i += 2){
		int j = (i + 3) % 6;
		cnt[j] -= cnt[i];
	}

	string res = getSimple();
	if(res == "IMPOSSIBLE")
		return res;

	for(int i = 1; i < 6; i += 2){
		int j = (i + 3) % 6;
		for(int it = 0; it < cnt[i]; it++){
			for(int k = 0; k < res.length(); k++){
				if(res[k] == str[j]){
					string tmp = res.substr(0, k) + str[j];
					tmp += str[i] + res.substr(k);
					res = tmp;
					break;
				}
			}
		}
	}
	return res;
}

int main(){
	std::ios::sync_with_stdio(false);
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n;
		for(int i = 0; i < 6; i++)
			cin >> cnt[i];
		string res = getComplex();
		cout << "Case #" << ++test << ": " << res << endl;
	}
	return 0;
}
