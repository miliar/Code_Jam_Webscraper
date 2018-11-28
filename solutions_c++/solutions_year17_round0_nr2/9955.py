#include<iostream>
#include <fstream>

using namespace std;
unsigned int t;
unsigned long long n;

unsigned long long Resolver(unsigned long long n);
bool EsTidy(unsigned long long k);

int main(){
    ifstream input ("B-large.in");
    ofstream output ("output.txt");
    input >> t;
    for(unsigned long long i = 1; i <= t; i++){
        input >> n;
        output << "Case #" << i << ": " << Resolver(n) << endl;
    }
    return 0;

}

unsigned long long Resolver(unsigned long long n){
    while(n > 9){
        unsigned long long k = n;
        unsigned long long div = 10;
        unsigned int ult = k%10;
        bool jump = false;
        k = n/div;
        unsigned int ault = k%10;

        while(k > 0){
            if(ult < ault){
                jump = true;
                break;
            }
            ult = ault;
            div*=10;
            k = n / div;
            ault = k%10;
        }
        if(jump){
            n -= ((n%div) + 1);
        }else{
            return n;
        }
    }
    return n;
}
