#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int inputs;
    ofstream output;
    output.open("output.txt");
    ifstream input;
    input.open("data.txt");
    input >> inputs;
    for(int z = 0; z < inputs; z++)
    {
    int i = 0, numb, num, digits[5];
    input >> numb;
    while(1) {
        if(numb / 10 == 0) break;
        i = 0;
        num = numb;
        while(num != 0) {
            digits[i++] = num % 10;
            num = num / 10;
        }
        --i;
        while(i != 0) {
            if(digits[i] > digits[--i]) break;
        }
        if(i == 0) {
            if(digits[1] <= digits[0]) break;
            else --numb;
        }
        else --numb;
    }
    output << "Case #" << z+1 << ": " << numb << endl;
    }
    return 0;
}
