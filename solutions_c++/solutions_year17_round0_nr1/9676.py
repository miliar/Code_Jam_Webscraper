#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
int main(){
    optimizar_io
    freopen( "oversized_input.txt","r",stdin);
    freopen( "oversized_output.txt","w",stdout);
    int a,k,cont,aux,tot,i;
    string b;
    cin>>a;
    for(int i=1;i<=a;++i){
        cont=0;
        cin>>b>>k;
        if(b.find('-')<(int)b.size()){
                    for(int j=0;j<(int)b.size()-k+1;++j){
                        if(b[j]=='-'){
                        cont++;
                        tot=0;
                        aux=j;
                            while(tot<k){
                                if(b[aux]=='+'){b[aux]='-';}
                                else{b[aux]='+';}
                                aux++;
                                tot++;
                            }
                    }
                }
            if(b.find('-')<(int)b.size()){cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;goto kok;}
            cout<<"Case #"<<i<<": "<<cont<<"\n";
        }
        else{cout<<"Case #"<<i<<": 0\n";}
        kok:;
    }
    return 0;
}
