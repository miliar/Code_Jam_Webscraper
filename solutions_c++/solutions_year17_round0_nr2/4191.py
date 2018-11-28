#include <bits/stdc++.h>

using namespace std;

string str,ans;
int ch[20];

void gao(int k){
	if (ans.length()>0) return ;
	for (int i=0;i<k-1;i++)
		if (ch[i]>ch[i+1]) return;
	for (int i=0;i<k;i++){
		int d = str[i] - '0';
		if (d>ch[i]) break;
		if (d<ch[i]) return ; 
	}
	if (k==str.length()){
		for (int i=0;i<k;i++)
			ans+=char(ch[i]+48);
		return ;
	}
	for (int i=9;i>0;i--){
		ch[k] = i;
		gao(k+1);
	}	
}

int main(){
	int T;
	scanf("%d",&T);
	for (int ti=1;ti<=T;ti++){
		cin >> str;
		ans="";
		gao(0);
		if (ans.length()==0){
			for (int i=0;i<str.length()-1;i++)
				ans+='9';
		}
		printf("Case #%d: ", ti);
		puts(ans.c_str());
	}
	return 0;
}
