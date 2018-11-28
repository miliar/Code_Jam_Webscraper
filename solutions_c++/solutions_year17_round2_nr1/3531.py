#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include "math.h"
using namespace std;

/*
void swapPanc(string& p, int i){
	if (p[i]=='-'){
		p[i]='+';
	} else {
		p[i]='-';
	}
}

void problemaA(int t){
	int res = 0;
	bool canDo = true;
	string pancakes;
	int flipper;
	cin >> pancakes;
	cin >> flipper;

	for (int i = 0; i < pancakes.size()-flipper+1; ++i){
		if(pancakes[i] == '-'){
			res++;
			for (int j = i; j < min((int )pancakes.size(),i+flipper); ++j){
				swapPanc(pancakes,j);
			}
		}
	}
	for (int i = pancakes.size()-flipper; i < pancakes.size(); ++i){
		if (pancakes[i] == '-'){
			canDo = false;
			break;
		}
	}

	cout << "Case #" << t << ": ";
	if (canDo){
		cout << res << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}

}

void volverIgual(vector<int>& n, int index){
	for (int i = index-1; i >= 0; ++i){
		if (i == 0){
			n[i]--;
			break;
		}
		if(n[i] == n[index] && i!=0){
			n[i] = 9;
		} else {
			n[i+1]--;
			break;
		}
		
	}
}
void problemaB(int t){
	long long int input;
	cin >> input;
	int quantityDigits = floor(log10(input))+1;
	vector<int> number(quantityDigits,0);
	vector<int> result(quantityDigits,0);
	long long int res = 0;

	for (int i = 0; i < quantityDigits; ++i){

		number[quantityDigits-1-i] = input%10;
		input = input/10;
	}


	int i;
	for (i = 0; i < quantityDigits; ++i){
		if (i == quantityDigits-1){
			result[i] = number[i];
			break;
		}
		if (number[i] <= number[i+1]){
			result[i] = number[i];
		} else {
			if(i!=0 && number[i] == number[i-1]){
				result[i] = number[i];
				volverIgual(result,i);
				result[i] = 9;
			} else {
				result[i] = number[i]-1;
			}
			
			break;
		}
	}

	for (i = i+1; i < quantityDigits; ++i){
		result[i] = 9;
	}

	for (i = 0; i < quantityDigits; ++i){
		long long int d = pow(10,quantityDigits-i-1);
		res += result[i]*d;
	}

	cout << "Case #" << t << ": ";
	cout << res << endl;
}

long long int solvEq(long long int a, long long int b, long long int n, long long int l){
	return n-l*a;
}

void problemaC(int t){
	long long int k,n;
	cin >> n;
	cin >> k;
	long long int res = n+2;
	int sobra = 0;
	long long int hasta = floor(log2(k))+1;
	for (int i = 0; i < hasta; ++i){
		if (i == hasta-1){
			long long int p = pow(2,floor(log2(k)));
			long long int cantMayor = solvEq(res-1,res,n+2+p-1,p);
			if (k-p>=cantMayor){
				sobra = (res)%2;
				res = (res)/2;
			} else {
				sobra = (res+1)%2;
				res = (res+1)/2;
			}
			//sobra = (res+1)%2;
			//res = (res+1)/2;
		} else {
			res = (res+1)/2+(res+1)%2;
		}
	}

	
	//int resMin = floor((float)(res-2)/2);
	long long int resMin = res-2;
	long long int resMax = resMin+sobra;

	cout << "Case #" << t << ": ";
	cout << resMax << " " << resMin << endl;
	
}


void agregar(vector< vector<int> >& matrix, vector<int>& l, int& f, int& c){
	if(l[0] == matrix[f][0]){
		matrix[f] = l;
		f++;
	} else if (l[0] == matrix[0][c]){
		for (int j = 1; j < size; ++j){
			matrix[j][0] = l[j];
		}
		c++;
	} else {
		cout << "Error" << endl;
	}
}

void agregar(vector< vector<int> >& matrix, vector<int>& l, int f, int c){
	for (int i = 0; i < l.size(); ++i){
		if()
	}
	if(l[0] == matrix[f][0]){
		matrix[f] = l;
	} else if (l[0] == matrix[0][c]){
		for (int j = 1; j < size; ++j){
			matrix[j][0] = l[j];
		}
	} else {
		cout << "Error" << endl;
	}
}

void problemaBViejo(int i){
	int size;
	cin >> size;
	vector< vector<int> > lists;
	int minorValue = 2501;
	for (int i = 0; i < 2*size-1; ++i){
		vector<int> list;
		for (int i = 0; i < size; ++i){
			int val;
			cin >> val;
			list.push_back(val);
		}
		minorValue = min(list[0],minorValue);

		lists.push_back(row);
	}
	vector<int> row(size,0);
	vector< vector<int> > matrix(size,row);
	for (int i = 0; i < lists.size(); ++i){
		bool first = true;
		if(lists[i][0] == minorValue){
			if(first){
				matrix[0] = lists[i];
			} else {
				for (int j = 1; j < size; ++j){
					matrix[j][0] = lists[i][j];
				}
			}
		}
	}
	sort(lists.begin(), lists.end());
	int i = 1;
	int j = 1;
	while(i<size && j<size){
		if(lists[i+j][0] != matrix[i][0] && lists[i+j][0] != matrix[0][j]){
			if(lists[i+j][0] == matrix[i+1][0]){
				i++;
			} else if (lists[i+j][0] != matrix[0][j+1]){
				j++;
			} else {
				cout << "Error" << endl;
			}
		}
		if(i+j == lists.size()-1){
			agregar(matrix,lists[i+j],i,j);
		}
		if(lists[i+j][0] != lists[i+j+1][0]){
			agregar(matrix,lists[i+j],i,j);
		} else {
			agregarDondePueda(matrix,lists[i+j],i,j);
		}
	}
}
*/

void problemaA(int t){
	long long int d,n;
	cin >> d;
	cin >> n;
	double maxHs = 0;
	for (int i = 0; i < n; ++i){
		long long int pos,vel;
		cin >> pos;
		cin >> vel;
		double hsToFinish = (double )(d-pos)/(double )vel;
		
		if(hsToFinish > maxHs){
			maxHs = hsToFinish;
		}
	}


	double res = (double )d/maxHs;

	cout << "Case #" << t << ": ";
	printf("%.7lf \n",res);

}


void problemaB(int t){
	int  n, r, o, y, g, b, v;
	cin >> n;
	cin >> r;
	cin >> o;
	cin >> y;
	cin >> g;
	cin >> b;
	cin >> v;


	int  fromR, fromO, fromY, fromG, fromB, fromV;
	int  toR, toO, toY, toG, toB, toV;

	fromR = (y+g+b);
	fromY = (r+b+v);
	fromB = (y+r+o);
	fromO = (b);
	fromG = (r);
	fromV = (y);

	


	cout << "Case #" << t << ": ";
	//cout << res << endl;

}


int main(){
	int cantTest;
	cin >> cantTest;
	for (int i = 0; i < cantTest; ++i){
		problemaA(i+1);
	}
	

	return 0;
}
