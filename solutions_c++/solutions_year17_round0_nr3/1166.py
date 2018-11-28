#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int t;
    ifstream in("C-large.in");
    ofstream out("out.txt");
    long long n,k;
    in>>t;
    for(int it=0;it<t;it++){
        in>>n>>k;
        long long numU=1;
        long long numL=0;
        long long count=0;
        for(;count+numU+numL<k;){
            if(n&1){
                count+=numU+numL;
                numU=2*numU+numL;
                n/=2;
            }else{
                count+=numU+numL;
                numL=numU+2*numL;
                n/=2;
            }
        }
        if(count+numU>=k)
            out<<"Case #"<<it+1<<": "<<n/2<<" "<<(n-1)/2<<endl;
        else
            out<<"Case #"<<it+1<<": "<<(n-1)/2<<" "<<(n-2)/2<<endl;
    }
}
