#include <string>
#include <fstream>
#include <iostream>

std::ifstream cin("large_input.txt");
std::ofstream cout("large_output.txt");

using std::string;

int isPossible(string &row, int k){
    int be=-1;
    int en=-1;
    int flip=0;
    for(int i=0;i<row.size();++i){
        if(row[i]=='-'){
                if(be==-1 && en ==-1){
                    be = i; en = i+k-1;
                    row[i]='+';
                    ++flip;
                }else{
                    if(be<=i && i<=en){
                        row[i]='-';
                    }else{
                        if(be>i){
                            for(int e=be;e<=en;++e){
                                row[e]=((row[e]=='-')?'+':'-');
                            }
                        }
                        be = i; en = i+k-1;
                        row[i]='+';
                        ++flip;
                    }
                }
        }else{
            if(be<=i && i<=en){
                be =en+1;
                en = i+k-1;
                ++flip;
            }
        }
    }
    if(en<(int)row.size() && be<(int)row.size()) return flip;
    return -1;
}


int main() {
    int T;
    string row;
    int k;
    int flip;

    cin >> T;

    for(int e=1;e<=T;++e){
        cin >> row >> k;
        flip = isPossible(row,k);
        if(flip==-1) cout <<"Case #"<<e<< ": IMPOSSIBLE\n";
        else cout <<"Case #"<<e<<": "<< flip << "\n";
    }

    return 0;
}



