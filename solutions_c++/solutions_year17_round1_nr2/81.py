#include "bits/stdc++.h"
using namespace std;
const int maxn = 55;
typedef long long ll;
ll arr[maxn][maxn], r, c;
ll values[maxn], pointer[maxn];
bool over(){
	for(int e = 0; e < r; e++)
		if(pointer[r] == c)
			return true;
	return false;
}
int ok(ll x){
	for(int e = 0; e < r; e++){
		while(pointer[e] < c && arr[e][pointer[e]] < (values[e]*x*9.0)/10) pointer[e]++;
		if(pointer[e] == c) return 0;
		if(arr[e][pointer[e]] > (values[e]*x*11.0)/10) return 0;
	}
	return 1;
}
void advance(){
	for(int e = 0; e < r; e++)
		pointer[e]++;
}
int answer(){
	memset(pointer, 0, sizeof(pointer));
	int ans = 0;
	for(int e = 1; e <= 1000100; e++){
		if(over()) break;
		while(ok(e)){ ans ++; advance(); }
	}
	return ans;
}
int main(){
	int cases; cin >> cases;
	for(int cs = 1; cs <= cases; cs++){
		cout << "Case #" << cs << ": ";
		cin >> r >> c;
		for(int e = 0; e < r; e++)
			cin >> values[e];
		for(int e = 0; e < r; e++){
			for(int f = 0; f < c; f++)
				cin >> arr[e][f];
			sort(arr[e], arr[e] + c);
		}
		cout << answer() << endl;
		//cerr << cs << endl;
	}
	return 0;
}
