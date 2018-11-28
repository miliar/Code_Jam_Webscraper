#include<iostream>
#include<cstdio>
#include<map>
using namespace std;


unsigned long long int Ls, Rs;
unsigned long long int N, K;

void findLsRs();
void outputLsRs(int);

int main(){
	
	int T;
	scanf("%d", &T);
	
	for(int i=1;i<=T;i++){
		scanf("%lld %lld", &N, &K);
		findLsRs();
		outputLsRs(i);		
	}
}

void findLsRs(){
	
	map<unsigned long long int, unsigned long long int>  myMap;

	unsigned long long int z = 1, i,j, count;

	map<unsigned long long int, unsigned long long int>::reverse_iterator it;

	map<unsigned long long int, unsigned long long int>::iterator fit;
	
	myMap.insert(make_pair(N,1));
	

	for(;z<K;z++){
		
		it = myMap.rbegin();
		i = (*it).first;
		count = (*it).second;
		myMap[i] = count-1;

		if(myMap[i] == 0){
			myMap.erase(i);
		}

		j = (i-1)/2;

		if(j != 0){
			fit = myMap.find(j);
			if(fit != myMap.end()){
				count = (*fit).second;
				myMap[j] = count + 1;
			}
			else{
				myMap.insert(make_pair(j,1));
			}
		}

		j = (i-1) - (i-1)/2;

		if(j != 0){
                        fit = myMap.find(j);
                        if(fit != myMap.end()){
                                count = (*fit).second;
                                myMap[j] = count + 1;
                        }
                        else{
                                myMap.insert(make_pair(j,1));
                        }
                }

	}

	it = myMap.rbegin();
	i = (*it).first;
	Rs = (i-1) - (i-1)/2;
	Ls = (i-1)/2;
}

void outputLsRs(int i){
	
	printf("Case #%d: %lld %lld\n", i, Rs, Ls);
}
