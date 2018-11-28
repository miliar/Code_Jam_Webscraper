#include <iostream>

using namespace std;

#define Aman Jain

int main(){
	int testcase, length, j, k, l;
	long long ans;
	string number;
	cin >> testcase;

	for(int i=1;i<=testcase;i++){
		cin >> number;
		length = number.length();
		
		for(j=length-1;j>0;j--)
			if(number[j]<number[j-1]){
				for(k=j;k<length;k++)
					number[k]='9';
				
				l=j-1;
				number[l]-=1;
				while(l>0 && number[l]=='0'){
					number[l]='9';
					number[--l]-=1;
				}
			}

		cout << "Case #" << i << ": ";

		ans = 0;
		for(j=0;j<length;j++){
			ans*=10;
			ans+=number[j]-'0';
		}

		cout << ans << endl;
	}
	
	return 0;
}