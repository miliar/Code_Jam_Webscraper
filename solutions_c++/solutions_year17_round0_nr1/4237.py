#include<bits/stdc++.h>
using namespace std;
int calculate_answer(string s, int k){
	int cnt = 0;
	int l = s.length();
	for(int i=0; i<l; i++){
		if(s[i]=='-'){
			for(int j=i; j<k+i;j++){
				if(j==l)
					return -1;
				else
				s[j] = (s[j]=='+')?'-':'+';
			}
			cnt++;
		}
	}
	return cnt;
}
int main(){
	ofstream out("output.out");
	ifstream in("input.in");
	int t, k;
	string s;
	in>>t;
	for(int i=1; i<=t;i++){
		in>>s>>k;
		int ans = calculate_answer(s, k);
		if(ans==-1){
			out<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			out<<"Case #"<<i<<": "<<ans<<endl;
		}
	}
	return 0;
}