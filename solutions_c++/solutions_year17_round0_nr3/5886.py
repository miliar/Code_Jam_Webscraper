#include <iostream>
#include <cstring>
using namespace std;

bool stall[1000001];
long ls,rs;

int buscar_medio_mayor (int n){
	int medio,i=0,aux=0, mayor=0,aux2=0;

	for (int j=0 ; j <= n+1 ; j++){
		if (stall[j]){
			aux = j - i;
			if (mayor < aux){
				mayor = aux;
				aux2 = i + j;
			}
			aux = 0;
			i = j;
		}
	}
	medio = aux2 /2;
	return medio;
}

int ls_and_rs(int mid, int n){
	ls=0;
	rs=0;
	for (int i = mid-1 ; i>0 && !stall[i] ; i--){
		ls++;
	}
	for(int i = mid+1 ; i<=n+1 && !stall[i]; i++){
		rs++;
	}
}

int main(){
	int t,p;
	cin >> t;
	p=t;
	while (t--){
		memset (stall,0,sizeof(stall));
		int n,k,medio;
		cin >> n >> k;
		stall[0] = true;
		stall[n+1] = true;
		for (int i=0 ; i < k ; i++){
			medio = buscar_medio_mayor(n);
			stall[medio] = true;			 	
		}
		ls_and_rs(medio, n);
		cout << "Case #" << p-t << ": " << max(ls,rs) << " " << min(ls,rs) << endl;
	}
}
