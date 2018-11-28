#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

long long findMaxPos(vector<long long> v){
	long long m = v[0];
	long long pos = 0;
	
	for (long long i = 1; i < v.size(); i++){
		if(v[i] > m){
			m = v[i];
			pos = i;
		}
	}
	
	return pos;
}

long long solve2(long long N, long long K, long long &lmax, long long &lmin){
	long long g = 1;
	long long n = 1;
	long long tab[2][2] = {{1, 0},{N, 0}};
	
	while(K > n){
		K -= n;
		n *= 2;
		
		long long temp[2][2] = {{0, 0},{-1, -1}};
		long long g_min = 0, g_max = 0;
		
		for (int i = 0; i < 2; i++){
			if (tab[0][i] > 0){
		
				g_min = (tab[1][i] - 1) / 2;
				g_max = (tab[1][i] - 1) - (tab[1][i] - 1) / 2;
				
				for (int j = 0; j < 2; j++){
					if (temp[1][j] == -1 || temp[1][j] == g_max){
						temp[1][j] = g_max;
						temp[0][j] += tab[0][i];
						break;
					}
				}
				
				for (int j = 0; j < 2; j++){
					if (temp[1][j] == -1 || temp[1][j] == g_min){
						temp[1][j] = g_min;
						temp[0][j] += tab[0][i];
						break;
					}
				}	
			}
		}
		
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 2; j++)
				tab[i][j] = temp[i][j];
	}
	
	int slot = tab[1][0] > tab[1][1] ? 0 : 1;
	slot = K <= tab[0][slot] ? slot : (slot == 1 ? 0 : 1);
	
	lmin = (tab[1][slot] - 1) / 2;
	lmax = (tab[1][slot] - 1) - (tab[1][slot] - 1) / 2;
}

void solve(long long N, long long K, long long &lmin, long long &lmax){
	vector<long long> v;
	v.push_back(N);
	
	for(long long i = 1; i < K; i++){
		long long pos = findMaxPos(v);
		long long m = v[pos] - 1;
		v.push_back(m / 2);
		v.push_back(m - m / 2);
		v.erase(v.begin() + pos);
	}
	
	long long m = v[findMaxPos(v)] - 1; 
	lmax = m - m / 2;
	lmin = m / 2;
}


int main() {	
	ifstream input("C-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			long long N;
			long long K;
			long long lmin = 0, lmax = 0;
			
			input >> N >> K;
			
			
			
			solve2(N, K, lmax, lmin);
			cout << "Case #" << n << ": " << lmax << " " << lmin << "\n";	
			output << "Case #" << n << ": " << lmax << " " << lmin << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
