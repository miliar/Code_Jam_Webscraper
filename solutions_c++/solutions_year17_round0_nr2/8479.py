#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int n,m;

vector<int>tmp;

int check(int x){
	tmp.clear();
	while(x){
		tmp.push_back(x % 10);
		x /= 10;
	}
	for (int i = 1;i < tmp.size();i++){
		if (tmp[i] > tmp[i - 1])  return 0;
	}
	return 1;
}


int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	cin >> T;
	typedef long long ll;
	ll n; int nc = 0;
	while(cin >> n){
        while(!check(n)) n--;
        cout << "Case #" << ++nc << ": ";
        cout << n << endl;
	}
}
