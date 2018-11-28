//
//  codejam.cpp
//  codejam
//
//  Created by Zimu Wang on 4/8/17.
//
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

long long calculate(long long input, long long people){
    if (people == 1){
        return input - 1;
    }
    else{
        if (people%2 == 0){
            return calculate(input / 2, people / 2);
        }
        else{
            if (input % 2 == 0){
                return calculate(input/2 -1, people/2);
            }
            else{
                return calculate(input/2, people/2);
            }
        }
    }
}
int main(){
    ifstream fin ("C-large.in");
    ofstream fout ("C-large.out");
    int cases;
    fin >> cases;
    long long input, people;

    long long ans, min_d, max_d;
    for (int i=0;i<cases;i++){
        fin >> input >> people;
        ans = calculate(input, people);
        if (ans % 2 == 1){
            max_d = (ans+1)/2;
            min_d = (ans-1)/2;
        }
        else{
            max_d = ans / 2;
            min_d = ans/2;
        }
        fout << "Case #" << i+1 << ": " << max_d<< " " << min_d << endl;
    }
    fout.close();
}
