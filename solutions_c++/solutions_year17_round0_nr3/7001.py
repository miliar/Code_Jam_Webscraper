#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ullint;

ullint T;
ullint _case;
ullint N, K;
bitset <1000002> posti;

int main() {
	int i,j,tmp_min,tmp_max;
	int Rs, Ls;
	int maxPos;
	int max_min, max_max;
	
	cin >> T;
	
	for (_case=1; _case<=T; _case++) {
		cin >> N >> K;
		
		N+=2;
		
		posti.reset();
		posti[0] = true;
		posti[N-1] = true;
		
		for (i=0; i<K; i++) { //per ogni persone
		
			max_min=-1;
			max_max=-1;
			for (j=1; j<N-1; j++) { //passa ogni posto
				if (!posti[j])  { //se non e' occupato
				
					for (Ls=0; !posti[j-Ls-1]; Ls++);
					for (Rs=0; !posti[j+Rs+1]; Rs++);
					
					tmp_min = min(Ls,Rs);
					tmp_max = max(Ls,Rs);
					
					if (tmp_min > max_min || (tmp_min == max_min && tmp_max > max_max)) {
						max_min = tmp_min;
						max_max = tmp_max;
						maxPos = j;
					}
				}
			}
			posti[maxPos] = true;
		}
		
		for (Ls=0; !posti[maxPos-Ls-1]; Ls++);
		for (Rs=0; !posti[maxPos+Rs+1]; Rs++);
		
		cout << "case #" << _case << ": " << max(Ls,Rs) << " " << min(Ls,Rs) << "\n";
	}
	
	return 0;
}
