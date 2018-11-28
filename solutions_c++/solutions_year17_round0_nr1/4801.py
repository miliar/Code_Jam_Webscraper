#include<iostream>
using namespace std;
int main(){
	int sum,t,k,num=0,flag,counter;
	string s;
	cin>>t;
	while(t--){
		sum=flag=0;
		num++;
		cin>>s>>k;
		for(int i=0;i<=s.length()-k;i++){
			if(s[i]=='-'){
				flag=0;
				for(int j=i;j<i+k;j++){
					if(s[j]=='-') s[j]='+';
					else if(flag!=1){
						s[j]='-';
						flag=1;
						counter=j;
					}
					else s[j]='-';
				}
				sum++;
				if(flag==1)
				i=counter-1;
				else i=i+k-2;
			}
		}
		flag=0;
		for(int i=s.length()-1;i>s.length()-k;i--){
			if(s[i]=='-') { flag=1; break; }
		}
		cout<<"Case #"<<num<<": ";
		if(flag==1) cout<<"IMPOSSIBLE";
		else cout<<sum;
		cout<<"\n";
	}
}
