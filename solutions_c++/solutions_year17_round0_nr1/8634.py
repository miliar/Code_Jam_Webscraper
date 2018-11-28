#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;

int main()
{
    ofstream my_output;
    my_output.open("output.txt");
    ifstream my_input;
    my_input.open("A-large.in");
    unsigned int T;
    my_input >> T;
    unsigned int *K=new unsigned int [T];
    string *my_strings=new string [T];
    int *output = new int [T];
    for(unsigned int i=0;i<T;i++) {
        my_input >> my_strings[i] >> K[i];
    }
    for(unsigned int i=0;i<T;i++) {
        bool solved =0;
        unsigned int changes = 0;
        output[i]=0;
        for(unsigned int j=0;(j<my_strings[i].length())&&(solved==0);j++) {
            if((my_strings[i][j]=='-')&&(j<=(my_strings[i].length()-K[i]))) {
                for(unsigned int l=0;l<K[i];l++) {
                    if(my_strings[i][j+l]=='-') {
                        my_strings[i][j+l]='+';
                    } else {
                        my_strings[i][j+l]='-';
                    }
                }
                changes++;
            } else if((my_strings[i][j]=='-')) {
                output[i]= -1;
                        solved = 1;
            }
        }
        if(!solved) {
            output[i]=changes;
        }
    }

    for(unsigned int i=0;i<T;i++) {
        my_output << "Case #" << i+1 << ": ";
        if(output[i]==(-1)) {
            my_output << "IMPOSSIBLE";
        } else {
            my_output << output[i];
        }
        my_output << endl;
    }
    my_output.close();
    my_input.close();
    delete [] K;
    delete [] my_strings;
    delete [] output;


    return 0;
}
