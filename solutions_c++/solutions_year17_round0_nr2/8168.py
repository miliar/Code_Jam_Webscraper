#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
using namespace std;

int main(){		
	int casenum = 0;
	cin>>casenum;
	long long int tidy = 0, ori = 0, toadd= 0;
	int topush = 0, countbit = 0, maxbit = 0;
	string num = "";
	string trans = "";
	for(int i = 0; i < casenum; ++i){
		cin>>tidy;
		ori = tidy;
		num = "";
		countbit = 0;
		maxbit = 0;
		while(tidy>0){
			topush = tidy%10;
			tidy/=10;
			++countbit;
			if(num.size()>0 && (num[num.size()-1]-'0')<topush){
				topush-=1;
				maxbit = countbit-1;
			}
			num+=(char)(topush+'0');
		}	
		if(maxbit==0){
			cout<<"Case #"<<i+1<<": "<<ori<<endl;
			continue;
		}
		//maxbit-=1;
		num=num.substr(maxbit, num.size()-maxbit);
		reverse(num.begin(), num.end());
		while(num[num.size()-1]=='0')num = num.substr(0,num.size()-1);
		for(int j = 0; j < maxbit; ++j){
			num+="9";
		}
		
		cout<<"Case #"<<i+1<<": "<<num<<endl;	
	}
	return 0;
}
