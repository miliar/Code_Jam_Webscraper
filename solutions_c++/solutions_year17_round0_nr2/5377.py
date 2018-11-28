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
	int t,tc;
	cin >> t;
	tc = t;
	string str;
	int i,j;
	while(tc--){
		cout << "Case #" << t-tc << ": ";
		cin >> str;
		for(i=str.length()-1;i>0;--i){
			if(str[i] < str[i-1]){
				for(j=i;j<str.length();++j)str[j] = '9';
				str[i] = '9';
				str[i-1] -= 1;
				if(str[i-1] < '0'){
					str[i-1] = '0';
					for(j=i-1;j>=0 && str[j] == '0';--j)str[j] = '9';
					str[j] -= 1;
				}
			}
		}
		cout << stoll(str) << endl;
	}
	return 0;
}

