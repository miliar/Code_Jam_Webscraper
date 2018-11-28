#include <bits/stdc++.h>
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

int main(){
	cin >> N;
	
	for (_case = 1; _case <= N; _case++){
		cin >> num;
		
		while (!isTidy(num))
			num--;
		
		cout << "case #"<<_case<<": "<<num << "\n";
	}
	
	
	return 0;
}

