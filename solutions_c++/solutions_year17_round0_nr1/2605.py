#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	int t;
	string s;
	int k,count,flag;
	cin >> t;
	for(int i=1;i<=t; ++i){
		cin >> s >> k;
		count = 0;
		for(int j=0;j<s.size();j++){
			if(s[j]=='-'){
				if(j+k-1<s.size()){
					count +=1;
					for(int h=0;h<k;h++){
						if(s[j+h]=='-')s[j+h]='+';
						else s[j+h]='-';
					}
				}
			}
		}
		flag=0;
		for(int j=0;j<s.size();j++){
			if(s[j]=='-')flag=1;
		}
		if(flag==1){
			cout << "Case #" << i << ": IMPOSSIBLE" <<endl;
		}else{
			cout << "Case #" << i << ": " << count <<endl;
		}
	}
	return 0;
}