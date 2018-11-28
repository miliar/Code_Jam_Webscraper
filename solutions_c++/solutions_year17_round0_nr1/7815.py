#include <iostream>
#include <string>
using namespace std;

bool flip(string &s, int i, int k){
	if(k > s.length()-i)
		return false;
	for(int j=i;j<i+k;j++)
		(s[j] == '+')? s[j] = '-' : s[j]='+';
	return true;
}

int main(){
	int t,k;
	string s;
	cin >> t;
	for(int c=1;c<=t;c++){
		cin >> s >> k;
		cout << "Case #" << c << ": ";
		int ops = 0;
		bool flag = true;
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				if(flag = flip(s,i,k))
					ops++;
				else
					break;
			}
		}
		if(flag){
			for(int i=0;i<s.length();i++){
				if(s[i]=='-')
					flag = false;
			}
		}
		if(flag)
			cout << ops << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}