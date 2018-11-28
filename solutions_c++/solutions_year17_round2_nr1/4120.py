//============================================================================
// Name        : google_code_jam2017B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "/home/doma/workspace/quick_start.h"
using namespace std;

//vector<int> Ki,vector<int> Si,
double mo1(int D,int N,vector<pair<int,int> > par){
	vector<double> Hely;
	vector<double> Seb;

	double K_min=par[0].first;
	double S_min=par[0].second;

	par.push_back(make_pair(D,0));
	//Ki.push_back(D);
	//Si.push_back(0);

	//Hely.push_back(K_min);
	//double ido_max=(D-K_min)/S_min;
	double ido_max=0;

	for(int i=0;i<=N;i++){
		double Si=par[i].second;
		double Ki=par[i].first;
		if(Si<S_min){
			double delta=S_min-Si;
			double ido=(Ki-K_min)/delta;
			double Hely0=S_min*ido+K_min;
			double Seb0=Si;

			if(Hely0<=D+0.0000001){
				Hely.push_back(Hely0);
				Seb.push_back(Seb0);
				K_min=Hely0;
				S_min=Seb0;
				ido_max+=ido;
			}
		}
	}
	return ((double) D)/ido_max;
	//return ido_max;

}
void feladat1(){
	string feladat="A";
	int szam=1;
	//cin>>szam;
	string files[]={"be1",feladat+"-small-attempt1",feladat+"-large-practice"};
	string filename=files[szam];
	fstream myfileIn((filename+".in").c_str(),fstream::in);
	fstream myfileOut((filename+".out").c_str(),fstream::out);

	int T;

	myfileIn>>T;
	cout<<"T: "<<T<<endl;
	for(int round=1;round<=T;round++){
		unsigned int D,N;
		myfileIn>>D>>N;

		//vector<int> v=beolv(myfileIn,N);
		vector<int> Ki(N);
		vector<int> Si(N);
		vector<pair<int,int> > par;
		For(i,N){
			int K,S;
			myfileIn>>K>>S;
			Ki.push_back(K);
			Si.push_back(S);

			par.push_back(make_pair(K,S));
		}
		sort(par.begin(),par.end());

		if(round==28){
			cout<<D<<endl;
			print(Ki);
			print(Si);
		}
		double mo=mo1(D,N,par);
		printMo(mo,round,myfileOut);
	}

	int a=1;
	string s=to_string(a);
}


int main() {
	feladat1();

	double d = 122;

	std::cout << std::fixed;
	std::cout << std::setprecision(6);
	std::cout << d;
	return 0;
}
