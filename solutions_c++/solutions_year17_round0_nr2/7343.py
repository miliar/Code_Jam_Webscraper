#include<iostream>
using namespace std;

bool is_tidy(long long number){
	long long tmp=number;
	int digit,prev_digit=10;
	bool r=false;
	do{
		digit = tmp%10;
		r = digit<=prev_digit;
		prev_digit = digit;
		tmp = (tmp - digit)/10;
	}while(r && tmp>0);
	return r;
}

int main(){
  long long t,T;
  long long number,ans;
  cin >> T;
  for(t=1;t<=T;++t){
		cin >> number;
		ans=number;
		while(!is_tidy(ans))ans--;	
		cout << "Case #"<<t<<": "<<ans<<endl;
	}
	return 1;
}

