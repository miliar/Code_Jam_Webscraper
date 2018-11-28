//g++ largeTidy.cpp -o largeTidy && ./largeTidy < test.txt 
#include <iostream>

long long powerOfTen(int exp){
	long long result = 1LL;
	for(int i=0; i<exp; i++)
		result *= 10LL;
	return result;
}

void fillWithNines(long long &number, int digitsToFill){
	for(int i=0; i<digitsToFill; i++)
		number += 9LL*powerOfTen(i);
}

int main(int argc, char** argv){
	int T;
	long long N;
	int a,b,digitPos;
	
	std::cin >> T;
	for(int i=0; i<T; i++){
		std::cin >> N;
		long long TedyNumber = 0;
		for(long long j=N; j>0LL; j--){
			bool isTidy = true;
			long long temp = j;
			a = 9;
			digitPos = 0;
			while(temp > 0LL){
				b = temp%10LL;
				if (a-b < 0){
					isTidy = false;
					break;
				}
				temp /= 10LL;
				a=b;
				digitPos++;
			}
			if(isTidy){
				TedyNumber = j;
				break;
			}
			else {
				temp -= 1LL;
				temp *= powerOfTen(digitPos);
				fillWithNines(temp,digitPos);
				j = temp + 1LL;
			}
				
		}
		std::cout << "Case #" << i+1 << ": " << TedyNumber << std::endl;
	}
	
	return 0;
}
