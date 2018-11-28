#include <iostream>
using namespace std;

string helper(string state, int k){
	string result;
	int step = 0;
	int len = state.size();
	int l = 0, r = len-1;
	while(l<r){
		while(l<r&&state[l]=='+') l++;
		while(l<r&&state[r]=='+') r--;
		if(l==r&&state[l]=='+') break;
		if(r-l+1<k){
			step = -1;
			break;
		}
		for(int t = 0; t<k; t++){
			if(state[l+t]=='-') state[l+t] = '+';
			else state[l+t] = '-';
		}
		step++;
	}
	if(step==-1) return "IMPOSSIBLE";
	return to_string(step);
}

int main(){
	int n;
	cin>>n;
	string s;
	int k;
	for(int i = 0; i<n; i++){
		cin>>s>>k;
		cout<<"Case #"<<i+1<<": "<<helper(s, k)<<endl;
	}
	return 0;
}
