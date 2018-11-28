#include<bits/stdc++.h>
using namespace std;
string s ;
void revers(int end , int k ){
for(int i = end-k ;  i<=end ; i++){
	if(s[i]=='+')
		{s[i] = '-';
}
	else
		s[i]= '+';

}	
}
int main(){
	
	int t;
	int m=1 , k ;
	cin>>t ;
	t++;
	while(m!=t){
		int count=0, flag = 0;
		cin>>s;
		cin>>k;
		int ss = s.size();
		for(int i = ss-1; i>=(k-1);i--){
			if(s[i]=='-')
			{	//s[i]='+';
				count++;
				revers(i, k-1);
			}

		}
		for(int i = 0 ; i <ss-1 ;i++){
			if(s[i]=='-'){
				flag=1;
			}
		}
		if(flag==1){
				cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
			

		}
		else
		cout<<"Case #"<<m<<": "<<count<<endl;
		m++;
	}

	return 0;
}