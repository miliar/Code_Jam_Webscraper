#include <iostream>
#include <map>
using namespace std;


int main(){
	unsigned N;
	cin >> N;
	
	unsigned long long S;
	unsigned long long K;
	
	unsigned long long dist;
	map<unsigned long long, unsigned long long>::iterator it;
	
	for(unsigned caseNo=1; caseNo<=N; caseNo++){
		cin >> S >> K;
		
		map<unsigned long long, unsigned long long> stallMap; // (Distance, Count)
		stallMap[S] = 1;
		
		while(K > stallMap.rbegin()->second){
			K -= stallMap.rbegin()->second;
			
			if(stallMap.rbegin()->first %2 == 1){ // odd -> same left and right
				dist = (stallMap.rbegin()->first-1)/2;
				
				it = stallMap.find(dist);
				if(it != stallMap.end())
					stallMap[dist] += 2* stallMap.rbegin()->second;
				else
					stallMap[dist] = 2* stallMap.rbegin()->second;
			} else{ // even -> diff left and right
				dist = stallMap.rbegin()->first/2;
				
				it = stallMap.find(dist);
				if(it != stallMap.end())
					stallMap[dist] += stallMap.rbegin()->second;
				else
					stallMap[dist] = stallMap.rbegin()->second;
				
				it = stallMap.find(dist-1);
				if(it != stallMap.end())
					stallMap[dist-1] += stallMap.rbegin()->second;
				else
					stallMap[dist-1] = stallMap.rbegin()->second;
			}
			
			stallMap.erase(stallMap.rbegin()->first);
		}
		
		if(stallMap.rbegin()->first %2 == 1){
			dist = (stallMap.rbegin()->first-1)/2;
			cout << "Case #" << caseNo << ": " << dist << " " << dist << endl;
		} else{
			dist = stallMap.rbegin()->first/2;
			cout << "Case #" << caseNo << ": " << dist << " " << dist-1 << endl;
		}
	}
	
	return 0;
}

