#include <iostream>
#include <fstream>

using namespace std;

bool checkIfTidy(long long int num){
    long long int current, prev = 10;
    if(num <= 10){
        return true;
    }
    while(num > 0){
        current = num%10;
        num /= 10;
        if(current > prev){
            return false;
        }
        prev = current;
    }
    return true;
}

int main()
{
    ifstream inFile("C:\\Users\\Anjy-Joe Olatunbosun\\Downloads\\B-small-attempt2.in");
    //ifstream inFile("te.in");
    ofstream outFile("oroode.out");

    int testCases = 0, t = 0;
    inFile >> testCases;

    t = testCases;

    long long int num = 0;

    for(;testCases > 0;testCases--){
        inFile >> num;

        if(num < 10){
            outFile << "Case #" << t + 1 - testCases << ": " << num << "\n";
        }
        else{
            for(long long int i = num;i >= 10;i--){
                if(checkIfTidy(i)){
                    outFile << "Case #" << t + 1 - testCases << ": " << i << "\n";
                    break;
                }
            }
        }
    }

    inFile.close();
    outFile.close();

    return 0;
}
