#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long long ll;
#define INF 2000000000
#define MOD 1000000007
#define endl '\n'

int main(){
	ios::sync_with_stdio(false);
	int t,tc,i,j,k;
	bool flag;
	int counter;
	string str;
	cin >> t;
	tc = t;
	while(tc--){
		cout << "Case #" << t-tc << ": ";
		cin >> str >> k;
		counter = 0;
		for(i=0;i<=str.size()-k;++i){
			if(str[i] == '-'){
				++counter;
				for(j=0;j<k;++j){
					str[i+j] = str[i+j]=='-'?'+':'-';
				}
			}
		}
		flag = true;
		for(i=str.size()-k;i<str.size();++i){
			if(str[i] == '-'){
				flag = false;
				break;
			}
		}
		if(!flag){
			cout << "IMPOSSIBLE";
		}else{
			cout << counter;
		}
		cout << endl;
	}
	return 0;
}

