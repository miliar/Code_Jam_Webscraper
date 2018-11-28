#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>


using namespace std;

unsigned long count(unsigned long num) {
    int counter = 0;
    do {
        counter++;
        num = num / 10;
    }while (num != 0);
    return counter;
}



bool check(unsigned long x) {
    unsigned long x_size = count(x);
    unsigned long temp = x % 10;
    unsigned long next = 0;
    
    for(int i = 0; i < (x_size - 1); i++) {
        x = x / 10;
        next = x % 10;
        if(temp < next) {
            return false;
        }
        temp = next;
    }
    
    
    return true;
}



unsigned long tidy(unsigned long x) {
    while(!check(x)) {
        x--;
    }
    return x;
}


int main(){
    string input;
    unsigned long NumTests = 0;
    unsigned long unknownNum = 0;
    unsigned long tidynum = 0;
    string testcase;

 
 	getline(cin,input);
	
	NumTests = atoi( input.c_str() );
	
	
	
	for(int i = 1; i <= NumTests; i++) {
		getline(cin, testcase);
			
			unknownNum = atoi( testcase.c_str() );
				
			
		tidynum = tidy(unknownNum);
		cout << "Case #" << i << ": " << tidynum << endl;
			
	}
	
 return 0;   
}