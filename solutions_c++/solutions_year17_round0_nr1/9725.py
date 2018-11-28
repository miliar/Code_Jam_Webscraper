#include <iostream>
#include <string>
#include <queue>
#include <map>
using namespace std;

bool isSolved(string &s){
	for(int i = 0; i<s.length(); i++){
		if(s[i] == '-'){
			return false;
		}
	}
	return true;
}

int solve(string &s, int k){
	queue<string> q;
	map<string, bool> visited;
	map<string, int> step;
	q.push(s);
	step[s] = 0;
	while(q.size() > 0){
		string current = q.front();
		q.pop();
		if(isSolved(current)){
			return step[current];
		}
		if(visited[current]){
			continue;
		}
		visited[current] = true;
		for(int i = 0; i <= current.length() - k; i++){
			string tmp = current;
			for(int j = 0; j<k; j++){
				if(tmp[i+j] == '+'){
					tmp[i+j] = '-';
				}else{
					tmp[i+j] = '+';
				}
			}
			if(step.find(tmp) != step.end()){
				if(step[tmp] > step[current] + 1){
					step[tmp] = step[current] + 1;
				}
			}else{
				step[tmp] = step[current] + 1;
			}
			q.push(tmp);
		}

	}
	return -1;
}

int main(){
	int t;
	string s;
	cin >> t;
	for(int i = 0; i<t; i++){
		int k;
		cin>>s>>k;
		int result = solve(s, k);
		cout<<"Case #"<<(i+1)<<": ";
		if(result >= 0){
			cout<<result<<endl;
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}

	}
}