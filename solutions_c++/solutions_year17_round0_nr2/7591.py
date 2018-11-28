#include<iostream>
#include<string>
using namespace std;
int countDigit;
string num;
string LTN(int start,int prev,bool borrow){
	if(start==countDigit)
		return string("\0");
	char temp[2];
	string num2;
	int i=num[start]-'0';
	if(borrow)
		i=9;
	for(;i>=prev;i--){
		temp[0]=(char)(i+'0');
		temp[1]='\0';
		string res=LTN(start+1,i,borrow);
		num2=string(temp)+res;
		if(num2.length()==countDigit-start)
			break;
		borrow=true;
	}
	if(num2.length()<countDigit-start)
		return string("\0");
	return num2;
}
int main(){
	int testCases;
	cin>>testCases;
	int c=0;
	while(testCases--){
		num.clear();
//		string num2;
		cin>>num;
		countDigit=num.length();
		num=LTN(0,0,false);
		c++;	
		cout<<"Case #"<<c<<": ";
	        int start=0;
		if(num[0]=='0')
			start=1;
		for(int i=start;num[i]!='\0';i++)
			cout<<num[i];
		cout<<"\n";
	}
	return 0;
}	
