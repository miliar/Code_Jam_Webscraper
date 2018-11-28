#include <iostream>

using namespace std;

int tidy(unsigned long long i){
	unsigned long long bb = 1000000000000000000;
	unsigned int d=0;
	
	int c =0;

//  cout <<i<<endl;
	while (bb >0){
	//	cout <<i<<" "<<bb<<" "<< d<<endl;
		if (d > i/bb){return 0;}
		d= i/bb;
		i = i %bb;
		bb= bb/10;
		c++;
	}

	return 1;
}

unsigned long long solve(unsigned long long s){
	unsigned long long bb = 10;
	int onemore =1;
	while (onemore){
		if (s/bb ==0){onemore=0;}
		if (!tidy(s%bb)){
	//		cout << (s/(bb))*(bb)  << " "<< (((s%(bb))/(bb/10)) -1)*(bb/10)  << " "<< ((bb/10) -1)<<endl;
			s = (s/(bb))*(bb) + (((s%(bb))/(bb/10)) -1)*(bb/10) + ((bb/10) -1);
		}else{bb=bb*10;}
//		cout<< bb<<'\t' << s <<endl;
	}
		
		


	return s;
}



int main (){
	int	test;
	unsigned long long cur;
	cin >> test;
	
	for (int i =1;i<=test;i++){
		cin >>cur;

		cur =solve(cur);
		if (cur <0){
		cout << "Case #"<<i<<":"<< " "<<"IMPOSSIBLE"<<endl;
		}else{
		cout << "Case #"<<i<<":"<< " "<<cur<<endl;
		
		}
	};

}
