#include <iostream>
#include <string>

using namespace std;

typedef unsigned long long llu;

llu max(llu a, llu b){
	return a>b?a:b;
}

llu pow_10(int n){
	llu ans=1;
	while(n--) ans*=10;
	return ans;
}

llu func(llu n){
	string num = to_string(n);
	int index=0;
	for(int i=num.size()-2;i>=0;i--){
		if(num[i]=='0'){
			index=i;
			break;
		}
		if(num[i]>num[i+1]) num[i]=num[i+1];
	}
	return stoull(num.substr(index));
}


int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		llu N; cin>>N;
		llu max_ans = func(N);
		for(int i=1;i<=18;i++){
			llu tens = pow_10(i);
			if(tens>=N) break;
			llu val= N - (N % tens);
			val--;
			max_ans = max(max_ans, func(val));
		}
		cout<<"Case #"<<t<<": "<<max_ans<<endl;

	}
	return 0;
}