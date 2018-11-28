#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = int(3e5), mod = int(1e9)  + 7;
int T;
string s;

bool good(string s){
	for(int i = 1; i < s.size(); i++){
		if(s[i] < s[i - 1]) return 0;
	}
	return 1;
}

bool bad(string s){
	for(int i = 0; i < int(s.size()) - 1; i++){
		if(s[i] < s[i + 1]) return 0;
	}
	return 1;
}


string get(string s){
	string res = "";
	bool ok = 0;
	for(int i = 0; i < s.size(); i++){
		if(s[i] != '0') ok = 1;
		if(ok) res += s[i];
	}
	return res;
}

void solve(){
	cin >> s;
	if(good(s)){
		cout << s << endl;
		return;
	}
	if(bad(s)){
		if(s[0] == '1'){
			for(int i = 1; i < s.size(); i++){
				cout << '9';
			}
			cout << endl;
		}
		else{
			cout << s[0] - 1 - '0';
			for(int i = 1; i < s.size(); i++){
				cout << '9';	
			}
			cout << endl;
		}
		return;
	}
	for(int i = 1; i < s.size(); i++){
		if(s[i] < s[i - 1]){
			s[i - 1] -= 1;
			for(int j = i; j < s.size(); j++){
				s[j] = '9';
			}
			break;
		}
	}
	s = get(s);
	cout << s << endl;
}

int main () {           
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}

return 0;
}