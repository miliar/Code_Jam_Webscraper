#include<bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i=(int)a; i<(int)b; i++)
#define INF 0x3f3f3f3f

int main(){
	
	//freopen("B.in", "r", stdin);
	//freopen("Bout.txt", "w", stdout);
	
	int n, x, aux, ans, b = 1;
	cin>>n;
	
	rep(i, 0, n){
		
		cin>>x;
		for(int j=x; j>=0; j--){
			aux = j;
			
			ans = (j%10);
			
			while(j>0){
				j/=10;
				if(ans<(j%10)){
					j = aux;
					break;
				}
				ans=(j%10);
			}
			
			if(j==0){
				cout << "Case #" << b++ << ": ";
				cout << aux << endl;
				break;
			}
			j = aux;
		}
	}
	
	return 0;
}
