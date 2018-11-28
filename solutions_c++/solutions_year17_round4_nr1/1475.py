#include"stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<assert.h>
#include<ctime>
#include<queue>
#include<fstream>
#include<string>
#include <functional>
using namespace std;


const int maxn = 110;
int g[maxn];

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	/*ofstream fout;
	fout.open("test.txt");
	fout << 10 <<endl;
	for (int i = 0; i < 10; i++){
		int t = rand() % 100 + 1;
		fout << t <<" "<<4<<endl;
		for (int j = 0; j < t; j++){
			int v = rand() % 100 + 1;
			fout << v << " ";
		}
		fout << endl;
	}*/
	ifstream fin;
	fin.open("A-large.in");
	fin >> t;
	ofstream fout;
	fout.open("1-large.out");
	fout.precision(20);
	fout.setf(ios::fixed);

	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";

		int n, p;
		fin >> n >> p;
		for (int i = 0; i < n; i++){
			fin >> g[i];
		}
		int ans = 0;
		if (p == 2){
			int cnt = 0;
			for (int i = 0; i < n; i++){
				if (g[i] % 2 == 1) cnt++;
			}
			ans = (cnt + 1) / 2 + n - cnt;
		}
		else if(p==3){
			int c[2] = { 0, 0 };
			for (int i = 0; i < n; i++){
				if (g[i] % 3 == 1) c[0]++;
				else if (g[i] % 3 == 2) c[1]++;
			}
			if (c[0]>c[1]) swap(c[0], c[1]);
			ans = n - c[0] - c[1]+c[0];
			ans += (c[1] - c[0]) / 3;
			if ((c[1] - c[0]) % 3 != 0) ans++;

		}
		else{
			//cout << ti << endl;
			int c[4] = { 0, 0, 0, 0 };
			for (int i = 0; i < n; i++){
				c[g[i] % 4]++;
			}
			ans = 0;
			for (int x = 0; 2 * x <= c[1]&&x<=c[2];x++){// x: 1,1,2
				for (int y = 0; x + y <= c[2] && 2 * y <= c[3]; y++){//y:2,3,3
					for (int z = 0; z + 2 * y <= c[3] && z+2*x <= c[1]; z++){//z:1,3
						int temp = c[0] + x + y + z;
						int remain = 0;
						temp += (c[1] - 2 * x - z) / 4;
						if ((c[1] - 2 * x - z) % 4 != 0) remain += (c[1] - 2 * x - z) % 4;//temp++;
						temp += (c[3] - 2 * y - z) / 4;
						if ((c[3] - 2 * y - z) % 4 != 0) remain += 3*((c[3] - 2 * y - z) % 4);
						temp += (c[2] - x - y) / 2;
						if ((c[2] - x - y) % 2 != 0) remain += 2;
						if (remain != 0) temp++;
						//cout << x << " " << y << " " << z << " " << temp << endl;
						ans = max(ans, temp);
					}
				}

			}
		}
		fout << ans << endl;

	}
	system("Pause");
	return 0;
}
