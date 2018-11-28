#include <algorithm>
#include <iostream>
#include <cmath>
#include <bitset>
#include <sstream>
#include <string>
#include <vector>

typedef   long long unsigned int bigint;

using namespace std;

class Matrix {
public:
	int **arr;
	int size;
	Matrix(int n):size(n) {
		arr = new int *[n]();
		if (arr) {
			for (int i = 0; i < n; i++) {
				arr[i] = new int[n]();
			}
		}
	}
	void operator=(Matrix b) {
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				this->arr[i][j] = b.arr[i][j];
			}
		}
	}
	void print() {
		for (int i = 0; i < size;i++) {
			for (int j = 0; j < size; j++) {
				cout << arr[i][j] << " ";
			}
			cout << endl;
		}

	}
};

bool check(int **map,int n){
	int countm=0;
	int countk=0;
	for(int i=0;i<n;i++){
		countm=0;
		countk=0;
		for(int j=0;j<n;j++){
			if(map[i][j]>0) countm++;
			if(map[i][j]==1) countk++;
		}
		if(countm-1!=countk && countm!=countk) return false;
	}
	for(int i=0;i<n;i++){
		countm=0;
		countk=0;
		for(int j=0;j<n;j++){
			if(map[j][i]>0) countm++;
			if(map[j][i]==1) countk++;
		}
		if(countm-1!=countk && countm!=countk) return false;
	}
	for(int i=0;i<n;i++){
		countm=0;
		countk=0;
		for(int j=0;j<n;j++){
			if(map[i][j]>0) countm++;
			if(map[i][j]==1) countk++;
		}
		if(countm-1!=countk && countm!=countk) return false;
	}
	for(int k=0;k<n;k++){
		int i=0;
		int j=k;
		countm=0;
		countk=0;
		while(i<n && i>=0 && j<n && j>=0){
			if(map[i][j]>0) countm++;
			if(map[i][j]==2) countk++;
			i++;
			j++;
		}
		if(countm-1!=countk && countm!=countk) return false;	
	}
	for(int k=0;k<n;k++){
		int i=0;
		int j=k;
		countm=0;
		countk=0;
		while(i<n && i>=0 && j<n && j>=0){
			if(map[i][j]>0) countm++;
			if(map[i][j]==2) countk++;
			i++;
			j--;
		}
		if(countm-1!=countk && countm!=countk) return false;	
	}
	for(int k=0;k<n;k++){
		int i=k;
		int j=0;
		countm=0;
		countk=0;
		while(i<n && i>=0 && j<n && j>=0){
			if(map[i][j]>0) countm++;
			if(map[i][j]==2) countk++;
			i++;
			j++;
		}
		if(countm-1!=countk && countm!=countk) return false;	
	}
	for(int k=0;k<n;k++){
		int i=k;
		int j=n-1;
		countm=0;
		countk=0;
		while(i<n && i>=0 && j<n && j>=0){
			if(map[i][j]>0) countm++;
			if(map[i][j]==2) countk++;
			i++;
			j--;
		}
		if(countm-1!=countk && countm!=countk) return false;	
	}
	return true;
}

int calc(int **map,int n){
	int sum=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			sum+=(map[i][j]+1)/2;
		}
	}
	return sum;
}

int MAX=0;
Matrix *Mmap;
		
void DFS(Matrix map,int n,int i,int j){
	if(j>=n){
		j=0;
		i++;
		if (i>=n){
			int temp=calc(map.arr,n);
			if(temp>MAX){
				MAX=temp;
				*Mmap=map;
			}
			//cout << "-----------" << endl;
			//cout << temp << endl;
			//map.print();
			return ;
		}
	}
	
	while(map.arr[i][j]<4){	
		//check
		//true
		if(check(map.arr,n)){	
			DFS(map,n,i,j+1);
		}
		map.arr[i][j]++;
	}
	
	map.arr[i][j]=0;
}

int main(){

	/*Matrix mtest(5);
	Mmap = new Matrix(mtest.size);
	for(int i=0;i<mtest.size;i++)
		mtest.arr[0][i] = 1;
	mtest.arr[0][0] = 3;
	
	DFS(mtest, mtest.size, 1, 0);
	Mmap->print();
	cout << MAX << endl;*/





	char cc[]={'.','+','x','o'};
	
	int a;
	int n,m;
	cin>>a;
	int all=a;
	while(a){
		cin>>n>>m;

		Matrix map(n);
		int c3 = 0;
		for (int i = 0; i < m; i++) {
			int r,c;
			char ch;
			cin >>ch>> r >> c;
			r--;
			c--;
			int temp;
			switch (ch) {
			case '+': temp = 1; break;
			case 'x': temp = 2; break;
			case 'o': temp = 3; break;
			}
			map.arr[r][c] = temp;
			if (temp == 3 || temp==2)
				c3 = c;
		}

		Matrix mm(n);
		
		int r2 = 1, c2 = n-1;
		for (int i = 0; i < n; i++) {
			mm.arr[0][i] = 1;
		}
		mm.arr[0][c3] = 3;
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if ((i == 0 || i == n - 1) && (j != 0)&& j!=n-1) mm.arr[i][j] = 1;
				if (c2 == c3) c2--;

				if (r2 == i && j == c2) {
					mm.arr[i][j] = 2;
					r2++;
					c2--;
				}
				 
			}
		}
		mm.arr[0][c3] = 3;
		//cout << c3 + 1 << endl;
		if (c3 == 0 &&c3+1!=n-1 && n > 1) mm.arr[n - 1][c3 + 1] = 3;
		//mm.print();

		int count = 0;
		vector<vector<int>> v;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (mm.arr[i][j] != map.arr[i][j]) {
					count++;
					v.push_back({mm.arr[i][j],i,j});
				}
			}
		}
		//mm.print();
		cout << "Case #" << all-a+1 << ": " << calc(mm.arr,mm.size)<<" "<<count<< endl;
		//cout<<check(mm.arr, mm.size) << endl;
		for (int i = 0; i < v.size(); i++) {
			cout << cc[v[i][0]] <<" "<< v[i][1]+1<<" " << v[i][2]+1 << endl;
		}

		a--;
		
	}
	return 0;
}
