#include <iostream>
using namespace std;

int n, c, m;
int ticket[1001][1001];
int totpos[1001];

void testcase(){
	cin >> n >> c >> m;
	for(int i=1; i<=c; i++) for(int j=1; j<=n; j++) ticket[i][j] = 0;
	for(int i=1; i<=n; i++) totpos[i] = 0;
	
	for(int i=0; i<m; i++){
		int p, b; cin >> p >> b;
		ticket[b][p]++;
		totpos[p]++;
	}
	
	int rides = totpos[1];
	int prom = 0;
	
	for(int i=0; i<ticket[1][1]; i++){
		int pos = 0;
		int num = 0;
		for(int p=2; p<=n; p++) if(ticket[2][p] > 0 && totpos[p] > num){
			num = totpos[p];
			pos = p;
		}
		if(pos != 0){
			ticket[2][pos]--;
			totpos[pos]--;
		}
	}
	for(int i=0; i<ticket[2][1]; i++){
		int pos = 0;
		int num = 0;
		for(int p=2; p<=n; p++) if(ticket[1][p] > 0 && totpos[p] > num){
			num = totpos[p];
			pos = p;
		}
		if(pos != 0){
			ticket[1][pos]--;
			totpos[pos]--;
		}
	}
	
	int t1 = 0;
	int t2 = 0;
	for(int p=2; p<=n; p++){
		t1 += ticket[1][p];
		t2 += ticket[2][p];
	}
	
	if(t1 > t2){
		rides += t1;
		for(int p=2; p<=n; p++) if(totpos[p] > t1) prom = totpos[p] - t1;
	}else{
		rides += t2;
		for(int p=2; p<=n; p++) if(totpos[p] > t2) prom = totpos[p] - t2;
	}
	
	cout << rides << ' ' << prom << endl;
}

int main(){
	int t; cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		testcase();
	}
	return 0;
}
