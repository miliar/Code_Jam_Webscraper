#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

#define INF 2000000000;

using namespace std;
typedef long long ll;


int main(){
    ifstream infile("in.txt");
    ofstream outfile("out.txt");
    int t; infile>>t;
    for (int h=0; h<t; h++){
        outfile<<"Case #"<<h+1<<": ";
        string s; infile>>s;
        int k; infile>>k;
        int it=0;
        bool valid=true;
        int flips=0;
        while (true){
            if (it==s.size()){
                break;
            }
            if (s[it]=='-'){
                if (it+k>s.size()){
                    valid=false;
                    break;
                }
                flips++;
                for (int j=it; j<it+k; j++){
                    if (s[j]=='-'){
                        s[j]='+';
                    }
                    else {
                        s[j]='-';
                    }
                }
            }
            it++;
        }
        if (valid){
            outfile<<flips<<endl;
        }
        else {
            outfile<<"IMPOSSIBLE"<<endl;
        }
    }
}
