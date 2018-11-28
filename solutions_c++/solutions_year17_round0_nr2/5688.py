#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>

using namespace std;

int main(){
	int i,j,k,l;
	string str;
	int K, T;
	int *a;
	cin>>T;

	for(l = 0 ; l < T ; l++)
	{
		cout<<"Case #"<<l+1<<": ";
		cin>>str;
		a = new int[str.length()];
		int N = str.length();
		for(i = 1 ; i < N ; i++){
			if(str[i] < str[i - 1])
				break;
		}
		if(i == N){
			cout<<str<<"\n";
			continue;
		}
		for(j = i ; j < N ; j++)
			str[j] = '9';
		i--;
		str[i] = str[i] - 1;
		while(i > 0 && str[i] < str[i - 1]){
			str[i] = '9';
			i--;
			str[i] = str[i] - 1;
		}
		i = 0;
		while(str[i] == '0')
			i++;
		for( ; i < N ; i++)
			cout<<str[i];
		cout<<"\n";
	}
	return 0;
}
