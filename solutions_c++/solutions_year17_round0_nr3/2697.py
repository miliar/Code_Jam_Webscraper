#include<bits/stdc++.h>
using namespace std;

long long N,K;
map<long long,long long> nseqs;

int main() {
	int C; cin >> C;
	for(int cas = 1; cas<=C; cas++){
		cin >> N >> K;		
		nseqs.clear();
		nseqs[N] = 1;
		long long size;
		while (K > 0){
			size = nseqs.rbegin()->first;
			if (K < nseqs[size]){
				break;
			}
			long long nb = nseqs[size];
			K -= nb;
			map<long long,long long>::iterator iter = nseqs.find(size);
			if (iter != nseqs.end())
				nseqs.erase(iter);
			if (size % 2 == 1){
				nseqs[size/2] += (2*nb);
			}
			else {
				nseqs[size/2] += nb;
				nseqs[size/2 -1] += nb;
			}
		}

		
		cout << "Case #" << cas << ": ";
		if (size % 2 == 0)
			cout << size/2 << " " << size/2 - 1 << endl;
		else 
			cout << size/2 << " " << size/2 << endl;
	}
}
