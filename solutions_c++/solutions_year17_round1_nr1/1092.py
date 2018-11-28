#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool empty(char a[30][30], int n, int c){
    for (int i=0; i<c; i++)
        if (a[n][i]!='?') return false;
    return true;
}

int main(){
	ofstream myfile;
  	myfile.open ("out1.txt");
    char a[30][30];
    int rn, r, c, i, j, flagi;
  	cin >> rn;
  	for (int ri=0; ri<rn; ri++){
  		cin >> r >> c;
        for (int i=0; i<r; i++)
        for (int j=0; j<c; j++)
            cin >> a[i][j];

        flagi = 1;
        for (int i=0; i<r; i++){
            if ((empty(a,i,c))&&(flagi))
                continue;
            if ((empty(a,i,c))&&(!flagi))
                for (int k=0; k<c; k++)
                    a[i][k] = a[i-1][k];
            j = 0;
            while (a[i][j]=='?')
                j++;
            for (int k=0; k<j; k++)
                a[i][k] = a[i][j];
            for (int k=j+1; k<c; k++)
                if (a[i][k]=='?') a[i][k] = a[i][k-1];

            if (flagi){
                for (int k=0; k<i; k++)
                for (int j=0; j<c; j++)
                    a[k][j] = a[i][j];
                flagi = 0;
            }

        }

        myfile << "Case #" << ri+1 << ":" << endl;
        for (int i=0; i<r; i++){
            for (int j=0; j<c; j++)
                myfile << a[i][j];
            myfile << endl;
        }
  	}
  	myfile.close();
  	return 0;
}