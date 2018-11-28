#include <iostream>
#include <string>
#include <vector>
using namespace std;

void solve(int i){
	int R,C;
	char cake[14][14];
	for(int i=0;i<14;i++){
		for(int j=0;j<14;j++){
			cake[i][j] = '-';
		}
	}

	vector<int> x,y;
	cin >> R >> C;
	for(int i=1;i<=R;i++){
		for(int j=1;j<=C;j++){
			cin >> cake[i][j];
			if(cake[i][j] != '?'){
				x.push_back(j);
				y.push_back(i);
			}
		}
	}

	for(int i=0;i<x.size();i++){
		int x_min, x_max, y_min, y_max;
		x_min = x_max = x[i];
		y_min = y_max = y[i];
		//cout << x[i] << " " << y[i] << " " << cake[y[i]][x[i]] << endl;
		while(1){
			bool flag1 = true;
			for(int r=x_min; r<=x_max;r++){
				if(cake[y_min-1][r] != '?')
					flag1 = false;
			}
			if(flag1){
				for(int r=x_min; r<=x_max;r++){
					cake[y_min-1][r] = cake[y[i]][x[i]];
				}
				y_min--;
			}

			bool flag2 = true;
			for(int r=x_min; r<=x_max;r++){
				if(cake[y_max+1][r] != '?')
					flag2 = false;
			}
			if(flag2){
				for(int r=x_min; r<=x_max;r++){
					cake[y_max+1][r] = cake[y[i]][x[i]];
				}
				y_max++;
			}

			bool flag3 = true;
			for(int c=y_min; c<=y_max;c++){
				if(cake[c][x_min-1] != '?')
					flag3 = false;
			}
			if(flag3){
				for(int c=y_min; c<=y_max;c++){
					cake[c][x_min-1] = cake[y[i]][x[i]];
				}
				x_min--;
			}

			bool flag4 = true;
			for(int c=y_min; c<=y_max;c++){
				if(cake[c][x_max+1] != '?')
					flag4 = false;
			}
			if(flag4){
				for(int c=y_min; c<=y_max;c++){
					cake[c][x_max+1] = cake[y[i]][x[i]];
				}
				x_max++;
			}	

			if(!(flag1 || flag2 || flag3 || flag4))
				break;
		}
		/*for(int i=1;i<=R;i++){
			for(int j=1;j<=C;j++){
				cout << cake[i][j];
			}
			cout << endl;
		}cout << endl;*/
	}
	cout << "Case #" << i << ":" << endl;
	for(int i=1;i<=R;i++){
		for(int j=1;j<=C;j++){
			cout << cake[i][j];
		}
		cout << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		solve(i+1);
	}
	return 0;
}