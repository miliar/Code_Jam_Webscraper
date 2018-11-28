#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<vector>
#include<string>



#define LL long long
using namespace std;

int main(){
int T;
string s;
cin>>T;
for(int k = 1; k<=T;k++){
	cin>>s;
	int len = s.size();
	for(int i =0;i < len-1; i ++){
		if(s[i]>s[i+1]){
			--s[i];
			for(int j = i+1;j<len;j++)
				s[j] ='9';
				break;
		}
	}
	for(int i =len-1;i >0; i --){
		if(s[i]<s[i-1]){
			--s[i-1];
			s[i] = '9';
		}
	}
	 LL a=0;
	for(int i = 0;i<len;i++){
		a*=10;
		a += s[i]-'0';
		
	}
	cout<<"Case #"<<k<<": "<<a<<endl;
} 

return 0;
}


