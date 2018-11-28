#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,l=1;
	cin >> t;
	while(l<=t){
		char a[1001];
		
		cin >> a;
		int i=0,n;
		cin >> n;
		int len = strlen(a);
		int cnt=0;
		for(i = 0;a[i]!=0;i++){
			if(a[i]=='-'){
				int s,e;
				cnt+=1;
				if((i+n)>len){
					s  = len-n-1;
					if(s<0)
						s = 0;
					e = len-1;
				}
				else
				{
					s = i;
					e = i+n;
				}
				for(;s!=e;s++){
					if(a[s]=='+')	
						a[s]= '-';
					else if(a[s]=='-')
						a[s] = '+';
				}
			}
		}
		int f = 1;
		for(i=0;a[i]!=0;i++){
			if(a[i]=='-'){
				f = 0;
				break;
			}
		}
		if(f == 0){
			cout << "Case #"<<l<<": "<<"IMPOSSIBLE"<<endl;
		}
		else 
			cout << "Case #"<<l<<": "<<cnt<<endl;
		l+=1;
	}
}
