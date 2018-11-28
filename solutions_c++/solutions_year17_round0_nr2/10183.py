/*
 * codejam.cpp
 *
 *  Created on: 09-Apr-2017
 *      Author: naivehobo
 */
#include <iostream>
#include <vector>

using namespace std;

vector<int> getDigit(long long int n){
	vector<int> dig;
	while(n>0){
		dig.push_back(n%10);
		n /= 10;
	}
	return dig;
}

void getTidyNum(vector<int> num, long long int n){
	int pos=-1;
	if(num.size()==1){
		cout<<n;
		return;
	}
	for(int i=num.size()-1;i>0;i--){
		if(num[i]>num[i-1]){
			pos = i;
			break;
		}
	}
	if(num.size()==2){
		if(pos==-1)
			cout<<n;
		else{
			if(num[1]==1)
				cout<<'9';
			else
				cout<<num[1]-1<<'9';
		}
		return;
	}
	if(pos!=-1){
		if(num[pos]==1){
			for(int j=0;j<num.size()-1;j++)
				cout<<'9';
		}
		else{
			while(true){
				if(num[pos]-1<num[pos+1]){
					pos++;
				}
				else{
					num[pos]--;
					for(int i=num.size()-1;i>=pos;i--)
						cout<<num[i];
					for(int i=pos-1;i>=0;i--)
						cout<<'9';
					break;
				}
				if(pos==num.size()-1){
					cout<<num[num.size()-1]-1;
					for(int i=0;i<num.size()-1;i++)
						cout<<'9';
					break;
				}
			}
		}
	}
	else
		cout<<n;
}

int main(){
	int t;
	cin>>t;
	vector<int> num;
	long long int n;
	for(int I=1;I<=t+1;I++){
		cin>>n;
		num = getDigit(n);
		cout<<"Case #"<<I<<": ";
		getTidyNum(num,n);
		cout<<endl;
		num.clear();
	}
	return 0;
}
