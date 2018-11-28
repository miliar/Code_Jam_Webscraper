#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

void swap (int*a,int*b) {
    int temp;
    temp =*a;
    *a =*b;
    *b =temp;
}

void bubble_sort(int *a, int n) { // bubble_sort(a, n); // a is array name, n is elements count
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) // descending: > // ascending: <
                swap(&a[j], &a[j + 1]);
        }
    }
}

int main () {
	int t;
	cin >> t;
	for (int i=0 ; i<t ; i++) {
		cout << "Case #" << i+1 << ": ";
		int n;
		cin >> n;
		for (int k=n ; k>0 ; k--) {
			int Temp = k;
			//cout << endl << k << endl;
			int dgts;
			for (dgts=0 ; Temp>0 ; Temp=Temp/10, dgts++) // counting digits
				;
			//cout << "dgts " << dgts << endl;
			Temp = k;
			int narr[dgts];
			for (int j = dgts - 1 ; j >= 0 ; j--) { // emptying digits into array
			    int temp = Temp % 10;
			    narr[j] = temp;
			    Temp = Temp / 10;
			}
			for (int g=0 ; g<dgts ; g++)
				//cout << "narr" << g << " " << narr[g] << endl;
			//cout << endl;
			bubble_sort(narr,dgts);
			for (int g=0 ; g<dgts ; g++)
				//cout << "bnarr" << g << " " << narr[g] << endl;
			//cout << endl;
			Temp = k;
			int newnum=0;
			for (int l=0 ; l<dgts ; l++) { // turning array into number
			    newnum=newnum*10+narr[l];
			}
			//cout << "newnum " << newnum << endl;
			if (newnum == Temp) {
				//cout << "in" << endl;
				cout << k;
				break;
			}
			//cout << "----------------------------------------------------------";
		}
		cout << endl;
	}
	return 0;
}