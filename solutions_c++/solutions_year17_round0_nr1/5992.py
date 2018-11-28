#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,k;
	char s[1005];
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("fliplarge.txt");
	in>>t;
	for(int i=1;i<=t;i++){
		in>>s;
		in>>k;
		int count=0,flag=1;
		int len = strlen(s);
		for(int j=0;s[j+k-1]!='\0';j++){
			if(s[j]=='-'){
				count++;
				for(int l=j;l<j+k;l++){
					if(s[l]=='+')
						s[l]='-';
					else if(s[l]=='-')
						s[l]='+';
				}
			}
		}
		for(int j=len-1;j>=len-k;j--){
			if(s[j]=='-'){
				flag=0;
				break;
			}
		}
		if(flag==0){
			out<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		}else{
			out<<"Case #"<<i<<": "<<count<<endl;
		}
	}
}