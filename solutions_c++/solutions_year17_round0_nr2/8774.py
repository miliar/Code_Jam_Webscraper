#include<iostream>
#include<iomanip>
#include<math.h>
using namespace std;

long long N,val;
bool det;

long  long a;
long  long ap=9;
long  long x=1;
long long v = 0;


bool findTidy(long long max_number);

int main(){

	//cout<<fmod(23.5,2.2);
	int T;
	cin>>T;
	//T Test cases
	for(int i=0;i<T;i++){

		cin>>N;

		for(long long j=N;j>0;j--){
			det = findTidy(j);
			if(det){
				val = j;
				break;
			}
			else{
				v = v-a*x/10;
				j = j-v;
			}
			}

		cout<<"Case #"<<i+1<<": "<<val<<endl;
	}
	return 0;
}

bool findTidy(long  long n){
	
	a=0;
	ap=9;
 	x=1;
	v = 0;

	while(n>0){
	//a = fmod(n,10);
	a = n%10;
	n = (n/10);
	x = x*10;
	v = v+ a*x/10;

	if(ap<a) return false;

	ap = a;
	}
	
	return true;
}