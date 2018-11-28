#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;


void recSort(vector<double> & toSort, vector<double> & carry, int a, int b){
	if(b<a+2)
		return;
	int middle=(a+b)/2;
	recSort(toSort, carry, a, middle);
	recSort(toSort, carry, middle, b);
	//merge
	vector<double> merged; vector<double> merged2;
	int pos1=a, pos2=middle;
	for(int i=a; i<b; i++){
		if(pos1==middle){
			merged.push_back(toSort[pos2]); merged2.push_back(carry[pos2]);
			pos2++;
		}else{
			if(pos2==b){
				merged.push_back(toSort[pos1]); merged2.push_back(carry[pos1]);
				pos1++;
			}else{
				if(toSort[pos1]<toSort[pos2]){
					merged.push_back(toSort[pos1]); merged2.push_back(carry[pos1]);
					pos1++;
				}else{
					merged.push_back(toSort[pos2]); merged2.push_back(carry[pos2]);
					pos2++;
				}
			}
		}
	}
	for(int i=a; i<b; i++){
		toSort[i]=merged[i-a]; carry[i]=merged2[i-a];
	}
}

void sort(vector<double> & toSort, vector<double> & carry){
	recSort(toSort, carry, 0, toSort.size());
}

int main(){
	cout<<"launching function main"<<endl;
	cout.precision(10);
	ifstream file("A-large.in");
	ofstream outputfile("myoutput.txt");
	int T, N, K, index_overhead;
	double Pi = 3.1415926535897, h, r, area, maxRR, overhead, new_add;
	vector<double> RR, THR;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		RR.clear(); THR.clear();
		file>>N>>K;
		RR.resize(N); THR.resize(N);
		for(int i=0;i<N;i++){
			file>>r>>h;
			THR[i]=2*h*r; RR[i]=r*r;
		}
		//solve
		sort(THR, RR);
		area=0; maxRR=0; overhead=0; index_overhead=0;
		for(int i=0; i<(K-1); i++){
			maxRR=max(maxRR, RR[N-1-i]);
			area+=THR[N-1-i];
		}
		for(int i=(K-1); i<N; i++){
			new_add=max(0.0,RR[N-1-i]-maxRR)+THR[N-1-i];
			overhead=max(overhead,new_add);
		}
		//write output
//		outputfile<<"Case #"<<(t+1)<<": "<<(Pi*(area+maxRR+overhead))<<endl;
		outputfile<<"Case #"<<(t+1)<<": "<<setprecision(10)<<(Pi*(area+maxRR+overhead))<<endl;
	}
	file.close();
	outputfile.close();
}

