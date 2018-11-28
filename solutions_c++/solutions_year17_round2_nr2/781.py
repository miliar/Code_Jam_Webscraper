#include <iostream>
#include <cstdio>
using namespace std;

char name[] = {'R','O','Y','G','B','V'};

int c[6];

void put(int col){
	cout << name[col];
	while(c[(col + 3) % 6] > 0){
		cout << name[(col + 3) % 6] << name[col];
		c[(col + 3) % 6]--;
	}
	c[col]--;
}

int main(){
	int t;
	cin >> t;
	for(int a = 0;a < t;a++){
		int n,ma,num;
		cin >> n;
		for(int i = 0;i < 6;i++) cin >> c[i];
		printf("Case #%d: ",a + 1);
		bool flag = false;
		for(int i = 0;i < 6;i++){
			if(c[i % 6] == c[(i + 3) % 6] && !c[(i + 1) % 6] && !c[(i + 2) % 6] && !c[(i + 4) % 6] && !c[(i + 5) % 6]){
				for(int j = 0;j < n;j++){
					if(j % 2) cout << name[(i + 3) % 6];
					else cout << name[i];
				}
				cout << endl;
				flag = true;
				break;
			}
		}
		if(flag) continue;
		if((c[3] && c[0] <= c[3]) || (c[5] && c[2] <= c[5]) || (c[1] && c[4] <= c[1])){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		c[0] -= c[3];
		c[2] -= c[5];
		c[4] -= c[1];
		if(c[0] > c[2] + c[4] || c[2] > c[0] + c[4] || c[4] > c[0] + c[2]){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if(c[0] > c[2]){
			if(c[0] > c[4]) ma = 0;
			else ma = 4;
		}else{
			if(c[2] < c[4]) ma = 4;
			else ma = 2;
		}
		num = c[(ma + 2) % 6] + c[(ma + 4) % 6] - c[ma];
		while(c[0] > 0 || c[2] > 0 || c[4] > 0){
			put(ma);
			if(num){
				put((ma + 2) % 6);
				put((ma + 4) % 6);
				num--;
			}else{
				if(c[(ma + 2) % 6]) put((ma + 2) % 6);
				else put((ma + 4) % 6);
			}
		}
		cout << endl;
	}
	return 0;
}