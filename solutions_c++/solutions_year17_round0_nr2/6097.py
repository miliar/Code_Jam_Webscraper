#include<iostream>
#include<string>
using namespace std;

int main(){
	int t;
	cin>>t;
	int x=1;
	while(t--){
		string s1;
		cin>>s1;
		
		for(int i = s1.length()-1;i>0;i--){
		//	cout<<s1<<endl;
			if(s1[i]-'0' < s1[i-1] -'0'){
				for(int j=i;j<s1.length();j++){
					s1[j]='9';
				}
				s1[i-1] = (s1[i-1] - 1);
			}
		}
	
		cout<<"Case #"<<x<<": "<<stol(s1,NULL,10)<<endl;

		x++;
	}
}
