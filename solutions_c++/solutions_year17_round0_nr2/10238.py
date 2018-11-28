#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std; 

bool isTidy(unsigned input){
    if(input<10)
        return true;
    int lastDigit = 9;
    while(input>0){
        int currentLastDigit = input%10;
        if(currentLastDigit>lastDigit)
            return false;
        lastDigit = currentLastDigit;
        input /= 10;
    }
    return true;
}

unsigned findFirstTidy(unsigned input){
    while(!isTidy(input))
        --input;
    return input;
}

int main()
{
    unsigned tests;
    cin>>tests;
    int k = 1;
    while(k!=tests+1){
        unsigned input;
        cin>>input;
        cout<<"Case #"<<k++<<": "<<findFirstTidy(input)<<endl;
    }

    return 0;
}