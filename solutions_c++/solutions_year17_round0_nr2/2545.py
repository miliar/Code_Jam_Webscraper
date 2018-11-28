#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <climits>

#define ll long long

using namespace std;

int main(){
	int t;
	cin>>t;
	int a=0;
	while (t--){
		a++;
		cout<<"Case #"<<a<<": ";
		string num;
		cin>>num;
		int i=0;
		while (i<num.size()-1){
			if (num[i]>num[i+1]){
				break;
			}
			i++;
		}
		if (i==num.size()-1){
			cout<<num<<endl;
		}
		else{
			int j=i;
			while(j>=0 && num[j]==num[i]){
				j--;
			}
			j++;
			num[j]--;
			for (i=j+1;i<num.size();i++){
				num[i]='9';
			}
			if (num[0]=='0'){
				for (i=1;i<num.size();i++){
					num[i-1]=num[i];
				}
				num.pop_back();
			}
			cout<<num<<endl;
		}



	}
	return 0;
}	
