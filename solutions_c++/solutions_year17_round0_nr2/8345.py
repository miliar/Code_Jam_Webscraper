#include <algorithm>
#include <iostream>


using namespace std;

typedef unsigned long long int ullint;

ullint N;
ullint _case;
ullint num;


bool isTidy(ullint n){
	ullint prev, act;
	act = n%10;
	n/=10;
	while(n){
		prev = act;
		act = n%10;
		n/=10;
		if(prev<act)
			return false;
	}
	return true;
}

ullint semplify(ullint n){
	int i, j;
	char v[20] = {0};
	
	for (i = 0; n ; i++){
		v[i]= (n%10)+'0';
		n/=10;
	}
	int cifre = i;
	
	for (i = 0, j = cifre-1; i < j ; i++, j--){
		char tmp = v[i];
		v[i] = v[j];
		v[j] = tmp;
	}
	
	for (i = 1; i < cifre && v[i-1]<=v[i]; i++);
	
	if(i<cifre){
		i--;
		while(v[i]==v[--i]);
		
		for(i+=2;i<cifre; i++){
			v[i] = '0';
		}
	}
	return atoll(v);
}

int main(){
	cin >> N;
	
	for (_case = 1; _case <= N; _case++){
		cin >> num;
		num = semplify(num);
		while(!isTidy(num)){
			num--;
		}
		
		cout << "case #"<<_case<<": "<<num<< "\n";
	}
	
	
	return 0;
}

