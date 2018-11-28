#include<bits/stdc++.h>
using namespace std;



void gen(long long int in, int depth, int size, map<int, vector<long long int> > &searchSpace){
	
	if(size == depth){
		searchSpace[size].push_back(in);
		return;
	}
	for(int i = in % 10; i <= 9; i++){
		gen(in * 10 + i, depth + 1, size, searchSpace);
	}
	
}

long long int solve(long long int N, map<int, vector<long long int> > searchSpace){
	int nDigits = log10(N) + 1;
	bool found = false;
	long long result = 0;
	for(int i = 0; i < searchSpace[nDigits].size(); i++){
		long long curr = searchSpace[nDigits][i];
		if(curr > N){
			break;
		}
		else{
			found = true;
			result = curr;
		}
	}
	return found ? result : searchSpace[nDigits - 1][searchSpace[nDigits - 1].size() - 1];
}

int main(){
	
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	map<int, vector<long long int> > searchSpace;
	searchSpace[1].push_back(0);
	
	for(int i = 1; i <= 18; i++){
		for(int j = 1; j <= 9; j++){
			gen(j, 1, i, searchSpace);	
		}
	}
	
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++){
		long long int N;
		cin >> N;
		printf("Case #%d: %lld\n", i, solve(N, searchSpace));
	}	
}
