#include <cstdio>
#include <string>
#include <iostream>
#include <sstream>

using namespace std ;

long long int cal(long long int num){

	string temp ;
	stringstream ss;
	ss << num ;
	temp = ss.str() ;
	//cout <<temp <<'\n' ;

	int max = 0;

	for (int i = 0; i < temp.length(); ++i)
	{
		if(temp[i]-48 < max) return 1 ;
		else max = temp[i]-48;
	}

	return 0 ;
}

int main(){

	int count ; scanf("%d",&count);

	int q = count ;

	while(count--){

		long long int num ; scanf("%lld",&num);

		while(cal(num))	num-- ;
		
		printf("Case #%d: %lld\n",q-count,num);
	}

}
