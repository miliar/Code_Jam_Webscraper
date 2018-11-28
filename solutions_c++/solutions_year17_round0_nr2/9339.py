#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define ll long long int

vector<int> s2d( ll value ){
    vector<int> digits;
    for( ; value > 0 ; value /= 10 ) digits.push_back( value%10 ) ;
    return digits ;
}

int main(){
	int T,i=0;
	cin>>T;
	while(i != T){
		ll N,num,x=0,j;
		cin>>N;
		num = N;
		vector<int>:: iterator it,it1;
		if(N%10 == 0) num=N-1;
		vector<int> mynum = s2d(num);
		a:reverse(mynum.begin(),mynum.end());
		if(!is_sorted(mynum.begin(),mynum.end())){
			for(j=0;j<mynum.size();j++){
				if(mynum[j] > mynum[j+1]) break;				
			}
			x = mynum[j+1];
			for(ll k=j+2;k<mynum.size();k++){
				x *= 10;
				x += mynum[k];
			}
			x++;
			num = num-x;
			mynum = s2d(num);
			goto a;
		}else{
			cout<<"Case #"<<(i+1)<<": "<<num<<endl;			
		}
		i++;
	}
}