//============================================================================
// Name        : google_code_jam2017.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <limits.h>
#include <stdlib.h>     /* atoi */
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>

using namespace std;


#define For(i,n) for(unsigned int i=0;i<(unsigned) n;i++)
#define max_v(v) (*(max_element(v.begin(),v.end())))
template<typename T>
void printMo(T mo,int round, fstream& myfileOut){
	(myfileOut)<<"Case #"<<round<<": "<<mo<<endl;
	cout<<"Case #"<<round<<": "<<mo<<endl;
}

int valt1(string str){
	int sum=0;
	For(i,(int) str.size()-1){
		if(str[i]!=str[i+1]){
			sum++;
		}
	}
	return sum;
}
int mo1(string str,int K){
	int valt=valt1(str);

	return 0;
}
void feladat1(){
	int szam=0;
	//cin>>szam;
	string files[]={"A-small-practice","A-large-practice"};
	string filename=files[szam];
	fstream myfileIn((filename+".in").c_str());
	fstream myfileOut((filename+".out").c_str(),fstream::out);

	int T;
	myfileIn>>T;
	cout<<T<<endl;

	for(int i=1;i<=T;i++){
		string str;
		int K;

		myfileIn>>str;
		myfileIn>>K;
		int mo=mo1(str,K);
		printMo(mo,i,myfileOut);
	}


	myfileIn.close();
	myfileOut.close();
}
int toInt(char c){
	return c-48;
}
char toChar(int a){
	return a+48;
}
string toString(int i){
	std::stringstream ss;
	ss << i;

	std::string str;
	ss >> str;
	return str;
}
string mo2(string str){
	bool kilenc=0;
	For(i,(int)str.size()-1){
		//cout<<toInt(str[i])<<endl;
		if(kilenc){
			str[i+1]='9';
		}
		else if(toInt(str[i])>toInt(str[i+1])){

			int szam=toInt(str[i]);
			int szam2=toInt(str[i])-1;
			char c=toChar(szam2);
			str[i]=c;
			kilenc=1;
			str[i+1]='9';
			//cout<<i<<endl;
		}
	}

	bool baj=0;
	for(int i=str.size()-1;i>0;i--){
		char c=str[i];
		if(baj){
			str[i]='9';
		}

		if(str[i]=='0' ){
			baj=1;
			str[i]='9';
		}
		else if(toInt(str[i-1])>toInt(str[i])){
			int szam2=toInt(str[i-1])-1;
			char c=toChar(szam2);
			str[i-1]=c;
			str[i]='9';
		}
	}
	if(str[0]=='0' or baj) return str.substr(1);
	else return str;
}
bool tidy(string str){
	//char d[2]={'a','b'};
	//int N=atoi(str.c_str());
	//int elozo=1;
	For(i,str.size()-1){
		if(toInt(str[i])>toInt(str[i+1])){
			return 0;
		}
	}
	return 1;
}
int last_tidy(string str){
	int elozo=1;
	int N=atoi(str.c_str());
	//cout<<N<<endl;
	if(N>1000) return 0;
	else{
		For(i,N+1){

			if(tidy(toString(i))){
				//cout<<i<<" "<<str1<<endl;
				elozo=i;
			}
		}
		return elozo;
	}
}
void feladat2(){
	int szam=2;
	//cin>>szam;
	string files[]={"be1","B-small-attempt1","B-large"};
	string filename=files[szam];
	fstream myfileIn((filename+".in").c_str());
	fstream myfileOut((filename+".out").c_str(),fstream::out);

	int T;
	myfileIn>>T;
	cout<<T<<endl;

	for(int i=1;i<=T;i++){
		string str;
		myfileIn>>str;
		string mo=mo2(str);
		//int mo=last_tidy(str);
		printMo(mo,i,myfileOut);
	}


	myfileIn.close();
	myfileOut.close();
}

int main() {
	//cout<<tidy("123")<<tidy("130");
	feladat2();


	return 0;
}
