#include <iostream>
#include <fstream>
using namespace std;
ifstream fin ("B-large.in");
ofstream fout ("output.txt");
string n;
long long queries;
int main() {
    fin >> queries;
    for (long long  i= 1; i <= queries; i++){
        fin >> n;
        for(long long x = 0; x < n.size()-1; x++){
            if(n[x+1]<n[x]){
                n[x]=(n[x]-'0')-1+'0';
                for(long long k = x+1; k < n.size(); k++){
                    n[k]='9';
                }
                x=-1;
            }
        }
        bool check = false;
        fout << "Case #" << i << ": ";
        for(long long x = 0; x < n.size(); x++){
            if(n[x]!='0'){
                check = true;
            }
            if(check==true){
                fout << n[x];
            }
        }
        fout << endl;
        if(check==false) fout << '0' << endl;
    }
}
