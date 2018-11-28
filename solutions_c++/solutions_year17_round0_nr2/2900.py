#include <iostream>
using namespace std;

long mult_10(int lvl, long ans){
    if (lvl==0) return ans;
    else return mult_10(lvl - 1, ans*10);
}
long consecutive_untidy_filter(long num, long rem, int level, int minsofar){
	//finds the last untidy number counted
	long r = rem%10;
	long q = rem/10;
	if (q==0 && r==0)
		return num;
	else if (r<=minsofar){
		return consecutive_untidy_filter(num, q, level+1, r);
	}
	else{
		long c = rem*(mult_10(level, 1)) -1;
		return consecutive_untidy_filter(c,c,0,10 );
	}
}

int main(){
	int t;
	cin>>t;
	long n;
	for(int i=0; i<t;i++){
	
        cin>>n;
		cout<<"Case #"<<i+1<<": "<<consecutive_untidy_filter(n,n,0,10) <<endl;
	}
}
