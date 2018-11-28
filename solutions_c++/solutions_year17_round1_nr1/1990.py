#include <iostream>
using namespace std;

int r,c;
char cake[30][30];

int main() {
	int t;
	int n=1;
	cin>>t;

	while(t) {
		cin>>r>>c;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				cin>>cake[i][j];
			}
		}
		int pre = 0;
		int letter;
		
		int firstLine = 0;
		
		for(int i = 0; i < r; i++) {

			int count = 0;
			for(int j = 0; j < c; j++) {
				if(cake[i][j] != '?') {
					count++;
				}
			}
			if(count != 0) {
				firstLine = i;
				break;
			}
		}
		for(int i = 0; i < c; i++) {
			if(cake[firstLine][i] != '?') {
				letter = cake[firstLine][i];
				for(int j = pre;  j < i; j++)
					cake[firstLine][j] = letter;
				pre = i+1;
			}
		}
		if(cake[firstLine][c-1] == '?') {
			for(int i = pre; i < c; i++) 
				cake[firstLine][i] = letter;
		}
		if(firstLine != 0) {
			for(int i = firstLine-1; i >= 0; i--) {
				for(int j = 0; j < c; j++)
					cake[i][j] = cake[i+1][j];
			}
		}

		for(int i = 1; i < r; i++) {
			pre = 0;
			int count = 0;
			for(int j = 0; j < c; j++) {
				if(cake[i][j] != '?') 
					count++;
			}
			if(count == 0) {
				for(int j = 0; j < c; j++)
					cake[i][j] = cake[i-1][j];
			}
			else {
				for(int j = 0; j < c; j++) {
					if(cake[i][j] != '?') {
						letter = cake[i][j];
						for(int k = pre;  k < j; k++)
							cake[i][k] = letter;
						pre = j+1;
					}
				}
				if(cake[i][c-1] == '?') {
					for(int j = pre; j < c; j++) 
						cake[i][j] = letter;
		}
			}
		}
		cout<<"Case #"<<n<<":\n";
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++)
				cout<<cake[i][j];
			cout<<endl;
		}
		n++;
		t--;
	}
	return 0;
}