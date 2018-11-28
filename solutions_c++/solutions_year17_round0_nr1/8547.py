#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool checkPos(int a[], int n, int m){
    for (int i=n-m-1; i<n; i++)
        if (a[i]==0) return false;
    return true;
}

int main(){
	ofstream myfile;
  	myfile.open ("out1.txt");
  	int rn,n,m,count;
    int a[1001];
    string s;
  	cin >> rn;
  	for (int ri=0; ri<rn; ri++){
  		cin >> s >> m;
  		n = s.length();
        for (int i=0; i<n; i++)
            if (s[i]=='+') a[i] = 1;
            else a[i] = 0;

        count = 0;
        for (int i=0; i<n-m+1; i++)
        if (a[i]==0){
            for (int j=i; j<i+m; j++)
                a[j] = !a[j];
            count++;
            /*for (int j=0; j<n; j++){
                cout << a[j] << " ";
            }
            cout << endl;*/

        }

        if (checkPos(a,n,m))
  		    myfile << "Case #" << ri+1 << ": " << count << endl;
        else
            myfile << "Case #" << ri+1 << ": IMPOSSIBLE" << endl;
  	}
  	myfile.close();
  	return 0;
}