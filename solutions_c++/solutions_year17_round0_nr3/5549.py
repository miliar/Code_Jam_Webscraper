#include <fstream>
#include <iostream>
#include <cassert>
#include <vector>
using namespace std;

int main() {
	int num, N, K, cntL, cntR, x, maxV;
	vector<int> slots, minS, maxS, slots1, minS1, maxS1;
	int* arr;
	ifstream fin;
	ofstream fout;
	fin.open("C-small-1.in", ifstream::in);
	fout.open("C-small-1.out");
    assert(!fin.fail());
    fin >> num;
	for (int i = 0; i < num; i++){
		fin >> N >> K;
		arr = new int[N+2];
		for (int j = 0; j < N+2; j++)
		    arr[j] = 0;
		arr[0] = 1;
		arr[N+1] = 1;
		for (int j = 0; j < K; j++){
		    slots.clear();
    		minS.clear();
    		maxS.clear();
    		slots1.clear();
    		maxS1.clear();
    		minS1.clear();
		    for (int k = 1; k <= N; k++){
		        if (arr[k] == 0){
		            cntL = 0;
		            cntR = 0;
		            x = k-1;
		            while (arr[x] != 1){
		                cntL++;
		                x--;
		            }
		            x = k+1;
		            while (arr[x] != 1){
		                cntR++;
		                x++;
		            }
		            slots.push_back(k);
		            if (cntL > cntR){
		                minS.push_back(cntR);
		                maxS.push_back(cntL);
		            } else{
		                minS.push_back(cntL);
		                maxS.push_back(cntR);
		            }
		        }
		    }
		    maxV = 0;
		    for (int k = 0; k < minS.size(); k++){
		        if (minS[k] > maxV){
		            maxV = minS[k];
		        }
		    }
		    for (int k = 0; k < minS.size(); k++){
		        if (minS[k] == maxV){
		            slots1.push_back(slots[k]);
		            minS1.push_back(minS[k]);
		            maxS1.push_back(maxS[k]);
		        }
		    }
		    maxV = 0;
		    for (int k = 0; k < maxS1.size(); k++){
		        if (maxS1[k] > maxV){
		            maxV = maxS1[k];
		        }
		    }
	        x = 0;
	        while(maxS1[x] != maxV){
	            x++;
	        }
	        arr[slots1[x]] = 1;
		}
		fout << "Case #" << (i+1) << ": ";
		fout << maxS1[x] << " " << minS1[x] << endl;
	}
	fin.close();
	fout.close();
}