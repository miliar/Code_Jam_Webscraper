#include <bits/stdc++.h>

using namespace std;

int test, r, c;
char a[30][30];

int main(){
	ifstream fi("A-large.in");
	ofstream fo("A-large.out");

	fi >> test;
	for(int k = 0; k < test; k++){
		fi >> r >> c;
		for(int i = 0; i < r; i++)
			for(int j = 0; j < c; j++) fi >> a[i][j];
		for(int i = 0; i < r; i++)
			for(int j = 1; j < c; j++)
				if(a[i][j] == '?') a[i][j] = a[i][j - 1];
		for(int i = 0; i < r; i++)
			for(int j = c - 2; j >= 0; j--)
				if(a[i][j] == '?') a[i][j] = a[i][j + 1];
		for(int j = 0; j < c; j++)
			for(int i = 1; i < r; i++)
				if(a[i][j] == '?') a[i][j] = a[i - 1][j];
		for(int j = 0; j < c; j++)
			for(int i = r - 2; i >= 0; i--)
				if(a[i][j] == '?') a[i][j] = a[i + 1][j];
		fo << "Case #" << k+1 << ":\n";
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++) fo << a[i][j];
			fo << endl;
		}
	}

	fi.close();
	fo.close();
	return 0;
}
