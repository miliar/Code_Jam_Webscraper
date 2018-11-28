#include <iostream>
#include <fstream>
#include <algorithm>
#define N 1000000
using namespace std;

int findMax(int n, int a[]){
    int max=0, index;
    for (int i=0; i<n; i++)
        if (a[i]>max){
            max = a[i];
            index = i;
        }
    return index;
}

bool comp(int x, int y){
    return x>y;
}

int main(){
    int a[N+1];
	ofstream myfile;
  	myfile.open ("out3.txt");
  	int n,m,t,l1,l2,ind,k;
  	cin >> n;
  	for (int ri=0; ri<n; ri++){
  		cin >> m >> k;

        for (int i=0; i<=N; i++)
            a[i] = 0;
        a[0] = m;
        
        int power = 1;
        while (k>=power){
            sort(a,a+power,comp);
            for (int i=power-1; i>=0; i--)
                if ((a[i]-1)%2==0){
                    a[i*2+1] = (a[i]-1)/2;
                    a[i*2] = (a[i]-1)/2;
                }
                else {
                    a[i*2+1] = (a[i]-1)/2;
                    a[i*2] = (a[i]-1)/2+1;
                }
            k -= power;
            power *= 2;
        }

        cout << k <<endl;
        if (k==0){
            l1 = a[power-1];
            l2 = a[power-2];
        }
        else{
            sort(a,a+power,comp);
            t = a[k-1];
            if ((t-1)%2==0)
                l1 = l2 = (t-1)/2;
            else {
                l2 = (t-1)/2+1;
                l1 = (t-1)/2;
            }
            if (t==0)
                l1 = l2 = 0;
        }

        /*for (int i=0; i<power; i++)
            cout << a[i] << "　";*/

        //cout << "Case #" << ri+1 << ": " << l2 << " " << l1 << endl;
  		myfile << "Case #" << ri+1 << ": " << l2 << " " << l1 << endl;
  	}
  	myfile.close();
  	return 0;
}