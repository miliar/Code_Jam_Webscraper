#include <bits/stdc++.h>

using namespace std;

int main(){
	int TC, NC = 1;
	string number;
	cin>>TC;
	while(TC--){
		cin>>number;
		char ant = '0';
		int temp = 0;
		int leftMostRight = 0;
		string ans;
		for(int i = 0 ; i<number.size() ;i++){
			if(ant<=number[i]){
				leftMostRight = i;
				ant = number[i];	
			}else	break;
		}

		if(leftMostRight == number.size()-1) {
			ans = number;
		}else{
			int findAnswer = 0;
			for(int i = leftMostRight ;i>0 ;i--){
				if(number[i-1]<number[i] ){
					number[i]--;
					for(int j = 0 ; j<=i ; j++){
						ans += number[j];	
					}
					for(int j = i+1;j<number.size() ;j++){
						ans += 	'9';
					}
					findAnswer = 1;
					break;	
				}	
			}
			
			if(findAnswer == 0){
				if(number[0] == '1'){

				}else{
					ans += number[0]-1;	
				}	
				for(int i = 1 ; i<number.size() ;i++){
					ans+='9';	
				}

			}

		}

		cout<<"Case #"<<NC++<<": "<<ans<<endl;
	}

	return 0;
}
