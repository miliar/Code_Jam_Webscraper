#include "bits/stdc++.h"
#include "string.h"
#include "iostream"

using namespace std;
 

int n,x,contagem;
bool impo;
string panqueca;

void val(int i){
 
    if(panqueca[i] == '+') panqueca[i]='-';
    else panqueca[i] = '+';
 
    return ;
}
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n;
 
    for(int z = 1;z <= n; ++z )
    {
        impo = false; contagem = 0;
        cin >> panqueca >> x;
 
        for(int y = 0; y < panqueca.size() - x + 1; ++y){
            if(panqueca[y] == '-' ){
              
                for(int j=0; j < x;++j)
                    val(y+j);
                contagem++;
            }
 
        }
 
        for(int y = panqueca.size() - x ;y < panqueca.size(); ++y){
            if(panqueca[y]=='-'){impo=true; break;}
        }
 
        if(!impo) cout<<"Case #"<<z<<": "<<contagem<<'\n';
        else      cout<<"Case #"<<z<<": IMPOSSIBLE\n";
 }
 
    return 0;
}