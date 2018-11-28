#include<iostream>
#include<string>

long long base10(int exp){
	long long ten = 1;
	int count = 0;
	while(count < exp){
		ten = ten * 10;
		count++;
	}
	return ten;
}
long long manualConvert(std::string value){
	long long hey = 0;
	unsigned int count = 0;
	
	while(count < value.length()){
		hey += (static_cast<int>(value[count]) - 48) * base10(value.length() - count - 1);
		
		count++;
	}
	return hey;
}
int goodNumber(long long tidy){
	bool done = true;
	int exp = 0;
	while(done){
		long long comp1 = tidy % 10;
		tidy = tidy / 10;
		long long comp2 = tidy % 10;
		if(comp2 > comp1){
			return false;
		}
		if(tidy == 0){
			done = false;
			return true;
		}
	}
	return true;
}
int main(){
	int number;
	std::cin>>number;
	
	long long * cases = new long long[number];
	
	//111111111111111110
	int caseNumb = 0;
	long long tests;
	std::string test;
	while(caseNumb < number){
		std::cin>>test;
		tests = manualConvert(test);
		
		
		bool tidy = goodNumber(tests);
		
		while(!tidy){
			tests -= 1;
			tidy = goodNumber(tests);
		}
		
		cases[caseNumb] = tests;
		
		caseNumb++;
	}
	
	int count = 0;
	while(count < number){
		std::cout<<"CASE #"<<count + 1<<": ";
		std::cout<<cases[count]<<std::endl;
		count++;
	}
	
}

