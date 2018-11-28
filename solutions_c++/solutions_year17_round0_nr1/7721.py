#include<iostream>
#include<cstring>
using namespace std;
int main(){
	int prob,count=0,k,scan1=0,r=0,scan,scan2=0,i,t=0,mm=0,s1[100000],temp;
	string str;
	char s[100000];
	cin>>prob;
	while(prob--){
		cin>>str>>k;
		strcpy(s, str.c_str());
		scan1=0;
		scan=1;
		count=0;
		for(i=0;i<str.length();i++){
		if((s[i]== '+') && (scan==1)){
			continue;
		}
		else{
	
			scan=0;
			if(k>=str.length()-i+1 && scan2==0){
			
				scan1=1;
				break;
			}
			if(s[i]=='+'){
				scan2=1;
				
				s[i]='-';
				
			}
			else if(s[i]=='-'){
				scan2=1;
				
				s[i]='+';
				
			}
			
			t++;
			if(t==k){
				scan=1;
				scan2=0;
				t=0;
				i=temp;
				count++;
			
			}
			if(t==1){
				temp=i;
			}
						
		}
		}
		if(scan1==1){
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

