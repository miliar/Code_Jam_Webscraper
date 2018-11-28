#include <string>
#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <queue>
#include <utility>
#include <functional>
using namespace std;
typedef unsigned long long myulong;
string process(myulong bath, myulong num){
   int i;
   myulong sum = 0;
   for(i = 0;;i++){
        sum+=1 << i;
        if(num <= sum)break;
   }
   myulong remain = num - (sum-(1<<i));
   i--;
   pair<myulong, myulong> even(0, 0), odd(0, 0);
   if(bath%2) {
     odd.first = bath;
     odd.second = 1;
   }  
   else{
    even.first = bath;
    even.second = 1;
   }
   while(i>=0){
    pair<myulong, myulong> tempe(0, 0), tempo(0, 0);
    if(odd.first!=0){
        if((odd.first/2)%2){
            tempo.first = odd.first/2;
            tempo.second += odd.second;
        }
        else{
            tempe.first = odd.first/2;
            tempe.second += odd.second;
        }
        if((odd.first - odd.first/2 - 1)%2){
            tempo.first = odd.first - odd.first/2 - 1;
            tempo.second+=odd.second;
        }
        else{
            tempe.first = odd.first - odd.first/2 - 1;
            tempe.second+=odd.second;
        }
    } 
    if(even.first != 0){
        if((even.first/2 - 1)%2){
            tempo.first = even.first/2 - 1;
            tempo.second += even.second;
        }
        else{
            tempe.first = even.first/2 - 1;
            tempe.second += even.second;
        }
        if((even.first - even.first/2)%2){
            tempo.first = even.first - even.first/2;
            tempo.second+=even.second;
        }
        else{
            tempe.first = even.first - even.first/2;
            tempe.second+=even.second;
        }
    }
    odd = tempo;
    even = tempe;
    i--;
   }
   if(even.first > odd.first){
       if(remain > even.second) bath = odd.first;
       else bath = even.first;
   }
   else{
    if(remain > odd.second) bath = even.first;
    else bath = odd.first;
   }
   return to_string(bath/2) + " " + to_string((bath-1)/2);
}

int main(){
    ifstream fread("input.in");
    ofstream fwrite("output.out");
    string raw_data;
    getline(fread, raw_data);
    stringstream ss(raw_data);
    int testcase;
    ss >> testcase;
    int count = 1;
    while(testcase){
        string data;
        getline(fread, data);
        stringstream ss(data);
        int bath, num;
        ss >> bath;
        ss >> num;
        fwrite << "Case #" << count << ": " << process(bath, num) << endl;
        testcase--;
        count++;
    }
    return 0;
}
