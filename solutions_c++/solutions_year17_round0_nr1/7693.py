#include<iostream>
#include<cstring>
using namespace std;
int main(){
	int test,count=0,k,flag1=0,r=0,flag,flag2=0,i,t=0,mm=0,s1[100000],temp;
	string ch;
	char s[100000];
	cin>>test;
	while(test--){
		cin>>ch>>k;
		strcpy(s, ch.c_str());
		flag1=0;
		flag=1;
		count=0;
		for(i=0;i<ch.length();i++){
		if((s[i]== '+') && (flag==1)){
			continue;
		}
		else{
		
			flag=0;
			if(k>=ch.length()-i+1 && flag2==0){
			
				flag1=1;
				break;
			}
			if(s[i]=='+'){
				flag2=1;
				
				s[i]='-';
				
			}
			else if(s[i]=='-'){
				flag2=1;
				
				s[i]='+';
				
			}
			
			t++;
			if(t==k){
				flag=1;
				flag2=0;
				t=0;
				i=temp;
				count++;
			
			}
			if(t==1){
				temp=i;
			}
						
		}
		}
		if(flag1==1){
			s1[mm]=-1;
			mm++;
		
		}
		else{
			s1[mm]=count;
			mm++;
	
		}
		
	}
	for(i=0;i<mm;i++){
		cout<<"Case #"<<i+1<<": ";
		if(s1[i]==-1){
			cout<<"IMPOSSIBLE\n";
		}
		else{
			cout<<s1[i]<<"\n";
		}
	}
	return 0;
}

