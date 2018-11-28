#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
vector<int> numList;
int n;
void banao(){
	for(int i=0;i<n-1;i++){
		if(numList[i+1]<numList[i]){
			long long int num=0;
			for(int k=0;k<=i;k++){
				num=10*num+numList[k];	
			}
			num--;
			for(int k=i;k>=0;k--){
				numList[k]=num%10;
				num=num/10;	
			}
						
			for(int k=i+1;k<n;k++){
				numList[k]=9;
			}
			if(i>0){
				if(numList[i]<numList[i-1])
				banao();
			}
			
		}
	}
	
}

int main() {
	int test;
	cin>>test;
	string s;
	int total=test;
	while(test--){
		cin>>s;
		n =s.length();
		for(int i=0;i<n;i++){
			numList.push_back((int) s[i]-48);
		}
		cout <<"Case #"<<total-test<<": "; 
		banao();
		bool for0=true;
		for(int i=0;i<n;i++){
			if(for0){
				if(numList[i]!=0)
				for0=false;
				else
				continue;
			}
			cout<<numList[i];
		}
		cout<<endl;
		numList.clear();
		
	}
	return 0;
}


