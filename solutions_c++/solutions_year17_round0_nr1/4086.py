#include <bits/stdc++.h>

using namespace std;
int main(){
	int t,i,j,y,k;
	cin>>t;
	int count;
	int impossible;

	string S;
	for(i=0;i<t;i++){
		cin>>S;
		cin>>k;
		count = 0;
		impossible = 0;
		for(j=0;j<S.length();j++){
			if(S[j]=='-'){
				for(y=j;y<j+k;y++){
					if(y>S.length()-1){
						impossible = 1;
						break;
					}
					S[y]=(S[y]=='-')? '+' : '-';
				}
				if(impossible)
					break;
				count++;
			}
		}
		if(impossible)
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		else			
			cout<<"Case #"<<i+1<<": "<< count<<endl;

	}
}