#include<bits/stdc++.h>
using namespace std;
string remove_zero(string num){
	string ans;
	for(int i=0;i<num.size();i++){
		if(num[i]!='0')
			ans = ans + num[i];
	}
	return ans;
}	
int main(){
	string num;
	int size;
	cin>>size;
	for(int k=0;k<size;k++){
		cin>> num;
		for(int i=1;i<num.size();i++){
			if(num[i-1]>num[i]){
				for(int j=i;j>=0;j--){
					if(num[j-1]>num[j]){
						num[j-1]=num[j-1]-1;
						num[j]='9';
					}
				}
				for(int j=i;j<num.size();j++)
				num[j]='9';
				
				break;				
			}
		}
	cout<<"Case #"<<(k+1)<<": "<<remove_zero(num)<<"\n";
	}
	
	return 0;
}

