#include<iostream>
#include<string>
using namespace std;
int countDigit;
string number;
string largestTidyNo(int start,int prev,bool borrow){
	if(start==countDigit)
		return string("\0");
	char temp[2];
	string num2;
	int j=number[start]-'0';
	if(borrow)
		j=9;
	for(;j>=prev;j--){
		temp[0]=(char)(j+'0');
		temp[1]='\0';
		string output=largestTidyNo(start+1,j,borrow);
		num2=string(temp)+output;
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
	int caseNo=0;
	while(testCases--){
		number.clear();
		cin>>number;
		countDigit=number.length();
		number=largestTidyNo(0,0,false);
		caseNo++;	
		cout<<"Case #"<<caseNo<<": ";
	        int start=0;
		if(number[0]=='0')
			start=1;
		for(int j=start;number[j]!='\0';j++)
			cout<<number[j];
		cout<<"\n";
	}
	return 0;
}	
