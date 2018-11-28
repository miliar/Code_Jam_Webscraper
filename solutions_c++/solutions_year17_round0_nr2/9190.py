#include<bits/stdc++.h>
#include<conio.h>
using namespace std;

// x^y
long long power(long long x, long long y){
	long long j = 1;
	for(long long i=0; i<y; i++)
		j*=x;
	return j;
}

long long length(long long num){
	long long index = 1;
	while(num/power(10,index) != 0)
		index++;
	
	return index;
}

long long nines(long long len){
	long long res = 0;

	for(long long i=0; i<len; i++){
		res = res*10 + 9;
	}
	return res;
}

int main(){
	int t;
	scanf("%d", &t);
	for(int ii = 0; ii<t; ii++){
		long long n = 0;
		scanf("%lld", &n);
	
		long long num = n;
		long long len = length(num);
		long long index = len-1;
	
		while(true){
			//break condition
			if(index == 0)
				break;
			
			long long l = power(10, index-1);
			long long m = power(10, index);
			long long h = power(10, index+1);
			
			if((num%h)/m <= (num%m)/l){
				index--;
			}
			else{
				num /= m;
				num *= m;
				num += nines(index);
				num -= m;
				index = len-1;
				//cout<<"m="<<m<<endl;
				//cout<<"num:"<<num;
			}
			//cout<<"check out"<<index<<endl;
			//getch();
		}
		cout<<"Case #"<<(ii+1)<<": "<<num<<endl;
	
	}
	return 0;
}
