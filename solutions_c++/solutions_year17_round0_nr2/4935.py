#include <bits/stdc++.h>
#define l long int
#define ll long long int
#define ull unsigned long long int

using namespace std;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int test_case;
	cin>>test_case;
	for(int t_val=1;t_val<=test_case;t_val++){
		cout<<"Case #"<<t_val<<": ";
		string input_str,res_val;
		cin>>input_str;
		int len_str=input_str.length();
		if(len_str==1) res_val=input_str;
		else {
			int flag=0;
			while(flag==0){
				if(flag==1) break;
				int start_val=-1,end_val=-1;
				int checker=0;
				for(int i=0;i<len_str-1;i++){
					if(checker==1) break;
					if(input_str[i]>input_str[i+1]) {
						start_val=i;end_val=i+1;checker=1;
						}
					}
				if(checker==0){
					flag=1;	
				} 
				if(start_val==-1&&end_val==-1){
					res_val=input_str;
					flag=1;	
				} 
				else if(input_str[start_val]=='1'&&input_str[end_val]=='0'){
					for(int j=0;j< len_str-1;j++) {
						res_val+='9';
						}
					flag=1;
					}
				else{
					int temp_val_n= input_str[start_val]-'0';--temp_val_n;
					char charac;
					charac=temp_val_n+'0';
					input_str[start_val]=charac;
					for(int j=end_val;j< len_str;j++){
						input_str[j]='9';	
					}
					res_val=input_str;
					}
				if(flag==1) break;
				}
			}
		
		cout<<res_val<<endl;
		}
	return 0;
	}