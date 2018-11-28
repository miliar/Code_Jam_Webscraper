#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
#define MAX_N 1000000
using occupied = vector<bool>;
using distances = vector<int>;
using stalls_t = vector<int>;

struct output{
	int x;
	int y;
};

void printOccupied(occupied & isOccupied){
	for(const auto & elem: isOccupied){
		if(elem){
			cout << "0";
		} else {
			cout << ".";
		}
	}
	cout << endl;
}
void printDist(distances & dist){
	for(auto elem: dist){
		cout << elem << " ";
	}
	cout << endl;
}

void occupy(int posToOccupy, occupied & isOccupied, distances & ls, distances & rs){

	for(int i = posToOccupy-1, j = 0; i >= 0 && !isOccupied[i] ; i--, j++){
		rs[i] = j;	
	}
	for(int i = posToOccupy+1, j = 0; i < (int)isOccupied.size() && !isOccupied[i] ; i++, j++){
		ls[i] = j;	
	}
	isOccupied[posToOccupy] = true;
}

output putOneAndUpdate(occupied & isOccupied, distances & ls, distances & rs){
	output out;
	long maxVal = 0;

	stalls_t maxStalls;
	for(int i =0, n = isOccupied.size(); i < n; i++){
		if(isOccupied[i]){

		} else {

			long maxDist = min(ls[i], rs[i]);
//			cout << i << " " << maxDist << endl;
			if(maxDist > maxVal){
				maxVal = maxDist;
				maxStalls.clear();
				maxStalls.push_back(i);
			} else if(maxDist == maxVal){
				maxStalls.push_back(i);
			}
		}
	}
//	cout << "Maxstalls" << endl;
//	for(auto elem: maxStalls) {
//		cout << elem << " ";
	//	}
//		cout << endl;
	stalls_t minStalls;
	maxVal = 0;
	for(int i = 0, n = maxStalls.size(); i < n; i++){
		long maxDist = max(ls[maxStalls[i]], rs[maxStalls[i]]);
		if(maxDist > maxVal){
			maxVal = maxDist;
			minStalls.clear();
			minStalls.push_back(maxStalls[i]);
		} else if(maxDist == maxVal){
			minStalls.push_back(maxStalls[i]);
		}
	}
	int posToOccupy = minStalls[0];	
	out.y = min(ls[posToOccupy], rs[posToOccupy]);
	out.x = max(ls[posToOccupy], rs[posToOccupy]);
	occupy(posToOccupy, isOccupied, ls, rs);
//	printOccupied(isOccupied);
//	printDist(ls);
//	printDist(rs);
	return out;
}



output solveProblem_n2(long n, long k){
	output out;
	occupied isOccupied(n, false);
	distances ls(n);
	distances rs(n);
	occupy(0,isOccupied,ls,rs);
	occupy(n-1, isOccupied, ls, rs);
//	printOccupied(isOccupied);
//	printDist(ls);
//	printDist(rs);
	while(k--){
		out = putOneAndUpdate(isOccupied, ls, rs);
	}
	return out;
}

int main(){
	int t;
	cin >> t;
	for(int i = 1; i <=t; i++){
		int n;
		int k;
		cin >> n >> k;
		output out = solveProblem_n2(n+2,k);
		cout << "Case #" << i << ": " << out.x << " "<< out.y << endl;
	}
	return 0;
}
