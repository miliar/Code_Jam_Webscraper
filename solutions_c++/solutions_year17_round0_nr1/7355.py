#include <bits/stdc++.h>

using namespace std;

int main(void){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for(int t=1;t<=test;t++){
		string s;
		int k;
		cin>>s>>k;
		int tot = 0;
		for(int i=0;i<s.size();i++){
			if(s[i]=='+')continue;
			if(i+k>s.size()){
				tot=-1;
				break;
			}
			tot++;
			for(int j=i;j<i+k;j++){
				s[j] = s[j]=='+'? '-':'+';
			}
		}
		if(tot!=-1)
		cout<<"Case #"<<t<<": "<<tot<<endl;
		else cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
