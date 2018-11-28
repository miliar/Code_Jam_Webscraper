# include <iostream>
# include <string.h>
using namespace std;

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	string n ;
	for (int j = 1; j <= t; j++){
	
		cin>>n;
		int l =n.size();
		//cout<<l;
		for (int i = l-1; i > 0; i--){
			if (n[i] < n[i-1]){
				for (int q = i; q < l; q++){
					n[q] = '9';
				}
				
				char a = n[i-1];
			//	cout<<a<<" ";
				int new_digit = int(a);
				new_digit = new_digit - 1;
			//	cout<<new_digit<<" ";
				n[i-1] = new_digit;
			//	cout<<n[i-1]<<endl;
			}
		}
		cout<<"Case #"<<j<<": ";
		for(int i = 0; i<l; i++){
			if(n[i] != '0'){
				cout<<n[i];
			}
		}
		cout<<endl;
	}
	return 0;
}
