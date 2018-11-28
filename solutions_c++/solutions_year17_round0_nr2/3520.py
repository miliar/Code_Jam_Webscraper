#include <iostream>
#include <fstream>
#include <deque>


using namespace std;

long get_tidy(long number){
    deque<int> vn;

    while (number > 0){
        vn.push_front(number%10);
        number/=10;
    }


    int alast = -1;
    for (int i = vn.size()-2; i >=0; --i){
        if (vn[i] > vn[i+1]){
            vn[i]--;
            alast = i;
        }
    }

    if (alast != -1){
        for (int i = alast+1; i < vn.size(); ++i){
            vn[i] = 9;
        }
    }

    long re = 0;

    for (int i = 0; i < vn.size(); ++i){
        re *= 10;
        re += vn[i];
    }

    return re;
}


int main(){

    ifstream infile("B-large.in");
    ofstream outfile("f2.out");

    int n;

    infile >> n;

    for (int acase = 0; acase < n; ++acase){
        long last_number;
        infile >> last_number;
        outfile << "Case #" << acase+1 << ": ";
        long result = get_tidy(last_number);
        outfile << result << endl;

    }
}