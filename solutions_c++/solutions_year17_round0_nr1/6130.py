#include<iostream>
#include<string>
using namespace std;

int main(){
	int t;
	cin>>t;
	int x=1;
	while(t--){
		int f = 0;
		string s1;
		cin>>s1;
		int k;
		cin>>k;
		for(int i=0;i<s1.length()-k+1;i++){
			//cout<<s1[i]<<" "<<i<<endl;
			if(s1[i] == '-'){
				for(int j = i; j < k+i;j++){
					if(s1[j] == '-'){
						s1[j] = '+';
					}else{
						s1[j] = '-';
					}
				}
				f++;
			}
			
			//cout<<s1<<endl;
		}
		
		
		
		bool flag = true;
		for(int i=0;i<s1.length();i++){
			if(s1[i] == '-'){
				flag = false;
			}
		}
		
		
		if(flag){
			cout<<"Case #"<<x<<": "<<f<<endl;
		}else{
			cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl;
		}
		
		x++;
	}
}
