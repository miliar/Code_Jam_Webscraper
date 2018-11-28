#include <iostream>
#include <vector>

using namespace std;

int T;
unsigned long long K, iK, N, iN, emp, ill;
int* stalls;
unsigned long long *lsV, *rsV, *minV, *maxV;
vector<unsigned long long> maxMins, minMaxs;

template<typename T>
void printArray(T* x){
	unsigned long long ill;
	for(ill=0; ill<N; ill++){
		cout << x[ill] << '\t';
	}
	cout << endl;
}

void printVector(vector<unsigned long long> v){
	unsigned long long ill;
	for(ill=0; ill<v.size(); ill++){
		cout << v[ill] << '\t';
	}
	cout << endl;
}

int main(int argc, char** argv){
	int iCase = 1;
	cin >> T;
	while(T--){
		cin >> N;
		N += 2;
		stalls = new int[N];
		lsV = new unsigned long long[N];
		rsV = new unsigned long long[N];
		minV = new unsigned long long[N];
		maxV = new unsigned long long[N];
		stalls[0]=1;
		for(iN=1; iN<(N-1); stalls[iN++]=0);
		stalls[N-1]=1;
		cin >> K;
		for(iK=0; iK<K; iK++){
			maxMins.clear();
			minMaxs.clear();
			unsigned long long maxMin=0, minMax=0;
			rsV[N-1]=0;
			for(ill=(N-1); ill>0; ill--){
				if(stalls[ill+1])
					rsV[ill]=0;
				else
					rsV[ill]=rsV[ill+1]+1;
			}
			lsV[0]=0;
			minV[0]=0;
			for(ill=1; ill<N; ill++){
				if(stalls[ill-1])
					lsV[ill]=0;
				else
					lsV[ill]=lsV[ill-1]+1;
				minV[ill] = (lsV[ill]>rsV[ill]) ? rsV[ill] : lsV[ill];
				maxV[ill] = (lsV[ill]<rsV[ill]) ? rsV[ill] : lsV[ill];
				if(!stalls[ill]){
					if(minV[ill]>maxMin){
						maxMin = minV[ill];
						maxMins.clear();
						maxMins.push_back(ill);
					}
					else if(minV[ill]==maxMin){
						maxMins.push_back(ill);
					}
				}
			}
			for(ill=0; ill<maxMins.size(); ill++){
				if(maxV[maxMins[ill]]>minMax){
					minMax = maxV[maxMins[ill]];
					minMaxs.clear();
					minMaxs.push_back(maxMins[ill]);
				}
				else if(maxV[maxMins[ill]]==minMax){
					minMaxs.push_back(maxMins[ill]);
				}
			}
			//printArray(stalls);
			stalls[minMaxs[0]]=1;
			//printArray(lsV);
			//printArray(rsV);
			//printArray(minV);
			//printArray(maxV);
			//printVector(maxMins);
			//printVector(minMaxs);
			//cout << endl << endl; 
		}
		cout << "Case #" << iCase << ": " << maxV[minMaxs[0]];
		cout << " " << minV[minMaxs[0]] << endl;
		iCase++;
		delete[] lsV, rsV, minV, maxV;
	}
}

