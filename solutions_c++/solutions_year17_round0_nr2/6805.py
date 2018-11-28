#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
int t,len,index;
char s[19];
bool zeroFlag, flag;
int main() {
	cin>>t;
	for (int test = 1; test <= t; test++){
		memset(s,NULL,sizeof(s));
		len = 0;
		index = 1;
		zeroFlag = flag = false;
		cin>>s;
		len = strlen(s);
		for(int i=1;i<len;i++){
			if(s[i-1] > s[i]){
				flag = true;
				index = i;
				s[index-1] -= 1;
				break;
			}
		}
		if(flag == true){
			for(int i=index;i<len;i++)
				s[i] = '9';
		}
		for(int i=index-1;i>=1;i--){
			if(s[i-1] > s[i]){
				s[i] = '9';
				s[i-1] -= 1;
			}
		}
		for(int i=0;i<len;i++){
			if(s[i] == '0'){
				index = i;
				zeroFlag = true; 
			}
		}
		cout<<"Case #"<<test<<": ";
		if(zeroFlag == true){
			for(int i=index+1;i<len;i++)
				cout<<s[i];
			cout<<endl;
		}
		else
			cout<<s<<endl;
   }
   return 0;
}