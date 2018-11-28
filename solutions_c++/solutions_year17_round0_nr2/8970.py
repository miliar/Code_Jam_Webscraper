#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;


void print_each_digit(unsigned long long int x)
{
    while(x >= 1) {
      	int digit = x % 10;
		std::cout << digit << '\n';
		x = x / 10;
	}
}
unsigned long long int n;
unsigned long long int temp;
int T = 0;
int i = 1;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    //unsigned long long int x = 423141;
    //print_each_digit(x);
	cin >> T;
	while(T--) {
		bool finished = false;
		cin >> n;
		int right;
		int left;
		//check each digit
		while(!finished) {
			finished = true;
			temp = n;
			right = temp % 10;
			temp = temp / 10;
			while(temp >= 1) {
				left = temp % 10;
				if(right < left) {
					finished = false;
					break;
				}
				right = left;
				temp = temp / 10;
			}
			if(finished) {
				cout << "Case #" << i << ": " << n << endl;
			} else n--;
		}
		i++;
	}
    return 0;
}





