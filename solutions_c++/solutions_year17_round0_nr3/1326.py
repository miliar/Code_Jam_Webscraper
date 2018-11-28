#include <iostream>
using namespace std;
long long n,k;
long long solve(long long cur,long long odd_cnt, long long even_cnt, long long val){
    if(k>=cur && k<(cur*2LL)){
        // we lie at this level
        long long index = k-cur+1; //1 based
        if(val%2){
            //greater value is odd
            if(index<=odd_cnt) return val;
            else return val-1;
        }
        else{
            //greater value is even
            if(index<=even_cnt) return val;
            else return val-1;
        }
    }
    else{
        long long neven = 0;
        long long nodd = 0;
        long long odd = 0;
        if(val%2){
            odd = val;
        }
        else{
            odd = val-1;
        }
        if((odd/2)%2)   nodd=odd_cnt*2;
        else    neven=odd_cnt*2;
        nodd+=even_cnt;
        neven+=even_cnt;
        return solve(cur*2LL, nodd, neven, val/2LL);
    }
    return -1000;
}
int main() {
    int t;
	cin>>t;
	for(int T = 1; T<=t; T++){
	    cin>>n>>k;
	    long long num = solve(1LL,n%2?1LL:0LL,n%2?0LL:1LL,n);
	    if(num%2)
            cout<<"Case #"<<T<<": "<<num/2<<" "<<num/2<<"\n";
        else
            cout<<"Case #"<<T<<": "<<num/2<<" "<<(num-1)/2<<"\n";
	}
	return 0;
}