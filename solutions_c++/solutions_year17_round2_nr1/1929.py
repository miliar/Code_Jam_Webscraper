#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream in("A-large.in");
    ofstream out("out.txt");
    int t;
    in>>t;
    double k,s,d,n,max=0;
    for(int it=0;it<t;it++){
        in>>d>>n;
        max=0;
        for(int i=0;i<n;i++){
            in>>k>>s;
            if(max<(d-k)/s)
                max=(d-k)/s;
        }
        out<<"Case #"<<it+1<<": "<<fixed<<d/max<<endl;
    }
}
