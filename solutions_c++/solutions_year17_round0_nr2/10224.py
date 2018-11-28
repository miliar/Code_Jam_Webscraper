#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>

using namespace std;

bool isTidy(string str){
	for(int i=0;i<(int)str.length()-1;i++){
		if(str[i]-'0'>str[i+1]-'0')
			return false;
	}
	return true;
}

int tidyNumber(int n){
	int i = n;
	while(true){
		if(isTidy(to_string(i)))
			break;
		i--;
	}
	return i;
}

int main(){
	int T,number;cin>>T;
	for(int i=1;i<=T;i++){
		cin>>number;
		cout<<"Case #"<<i<<": "<<tidyNumber(number)<<"\n";
	}
}

