#include <bits/stdc++.h>
using namespace std;
int main(){
	long long int t;
	cin >> t; 
	for(long long int h=1;h<=t;h++){
		
		long long int done=1,dig[10002]={0},final[10002]={0};
		string s;
		long long int flag=0,i=0,size=0,n,temp;cin >> n;temp = n;
		while(temp > 0){
			dig[i] = temp%10;
			final[i] = dig[i];
			temp /= 10;i++;
		}size = i;
		for(int i=0;i<size-1;i++){
			if(dig[i] < dig[i+1]) done = 0;
		}
		while(done == 0){
			done = 1;
			flag = 0;
			for(long long int i=size-1;i>-1;i--){
				if(flag == 1){
					final[i] = 9;
					continue;
				}
				if(dig[i] > dig[i-1] && flag == 0){
					final[i] = dig[i]-1;
					flag = 1;
				}	
				else{
					final[i] = dig[i];
				}
			}
			for(int i=0;i<size;i++){
				dig[i] = final[i];
				// cout << dig[i];
			}
			// cout << endl;
			for(int i=0;i<size-1;i++){
				if(dig[i] < dig[i+1]) done = 0;
			}
		}
		flag = 0;
		cout << "Case #" << h << ": ";
		if(n < 10) cout << n;
		else{
			for(int i=size-1;i>-1;i--){
				if(final[i] != 0){
					cout << final[i];
					flag = 1;
				}
				if(final[i] == 0){
					if(flag) cout << 0;
				}
			}
		}
		cout << endl;
	}
	return 0;
}