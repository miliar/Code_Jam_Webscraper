#include <iostream>
#include <string>
using namespace std;

bool all_same(string str, char c){
	if (str.length() == 0) return true;
	else if (str[0]==c)
		return all_same(str.substr(1), c);
	else return false;
	return -2;
}

string invert(string str,long k){
	string s1 = str.substr(k);
	string s2 = str.substr(0,k);
	for(long i=0;i<k;i++){
		if (s2[i] == '+') s2[i] = '-';
		else s2[i] = '+';
	}
	return s2.append(s1);
}

long turnup(string str, long k, long ans){
	if (str.length() == k ) {
		if (all_same(str.substr(1), str[0])){
				if (str[0] == '+') return ans;
				else return ++ans;
			}
		else return -1;
	}

	else if (str[0] == '+')
		return turnup(str.substr(1), k, ans);
	else {
		string s0 = invert(str,k);
		return turnup(s0.substr(1), k, ans+1);
	}
	return 0;
} 


int main(){
	long n;
	cin>>n;
	string s;
	long k;
	for(long i=0;i<n;i++){
		cin>>s;
		cin>>k;
		long a = turnup(s, k ,0);
		if (a == -1) cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<i+1<<": "<<a<<endl;
	}
}
