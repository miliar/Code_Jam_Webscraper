#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

bool isTidy(unsigned long long n)
{
    stringstream ss;
    ss << n;
    string num = ss.str();
    if(num[0] == '0'){
        return false;
    }
    else if(num.size() == 1){
        return true;
    }
    else{
        char last = num[0];
        for(int i = 1; i < num.size(); i++){
            int current = num[i] - '0';
            int l = last - '0';
            if(current >= l){
                last = num[i];
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
}

int main()
{
    ifstream fin("small.in");
    ofstream fout("small.out");
    int t;
    fin >> t;

    for(int i = 0; i < t; i++)
    {
        unsigned long long n;
        fin >> n;
        unsigned long long j = n;
        while(j != 0){
            if(isTidy(j)){
                break;
            }
            j--;
        }
        fout << "Case #" << i + 1 << ": " << j << "\n";
    }

    return 0;
}
