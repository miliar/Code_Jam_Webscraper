#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <string.h>
#include <fstream>
#include <iostream>
#include <math.h>
#include <algorithm>

#define INF 1e+20
#define EPS 1e-10
#define PI 3.14159265358979323846264338327950288419716939937510

using namespace std;

vector< vector<double> > data;
int N,K;

int main(int argc,char * argv[]){
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int size;
	fin>>size;
	for(int i=0;i<size;i++){
		fin>>N>>K;
		data.clear();
		for(int j=0;j<N;j++){
			vector<double> d;
			double s,t;
			fin>>s>>t;
			d.push_back(2*s*t);
			d.push_back(s*s);
			data.push_back(d);
		}
		double Smax=0;
		sort(data.begin(),data.end());
		reverse(data.begin(),data.end());
		// for(int j=0;j<N;j++){
		// 	cout<<data[j][0]<<" "<<data[j][1]<<endl;
		// }
		for(int j=0;j<N;j++){
			int k=1;
			double S=data[j][0]+data[j][1];
			double r2=data[j][1];
			int l=0;
			if(K==1){
				if(j==0) Smax=S;
				else if(Smax<S&&k==K) Smax=S;
				continue;
			}
			for(l=0;l<N;l++){
				if(l==j) continue;
				if(data[l][1]<=r2){
					S+=data[l][0];
					k++;
					if(k==K) break;
				}
			}
			if(j==0) Smax=S;
			else if(Smax<S&&k==K) Smax=S;
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%.20lf\n",Smax*PI);
		

		
	}
	fout.close();
	fin.close();
	return 1;
}

