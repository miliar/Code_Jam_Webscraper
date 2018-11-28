#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
vector<long long int>p;
void dfs(long long int x,long long int max) {
	if (x >max) return;
	p.push_back(x);
	int j = x % 10;
	if (x == 0) j = 1;
	for (;j <= 9;j++)
	{
		dfs(x * 10 + j, max);
	}
}
int main() {
	ifstream inFile;
	ofstream outFile;
	int value;
	long long int num;
	inFile.open("B-small-attempt2.in");
	outFile.open("x.out");
	inFile >> value;
	for(int i=1;i<=value;i++){
		inFile >> num;
		dfs(0, num);
		sort(p.begin(), p.end());
		outFile <<"Case #"<<i<<": "<<p.back() << endl;
		p.clear();
     }
}