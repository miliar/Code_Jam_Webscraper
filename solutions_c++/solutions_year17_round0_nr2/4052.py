#include <iostream>
using namespace std;
typedef long long ll;

ll T, N;
bool done = false;

void make_smaller(ll base){
	if(N<base*10)return;
	//if(done)return;
	//cerr<<base<<endl;
	if((N/base)%10 < (N/(base*10))%10){
		N = (N/(base*10));
		N *= base*10;
		N -= 1;
		//done = true;
	}
	make_smaller(base*10);
}

int main(){
	cin>>T;
	for(int i=1; i<=T; i++){
		cin>>N;
		done = false;
		make_smaller(1);
		cout << "Case #" << i << ": " << N <<endl;
	}
}