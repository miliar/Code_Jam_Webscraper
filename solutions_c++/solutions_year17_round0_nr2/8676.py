#include <iostream>
using namespace std;

int main(){
	string num;
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>num;
		int len=num.length();
		for(int j=0;j<len-1;j++){
			if(num[j]>num[j+1]){
				num[j]--;
				while(num[j]+1==num[j-1] && j>0){
					num[j]='9';
					num[j-1]--;
					j--;
				}
				for(int k=j+1;k<len;k++)
					num[k]='9';
				break;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		for(int j=0;j<len;j++){
			if(num[j]=='0')
				continue;
			cout<<num[j];
		}
		cout<<endl;
	}
	return 0;
}