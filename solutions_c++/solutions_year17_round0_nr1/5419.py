#include<iostream>
#include <fstream>
using namespace std;
int k;
bool checkString(string s){
	
	for(int i=0;i<s.length();i++){
		if(s[i]!='+'){
			return false;
		}
	}
	//cout<<"Blah"<<endl;
	return true;
}
int mini = 2000;
void flipPans(int u,string s,int steps){
	//cout<<s<<endl;
	//cout<<"blah"<<endl;
	if(checkString(s)){
		if(steps<mini){
			mini = steps;
			return;
		}
	}
	for(int i=u;i<=s.length()-k;i++){
		string s1 = s;
		for(int j=i;j<i+k;j++){
			if(s1[j]=='+'){
				s1[j]='-';
			}
			else{
				s1[j]='+';
			}
		}
		flipPans(i+1,s1,steps+1);
	}
}
int main(){
ofstream myfile;
  myfile.open ("A-small.out");
  
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
	mini = 2000;
	string s;
	cin>>s;
	cin>>k;
	flipPans(0,s,0);
	if(mini==2000){
		myfile<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
	}
	else{
		myfile<<"Case #"<<i<<": "<<mini<<endl;
	}
	
		
		
	}
	
	myfile.close();	
}
