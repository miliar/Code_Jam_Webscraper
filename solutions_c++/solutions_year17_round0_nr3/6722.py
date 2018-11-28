#include<bits/stdc++.h>

using namespace std;

int main(){

	int t, caso = 0;
	
	cin >> t;	
	
	while(t--){
		caso++;
		
		int n, k, ans1, ans2;
		
		cin >> n >> k;
		
		printf("Case #%d: ", caso);
		
		if (n == k){
			cout << 0 << " " << 0 << endl;
			continue;
		}
		
		int vet[n];
		
		memset(vet, 0, sizeof vet);
		
		while(k--){
			long long e = 0, d = 0, eAux = -1, dAux = -1;
			
			for (int i = 0; i < n; i++){
		
				if (vet[i] == 0){
					if (eAux == -1)
						eAux = i;
				}else{
					dAux = i - 1;
				
					if (eAux != -1 && dAux - eAux >= d - e){
						e = eAux;
						d = dAux;	
					}
					
					eAux = dAux = -1;
				}
			}
			
			if (dAux == -1) dAux = n - 1;
			
			if (eAux != -1 && dAux - eAux >= d - e){
				e = eAux;
				d = dAux;	
			}
			
			int pos = e + (d - e) / 2;
			vet[pos] = 1;
			
			if (k == 0){
				/*for (int i = 0; i < n; i++)
					cout << vet[i];
					
				cout << endl;	*/
					
				ans1 = 0;
				ans2 = n - 1;
				
				for (int j = pos - 1; j >= 0; j--)
					if (vet[j] == 1){
						ans1 = j + 1;
						break;
					}
					
				for (int j = pos + 1; j < n; j++)
					if (vet[j] == 1){
						ans2 = j - 1;
						break;
					}
					
				ans1 = pos - ans1;
				ans2 = ans2 - pos;		
			}
		}
		
		cout << max(ans1, ans2) << " " << min(ans1, ans2) << endl;			
	}
	
	return 0;

}
