#include <bits/stdc++.h>



using namespace std;

typedef unsigned long long LL;

LL res(LL num){


	int y=0;


	while(!y || num>0){
		
		stringstream ss;
		ss << num;
		string str = ss.str();
		int k = 1;
		for(int i = 1; i < str.size(); ++i){
			if((str[i]-'0') < (str[i-1]-'0')){
				k=0;
				break;
			}
		}
		if(k==1)
			return num;
		--num;
	}
}



int main(){

	int n;
	cin >> n;
	


	for(int i = 1; i <= n; ++i){
	
	
		LL num; cin >> num;
	

		cout << "Case #" << i << ": " << res(num) << endl;		
	}
}
