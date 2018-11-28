#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("a1.in");
ofstream fout("a1.out");

int main(){
    int t;
    fin>>t;
    for(int l=0;l<t;l++){
        string x;
        fin>>x;
        int n;
        fin>>n;
        int flip=0;
        while(x[0]=='+'){
            x.erase(0,1);
        }
        while(x.length()>=n){
            flip++;
            for(int i=0;i<n;i++){
                if(x[i]=='+')
                    x[i]='-';
                else
                    x[i]='+';
            }
            while(x[0]=='+'){
                x.erase(0,1);
            }
        }
        if(x.length()>0)
            fout<<"Case #"<<l+1<<": "<<"IMPOSSIBLE"<<endl;
        else
            fout<<"Case #"<<l+1<<": "<<flip<<endl;
    }
}
