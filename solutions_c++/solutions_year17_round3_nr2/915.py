#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	int c=1;
	while (c<=t){
		cout << "Case #" << c++ << ": ";
		int a,b;
		cin >> a >> b;
		int arr[a+b][2];
		for (int i=0;i<a+b;i++){
			cin >> arr[i][0] >> arr[i][1];
		}
		if (a<=1 && b<=1){
			cout << "2\n";
		}
		else{
			if (arr[0][0]<arr[1][0]){
				int temp1 = arr[0][0];
				int temp2 = arr[0][1];
				arr[0][0] = arr[1][0];
				arr[0][1] = arr[1][1];
				arr[1][0] = temp1;
				arr[1][1] = temp2;
			}
			int a = (arr[1][1]-arr[0][0]);
			if (a<0)a+=1440;
			int b = (arr[0][1]-arr[1][0]);
			if (b<0)b+=1440;
			if (a<=720 || b<=720){
				cout << "2\n";
			}
			else{
				cout << "4\n";
			}
		}
	}
}