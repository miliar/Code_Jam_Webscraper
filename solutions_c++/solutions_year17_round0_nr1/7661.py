#include <bits/stdc++.h>
using namespace std;

int main(void){
	ofstream fout("out.txt");
	ifstream fin("input.txt");
	int t;
	fin >> t;
	for(int i=1; i <= t; i++){
		string s;
		int k;
		fin>> s;
		fin>> k;
		vector<int> arr(s.size(), 0);
		for(int j=0; j != s.size(); j++){
			if(s[j] == '+') arr[j] = 1;
			else arr[j] = 0;
		}
		int count = 0;
		for(int zz = 0; zz <= s.size()-k; zz++){
			if(arr[zz] == 0){
				count++;
				for(int pq=0; pq != k; pq++) {
					arr[zz+pq] += 1;
					arr[zz+pq] %= 2;
				}
			}
		}
		int isdone = true;
		for(int lm = 0; lm != s.size(); lm++) if(! arr[lm]) isdone = false;
		fout<< "Case #" << i <<": ";
		if(! isdone) fout << "IMPOSSIBLE\n";
		else fout<< count << "\n";
	}
	return 0;
}