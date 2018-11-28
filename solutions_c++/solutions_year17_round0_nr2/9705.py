#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int t;
string s;

int main(){
	int n, caso=1;

	cin>>n;
	while(n--){
			string s,r;
		
		cin>>s;
		t=s.size();
		
		int j=0;
		for(int i=0;i<s.size()-1;i++){
			if(s[i]!=s[i-1])
				j=i;
			if(s[i]>s[i+1]){
				
				s[j]=s[j]-1;			
				for(j++;j<s.size();j++)
					s[j]=57;
			}
			
		}
		int i=0;
		if(s[0]==48)
		i=1;
		cout<<"Case #"<<caso<<": ";
		for(;i<s.size();i++){
			cout<<s[i]-48;
		}
		cout<<endl;
		caso++;
	}
}
