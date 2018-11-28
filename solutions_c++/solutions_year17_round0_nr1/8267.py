#include<bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i=(int)a; i<(int)b; i++)
#define INF 0x3f3f3f3f

int main(){
	
	//freopen("A.in", "r", stdin);
	//freopen("Aout.txt", "w", stdout);
	
	int n, bi = 1;
	cin>>n;
	string p;
	int t;
	
	while(n--){
		
		cin>>p>>t;
		int tam = p.size();
		int ini = 0, fim = 0;
		int c = 0;
		rep(i, 0, tam-t+1){
			if(p[i]=='-'){
				c++;
				rep(j, i, i+t){
					if(p[j]=='-') p[j]='+';
					else p[j]='-';
				}
				//cout << p << endl;
			}
		}
		 
		bool achou = true;
		
		rep(i, 0, tam){
			if(p[i]=='-') achou = false;		
		}
		cout << "Case #" << bi++ << ": ";
		if(achou) cout << c << endl;
		else cout << "IMPOSSIBLE" << endl;
		
	}
	
	return 0;
}
