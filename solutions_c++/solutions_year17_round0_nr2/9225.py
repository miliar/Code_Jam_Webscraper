#include <iostream>
using namespace std;

int outPut(int n){
    int n1;
    int n2;
    int digit;
    for(int j=n; j>=1; j--){
        int flag=0;
        n1=j;
        n2=j;
        do{
            digit=n2%10;
            n2=n2/10;
            if(digit<n2%10){
                flag=2;
                break;
            }
        }
        while(n2/10>0);
        if(flag==2){continue;}
        else{
            return n1;
            break;
        }
    }
}
int main() {
	int t;
	int n;
	cin >> t;
	for(int i=1; i<=t; i++){
	    cin >> n;
	    cout << "Case #" << i << ": " << outPut(n) << "\n";
	}
	return 0;
}