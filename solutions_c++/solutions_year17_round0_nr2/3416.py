#include<iostream>
#include<fstream>
using namespace std;
bool valid(string s){
	int i;
	int len=s.length();
	for (i=1;i<len;i++){
		if (s[i]<s[i-1]) return false;
	}
	return true;
}
bool reduceChecker(string s){
	int i;
	int len=s.length();
	string chk="";
	for (i=0;i<len;i++) chk=chk+"1";
	if (s<chk) return true;
	return false;
}
string workout(string s){
	int i,curpos;
	int len=s.length();
	string ans="";
	bool flag=true;
	char ch;
	/*
	for (i=0;i<len-1;i++){
		if (flag==false) {
			ans=ans+"9";
			continue;
		}
		if (s[i]>s[i+1]){
			//cout<<"s[i]="<<s[i]<<endl; 
			ch=s[i]-1;
			//cout<<"ch="<<ch<<endl;
			ans=ans+ch;
			flag=false;
			continue;
		} else {
			ans=ans+s[i];
		}
	}*/
	curpos=0;
	for (i=0;i<len-1;i++){
		if (s[i]<s[i+1]) {
			curpos=i+1;
			continue;
		}
		if (s[i]>s[i+1]){
			ch=s[i]-1;
			break;
		}
	}
	for (i=0;i<curpos;i++) ans=ans+s[i];
	ans=ans+ch;
	for (i=curpos+1;i<len;i++) ans=ans+"9";
	return ans;
}
int main(){
	ifstream in("Q2.in") ;
	ofstream out("Q2.out");
	int n,i,j,len;
	//cin>>n;
	in>>n;
	//cout<<"n="<<n;
	string s,ans;
	for (i=1;i<=n;i++){
		in>>s;
		len=s.length();
		out<<"Case #"<<i<<": ";
		//if (valid(s)) cout<<"Valid"<<endl; else cout<<"Invalid"<<endl; 
		if (valid(s)) {
			out<<s<<endl;
			continue;
		}
		if (reduceChecker(s)){
			ans="";
			for (j=1;j<len;j++) ans=ans+"9";
			out<<ans<<endl;
			continue;
		}
		ans=workout(s);
		out<<ans<<endl;
	}
} 
