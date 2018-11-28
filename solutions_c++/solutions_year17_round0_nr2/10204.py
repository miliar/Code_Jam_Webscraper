
#include <iostream>
using namespace std;

int main() {
	int k, num1 , num2 , v , a , b , d ;
	cin >> k;
	int r[k];
	for(int i=0;i<k;i++){
		cin >> num1;
		v=1;
		while(v==1){
			num2=num1;
			d=1;
			while(d==1 & num2!=0 ){
				a=num2%10;
				b=(num2%100)/10;
				if(a<b){
					d=0;
				}

				num2=num2/10;
			}
			if (d==0){
				num1=num1-1;
			}
			else {
				v=0;
			}
		}
		r[i]=num1;
	}
	for (int i=0;i<k;i++){
		cout << "Case #" << i+1 << ": " << r[i] << endl;
	}
	return 0;
}
