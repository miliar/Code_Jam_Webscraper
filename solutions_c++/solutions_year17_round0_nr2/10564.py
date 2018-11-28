#define JUDGE 1
#ifdef JUDGE
#include<fstream>
std::ifstream cin("input.in");
std::ofstream cout("output.in");
#else
#include<iostream>

using namespace std;
#endif
int len;
inline int LEN(unsigned long long N){ int count=0;while(N!=0){ N/=10 ;count++;} return count;}

inline int check(unsigned long long N){
	int count=0;
	unsigned long long temp,rem;
	do{
		rem=N%10;
		N=N/10;

		count++;
		if(N==0){
			return count;
		}
	}while(rem>=N%10);
	
	return 0;
}

    unsigned long long int N;
int main(){

    int i,T,len;
	cin>>T;
	for(i=1;i<=T;i++){
		cin>>N;
		
		while(N>=1){
			len=LEN(N);
             if(check(N)==len){
             	cout<<"Case #"<<i<<": "<<N<<std::endl;
             	break;
             }
			N--;
		}
	}
	
}
