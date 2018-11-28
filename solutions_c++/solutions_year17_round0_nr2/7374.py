#include<iostream>
#include<string>
using namespace std;
/*
string to_arr(int x){
	string arr;
	if(x == 0){
		arr="0";
		return arr;
	}
	int i = 0;
	while(x>0){
		arr[i] = x % 10;
		i++;
		x/=10;
	}
	string rev;
	for(int j = i - 1; j >= 0; j--)
		rev[ i - 1 - j] = arr[j];
	return rev;
}
 

long long int to_int(string x){
	long long int X=0;
	unsigned int i=0;
//	cout<<x<<'\t'<<x.length()<<endl;
	while(i < x.length()){
		X = X*10 + (x[i] - 48);
		i++;
	}
	return X;
}

*/

string truncate(string x){
	long long int i=x.length(), j = 0;
	while(j<i && x[j]=='0')
		j++;
	return x.substr(j);
}

string tidy (string x){
	long long int len = x.length(), counter = 0;
	for(long long int i = 0; i < len - 1 ; i++){
	    if(x[i] > x[i + 1]){
			if(x[i - counter] == '0')
				x[i - counter] = '9';
			else
				x[i - counter] = x[i - counter] - 1;
			
			for(long long int j = i - counter + 1; j < len; j++)
				x[j] = '9';
			break;
		}
		else if(x[i] == x[i + 1])	counter++;
		else counter = 0;
//	cout<<x<<endl;
	}
	return x;
}

int main(){
	int n;
	cin>>n;
	for(int i = 0 ; i < n ; i++){
		string test_case;
		cin>>test_case;
		cout<<"Case #"<<(i+1)<<": "<<truncate(tidy( test_case ))<<endl;
	}
	return 0;
}