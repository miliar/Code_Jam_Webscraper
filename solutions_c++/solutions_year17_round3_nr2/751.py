#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


void recSort(vector<int> & toSort, vector<int> & carry, int a, int b){
	if(b<a+2)
		return;
	int middle=(a+b)/2;
	recSort(toSort, carry, a, middle);
	recSort(toSort, carry, middle, b);
	//merge
	vector<int> merged; vector<int> merged2;
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

void sort_carry(vector<int> & toSort, vector<int> & carry){
	recSort(toSort, carry, 0, toSort.size());
}

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("B-large.in");
	ofstream outputfile("myoutput.txt");
	int T, AC, AJ, r, d, between, nswitch, previous_end, CT, JT, posc, posj, sumCS, sumJS, M=24*60;
	vector<int> CB, CE, JB, JE, CS, JS;
	bool last=true;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		CB.clear(); CE.clear(); JB.clear(); JE.clear(); CS.clear(); JS.clear();
		between=0; nswitch=0; CT=0; JT=0;
		file>>AC>>AJ;
		for(int i=0;i<AC;i++){
			file>>r>>d;
			CB.push_back(r); CE.push_back(d);
		}
		for(int i=0;i<AJ;i++){
			file>>r>>d;
			JB.push_back(r); JE.push_back(d);
		}
		//solve
		sort_carry(CB, CE); sort_carry(JB, JE);
		CB.push_back(M+1); JB.push_back(M+1);
		posc=0; posj=0;
		last=(CE[AC-1]>JE[AJ-1]);
		previous_end=last?(CE[AC-1]-M):(JE[AJ-1]-M);
		while(posc<AC || posj<AJ){
			if(CB[posc]<JB[posj]){
				if(last)
					CS.push_back(CB[posc]-previous_end);
				else{
					between+=(CB[posc]-previous_end);
					nswitch++;
				}
				CT+=CE[posc]-CB[posc];
				last=true;
				previous_end=CE[posc];
				posc++;
			}else{
				if(!last)
					JS.push_back(JB[posj]-previous_end);
				else{
					between+=(JB[posj]-previous_end);
					nswitch++;
				}
				JT+=JE[posj]-JB[posj];
				last=false;
				previous_end=JE[posj];
				posj++;
			}
		}
		sort(CS.begin(), CS.end()); sort(JS.begin(), JS.end());
		sumCS=0; sumJS=0;
		for(int i=0; i<CS.size(); i++)
			sumCS+=CS[i];
		for(int i=0; i<JS.size(); i++)
			sumJS+=JS[i];
		posc=CS.size()-1; posj=JS.size()-1;
		while(CT+sumCS+between<M/2){
			nswitch+=2;
			CT+=JS[posj];
			posj--;
		}
		while(JT+sumJS+between<M/2){
			nswitch+=2;
			JT+=CS[posc];
			posc--;
		}
		//write output
		outputfile<<"Case #"<<(t+1)<<": "<<nswitch<<endl;
	}
	file.close();
	outputfile.close();
}

