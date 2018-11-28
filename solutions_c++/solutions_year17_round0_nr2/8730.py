#include <iostream>
#include <tgmath.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream my_input;
    my_input.open("B-small-attempt0.in");
    ofstream my_output;
    my_output.open("output.txt");
    unsigned int T;
    my_input >> T;
    unsigned long long int *numbers = new unsigned long long int [T];
    for(unsigned int i=0;i<T;i++) {
        my_input >> numbers[i];
    }
    for(unsigned int i=0;i<T;i++) {
        for(unsigned int j=1;j<18;) {
            if((numbers[i]%(unsigned long long int)pow(10,j+1))/(unsigned long long int)pow(10,j)>
                    (numbers[i]%(unsigned long long int)pow(10,j))/(unsigned long long int)pow(10, j-1)) {
                numbers[i]-=numbers[i]%(unsigned long long int)pow(10,j)+1;
            } else {
                j++;
            }
        }
    }
    for(unsigned int i=0;i<T;i++) {
        my_output << "Case #" << i+1 << ": " << numbers[i] << endl;
    }

    my_output.close();
    my_input.close();
    delete [] numbers;
    return 0;
}
