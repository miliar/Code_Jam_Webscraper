//============================================================================
// Name        : GCJ2016C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "/home/doma/workspace/quick_start.h"


using namespace std;

void printMo2(long double mo,int round, fstream& myfileOut){
	//std::cout << std::fixed;
	//std::cout << std::setprecision(6);

	myfileOut<<"Case #"<<round<<": "<<fixed<<setprecision(8)<<mo<<endl;
	cout<<"Case #"<<round<<": "<< fixed<<setprecision(8)<<mo<<endl;
}
void feladat1(){
	string feladat="A";
	int szam=2;
	//cin>>szam;
	string files[]={"be1",feladat+"-small-attempt5",feladat+"-large"};
	string filename=files[szam];
	fstream myfileIn((filename+".in").c_str(),fstream::in);
	fstream myfileOut((filename+".out").c_str(),fstream::out);

	int T;

	myfileIn>>T;
	cout<<T<<endl;
	for(int round=1;round<=T;round++){
		unsigned int N,K;
		myfileIn>>N>>K;

		vector<pair<int,int> > pancakes;
		For(i,N){
			int r,h;
			myfileIn>>r>>h;
			pancakes.push_back(make_pair(r,h));
		}

		long long int max=0;
		For(i,N){
			vector<pair<long long int,int> > pancakes_i;
			For(j,N){
				long long int r=pancakes[j].first;
				long long int h=pancakes[j].second;
				long long int oldal=2*r*h;
				if(pancakes[j].first<=pancakes[i].first and i!=j){
					pancakes_i.push_back(make_pair(oldal,j));
				}
			}
			sort(pancakes_i.begin(),pancakes_i.end());

			long long int r=pancakes[i].first;
			long long int h=pancakes[i].second;
			long long int surface=r*r;

			int szam1=pancakes_i.size();
			for(int k=0;k<((K-1)<szam1?K-1:szam1);k++){
				surface+=pancakes_i[pancakes_i.size()-1-k].first;
			}
			surface+=2*r*h;

			if(surface>max) max=surface;
		}

		long double max1=max;
		long double mo=max1*M_PI;
		printMo2(mo,round,myfileOut);
	}
}
void feladat2(){
	string feladat="B";
	int szam=0;
	//cin>>szam;
	string files[]={"be1",feladat+"-small-attempt0",feladat+"-large"};
	string filename=files[szam];
	fstream myfileIn((filename+".in").c_str(),fstream::in);
	fstream myfileOut((filename+".out").c_str(),fstream::out);

	int T;

	myfileIn>>T;
	cout<<T<<endl;
	for(int round=1;round<=T;round++){
		unsigned int N;
		myfileIn>>N;

		vector<int> v=beolv(myfileIn,N);
		int mo=-1;
		printMo(mo,round,myfileOut);
	}
}
void feladat3(){
	string feladat="C";
	int szam=0;
	//cin>>szam;
	string files[]={"be1",feladat+"-small-attempt0",feladat+"-large"};
	string filename=files[szam];
	fstream myfileIn((filename+".in").c_str(),fstream::in);
	fstream myfileOut((filename+".out").c_str(),fstream::out);

	int T;

	myfileIn>>T;
	cout<<T<<endl;
	for(int round=1;round<=T;round++){
		unsigned int N;
		myfileIn>>N;

		vector<int> v=beolv(myfileIn,N);
		int mo=-1;
		printMo(mo,round,myfileOut);
	}
}
int main() {
	feladat1();

//	vector<int> v;
//	v.push_back(2);
//	v.push_back(1);
//	sort(v.begin(),v.end());
//	print(v);

	//feladat2();
	//feladat3();
	return 0;
}
