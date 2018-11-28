#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	string s;
	int k;
	for(int in=0;in<t;in++){
		cin >> s >> k;
		int count = 0;
		for(int i=0;i<=s.size()-k;i++){
			if(s[i] == '-'){
				count++;
				for(int f=0;f<k;f++){
					s[i+f] = (s[i+f] == '+')?'-':'+';
				}
			}
		}
		int flag = 1;
		for(int i=0;i<s.size();i++){
			if(s[i] == '-'){
				flag = 0;
				break;
			}
		}
		if(flag){
			cout << "Case #" << in+1 << ": " << count << endl;
		}
		else{
			cout << "Case #" << in+1 << ": IMPOSSIBLE" << endl;
		}
	}
}
