#include <string>
#include <fstream>
#include <iostream>

std::ifstream cin("large_input.txt");
std::ofstream cout("large_output.txt");

using std::string;

string getTidyNumber(string N){

    if(N.size()==1) return N;
    int limit=N.size();


    for(int i=N.size()-1;i>0;--i){
        if(N[i]<N[i-1]){
            --N[(limit=i)-1];
        }
    }

    for(int i=limit;i<N.size();++i) N[i]='9';

    limit=0;
    while(N[limit++]=='0');

    N=N.substr(limit-1);

    return N;
}


int main() {
    int T;
    string N;
    cin >> T;

    for(int e=1;e<=T;++e){
        cin >> N;
        cout <<"Case #"<<e<<": "<<getTidyNumber(N)<< "\n";
    }

    return 0;
}




