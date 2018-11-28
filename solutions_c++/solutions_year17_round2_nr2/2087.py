#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <fstream>
#include <iomanip>
#include <sstream>
using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("B-small-attempt0.in");
	fout.open("B-small-attempt0.out");

	int t;
	fin>> t;
	for(int tt=0;tt<t;tt++){
		int n,R, O, Y, G,B,V,M,MM,MMM,rest;
		char m,mm,mmm;
		fin>>n>>R>>O>>Y>>G>>B>>V;
		if(R>=Y && R>=B){
			m='R';
			M=R;
			rest=Y+R+B-M;
			mm='Y';
			MM=Y;
			mmm='B';
			MMM=B;
		}
		else if(Y>=R && Y>=B){
			m='Y';
			M=Y;
			rest=Y+R+B-M;
			mm='R';
			MM=R;
			mmm='B';
			MMM=B;
		}
		else{
			m='B';
			M=B;
			rest=Y+R+B-M;
			mm='R';
			MM=R;
			mmm='Y';
			MMM=Y;
		}
		bool possible=true;
		if(M>rest)possible=false;
		if(possible){
			int c=MM-(M-MMM);
			string answer;
			while(c>0){
				answer.push_back(m);
				answer.push_back(mm);
				answer.push_back(mmm);
				M--;
				MM--;
				MMM--;
				c--;
			}
			while(MM>0){
				answer.push_back(m);
				answer.push_back(mm);
				M--;
				MM--;
			}
			while(MMM>0){
				answer.push_back(m);
				answer.push_back(mmm);
				M--;
				MMM--;
			}
			fout <<"Case #"<<tt+1<<": "<< answer <<endl;
		}
		else {
			fout <<"Case #"<<tt+1<<": "<< "IMPOSSIBLE" <<endl;
		}
	}
	return 0;
}
