#include<iostream>
#include<algorithm>
#include<string>
#include<stdlib.h>

using namespace std;

//#define DEBUG

#ifdef DEBUG
#include<fstream>

ifstream Inputfile;
ofstream Outputfile;

#define	cin		Inputfile
#define	cout	Outputfile

#endif	//#ifdef DEBUG

unsigned long long NUMBER=0;

void FindAnamolyAt(unsigned long long Number,int& NumberOfDigits,int& AnamolyAt,int& digit){
	int lastdigit=Number%10;
	NumberOfDigits=1;
	AnamolyAt=1;
	Number=Number/10;
	int currentdigit=0;
	while(Number){
		NumberOfDigits++;
		AnamolyAt++;
		currentdigit=Number%10;
		Number=Number/10;
		if(currentdigit>lastdigit){
			//AnamolyAt--;
			digit=currentdigit;
			break;
		}
		lastdigit=currentdigit;
	}
	while(Number){
		NumberOfDigits++;
		Number=Number/10;
	}
}

bool CheckIncrementing(unsigned long long Number){
	int lastdigit=Number%10;
	int currentdigit=0;
	Number=Number/10;
	while(Number){
		currentdigit=Number%10;
		Number=Number/10;
		if(currentdigit>lastdigit){
			return false;
		}
		lastdigit=currentdigit;
	}
	return true;
}

void ModifyNumber(unsigned long long& Number,int& NumberOfDigits,int AnamolyAt,int digit){
	int aa=AnamolyAt;//aa=aa-1;
	while(aa){
		Number=Number/10;
		aa--;
	}
	aa=AnamolyAt-1;
	if(!Number) {
		if(digit==1){
			Number=9;aa--;
		}else{
			Number=digit-1;
		}
	}else{
		Number=Number*10;Number=Number+digit-1;
	}
	while(aa){
		Number=Number*10;Number=Number+9;
		aa--;
	}
}

void TestCasesE(int testcaseunmber){
	cout<<"Case #"<<testcaseunmber+1<<": ";
	cin>>NUMBER;
	if(CheckIncrementing(NUMBER)){
		cout<<NUMBER<<endl;
		return;
	}
	int NumberOfDigits=0; int AnamolyAt=0;int wrongdigit;
	//FindAnamolyAt(NUMBER,NumberOfDigits,AnamolyAt,wrongdigit);
	do{
		FindAnamolyAt(NUMBER,NumberOfDigits,AnamolyAt,wrongdigit);
		ModifyNumber(NUMBER,NumberOfDigits,AnamolyAt,wrongdigit);
	}while(!CheckIncrementing(NUMBER));
	cout<<NUMBER<<endl;
}


int main() {

	//AM_Allocate();
#ifdef DEBUG
	Inputfile.open("input.txt");
	Outputfile.open("output.txt");;
#endif // #ifdef DEBUG

	int testcase=0;
	cin>>testcase;
	for(int i=0;i<testcase;i++){
		TestCasesE(i);
	}

#ifdef DEBUG
	Inputfile.close();
	Outputfile.close();
#endif // #ifdef DEBUG
	//AM_DeAllocate();
	return 0;
 }
