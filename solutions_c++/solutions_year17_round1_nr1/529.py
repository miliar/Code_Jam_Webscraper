#include <iostream>
#include <stdio.h>

using namespace std;

#define AmanJain jainaman224

void scanlonglong(long long &x){
    register long long c=getchar_unlocked();
    x=0;
    for(;(c<48 || c>57);
    	c=getchar_unlocked());
    for(;c>47 && c<58;c=getchar_unlocked()){
        x=(x<<1)+(x<<3)+c-48;
    }
}

void scanlong(long &y){
    register long d=getchar_unlocked();
    y=0;
    for(;(d<48 || d>57);
    	d=getchar_unlocked());
    for(;d>47 && d<58;d=getchar_unlocked()){
        y=(y<<1)+(y<<3)+d-48;
    }
}

int main(){
	int t, r, c, i, j, k;
	char a[25][25];
	cin >> t;
	for(k=1;k<=t;k++){
		cin >> r >> c;
		for(i=0;i<r;i++)
			for(j=0;j<c;j++)
				cin >> a[i][j];

		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				if(a[i][j]=='?'){
					if(j>0 && a[i][j-1]!='?')
						a[i][j] = a[i][j-1];
					else if(j<c-1 && a[i][j+1]!='?')
						a[i][j] = a[i][j+1];
				}
			}
			for(j=c-1;j>=0;j--){
				if(a[i][j]=='?'){
					if(j>0 && a[i][j-1]!='?')
						a[i][j] = a[i][j-1];
					else if(j<c-1 && a[i][j+1]!='?')
						a[i][j] = a[i][j+1];
				}
			}
		}

		for(j=0;j<c;j++){
			for(i=0;i<r;i++){
				if(a[i][j]=='?'){
					if(i>0 && a[i-1][j]!='?')
						a[i][j] = a[i-1][j];
					else if(i<r-1 && a[i+1][j]!='?')
						a[i][j] = a[i+1][j];
				}
			}
			for(i=r-1;i>=0;i--){
				if(a[i][j]=='?'){
					if(i>0 && a[i-1][j]!='?')
						a[i][j] = a[i-1][j];
					else if(i<r-1 && a[i+1][j]!='?')
						a[i][j] = a[i+1][j];
				}
			}
		}

		cout << "CASE #" << k << ":" << endl; 

		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				cout << a[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}