#include <iostream>
#include <set>
#include <string>
#include <queue>

using namespace std;

string str;
int n, k;

bool check(string s){
	for(int i = 0; i < n; i++){
		if( s[i] == '-') return false;
	}
	return true;
}

void solve(){
	queue<string> q;
	queue<int> c;

	q.push(str);
	c.push(0);
	
	set<string> s;
	s.insert(str);

	int ans = -1;

	while(!q.empty()){
		string now = q.front();
		int cnow = c.front();
		if( check(now) ){
			ans = cnow;
			break;
		}
		for(int i = 0; i < k; i++){
			if(now[i] == '+'){
				now[i] = '-';
			}
			else now[i] = '+';
		}
		set<string>::iterator it = s.find(now);
		if( it == s.end() ){
			q.push(now); c.push(cnow+1); s.insert(now);
		}

		for(int i = 0; i < n-k; i++){
			if(now[i] == '+'){
				now[i] = '-';
			}
			else now[i] = '+';
			if(now[i+k] == '+'){
				now[i+k] = '-';
			}
			else now[i+k] = '+';
			it = s.find(now);
			if( it == s.end() ){
				q.push(now); c.push(cnow+1); s.insert(now);
			}
		}

		q.pop(); c.pop();
	}

	if( ans == -1 ){
		cout << "IMPOSSIBLE" << endl;
	}
	else{
		cout << ans << endl;
	}
	
}

int size;
int main(){
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("output", "wt", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> str >> k;
		n = (int) str.size();
		cout << "Case #" << i+1 << ": ";

		solve();	
	}

	return 0;
}