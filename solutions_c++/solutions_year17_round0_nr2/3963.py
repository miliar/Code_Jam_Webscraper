#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int mylength(int a){
	int res = 0;
	if(a==0)	return 1;
	while(a>0){
		a/=10;
		res++;
	}
	return res;
}

int main(){
	int t; cin >> t;
	for(int i=0;i<t;i++){
		// int num;	cin >> num;
		string s; cin >> s;
		int tmp1=-1,tmp2=-1;
		for(int x=0;x<s.length()-1;x++){
			if(s[x]>s[x+1]){
				tmp1 = x;
				for(int y=x;y>=0;y--){
					if(s[y]>s[y-1]){
						tmp2 = y;
						break;
					}
				}
				break;
			}
		}
		// cout << s << " " << tmp1 << " " << tmp2 << endl;
		if(tmp1!=-1){
			s[tmp2] -= 1;
			for(int x=tmp2+1;x<s.length();x++){
				s[x]='9';
			}
		}
		printf("Case #%d: ",i+1);
		int flag = 0;
		for(int x=0;x<s.length();x++){
			if(s[x]!='0'){
				flag=1;
			}
			if(flag==1){
				printf("%c",s[x]);
			}
		}
		printf("\n");
	}
}