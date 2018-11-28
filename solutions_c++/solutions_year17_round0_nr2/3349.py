#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("b1.in");
ofstream fout("b1.out");
bool check(string x){
    for(int i=0;i<x.length()-1;i++){
        if(x[i]>x[i+1])
            return false;
    }
    return true;
}

int main(){
    int t;
    fin>>t;
    for(int l=0;l<t;l++){
        string x;
        fin>>x;
        while(!check(x)){
            for(int i=0;i<x.length()-1;i++){
                if(x[i]>x[i+1]){
                    for(int k=i+1;k<x.length();k++)
                        x[k]='9';
                    if(x[i]!='0'){
                        x[i]--;
                        break;
                    }
                    int temp=i;
                    while((i>=0)&&(x[i]!='0')){
                        i--;
                    }
                    if(i!=-1){
                        for(int k=i+1;k<=temp;k++)
                            x[k]='9';
                        x[i]--;
                    }
                    else{
                        for(int k=i+1;k<=temp;k++)
                            x[k]='9';
                        x.erase(0,1);
                    }
                    break;
                }
            }
        }
        while(x[0]=='0')
            x.erase(0,1);
        fout<<"Case #"<<l+1<<": "<<x<<endl;
    }
}
