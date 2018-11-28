#include <iostream>
#include <string>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;



int main(){
	int t,i;
	cin >> t;
	string s;
	for(int c = 1;c <= t;c++){
		cout << "Case #" << c << ": ";
		cin >> s;
		for(int i=0;i<s.length();i++){
			if(i == s.length()-1){
				continue;
			}
			if(s[i+1] < s[i]){
				int st;
				for(st=i;st>=0;st--){
					if(s[st] < s[i])
						break;
				}
				s[st+1] = s[i]-1;
				st+=2;
				for(int j=st;j<s.length();j++)
					s[j] = '9';
				break;
			}
		}

		long long ans = 0,p=1;
		for(int i=s.length()-1;i>=0;i--){
			ans += int(s[i]-'0')*p;
			p *= 10;
		}
		cout << ans << endl;
	}
	return 0;
}