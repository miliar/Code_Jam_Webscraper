#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int i,j,k;

#define fi(a,b) for(i=a;i<b;i++)
#define fj(a,b) for(j=a;j<b;j++)
#define fk(a,b) for(k=a;k<b;k++)
#define fr(a,b,c) for(i=a;i<b;i+=c);
#define rf(a,b,c) for(i=a;i>b;i-=c);
#define pb(a) push_back(a);

string solve(string s, int start, int end, int k, int count){
	
	if (start==end){
		if (s[end] == '+'){
			cout << count;
			return "";
		} else {
			return "IMPOSSIBLE";
		}
	}
	
	/*
	for(i=start;i<end+1;i++){
		cout << s[i];
	}
	
	cout << endl;
	*/
	
	if (s[start]=='+') {
		//cout << s[i];
		//cout << "case 1" << endl;
		return solve(s,start+1,end,k,count);
	}

	if (s[end]=='+') {
		//cout << "case 2" << endl;
		return solve(s,start,end-1,k,count);
	}
	
	if(k>end-start+1) return "IMPOSSIBLE";
	
	//cout << "case 3" << endl;
	
	for(i=start;i<start+k;i++){
		if (s[i] == '+'){
			s[i] = '-';
		} else {
			s[i] = '+';
		}
	}
	
	return solve(s,start,end,k,count+1);
}

int main(){
	int t,k;
	
	cin >> t;
	
	fj(0,t){
		string s;
		cin >> s;
		int s_length = s.length();
		cin >> k;
		cout << "Case #" << j+1 << ": ";
		cout << solve(s,0,s_length-1,k,0) << endl;
	}
	
	return 0;
}