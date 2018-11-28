#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#define colori 6
//#defire R 0x1
//#define B 0x10
//#define Y 0x100
//#define G 0x110
//#define O 0x101
//#define V 0x11
//enum coloriTipo{R,O,Y,G,B,V};
using namespace std;
ifstream in("B-small.in");
ofstream out("out.out");
int nUnicorni,unPerColore[colori];

bool posso(int c,int l){
    return c!=l && c!=((l+1)%colori) && ((c+1)%colori)!=l;
}

vector<char> calcola(){
    vector<char> stalla;
    for (int i=0;i<colori;i++){
        if (unPerColore[i]){
            stalla.push_back(i);
            unPerColore[i]--;
            break;
        }
    }
    for (int i=1;i<nUnicorni;i++){
        int max=0,maxC=0;
        for (int c=0;c<colori;c++){
            if (posso(c,stalla.back())&&unPerColore[c]>max){
                max=unPerColore[c];
                maxC=c;
            }
        }
        if (max==0){
            stalla.clear(); return stalla;
        }
        unPerColore[maxC]--;
        stalla.push_back(maxC);
    }
    return stalla;
}


int main(){
    int caso,ncasi;
    in>>ncasi;
    bool possible;
    vector<char> stalla;
    for (caso=1;caso<=ncasi;caso++){
        stalla.clear();possible=true;
        in>>nUnicorni;
        cout<<nUnicorni;
        for (int i=0;i<colori;i++){
            in>>unPerColore[i];
        }
        for (int i=0;i<colori;i+=2){
            int stessoColore=unPerColore[i];
            if (i==0) stessoColore+=unPerColore[5];
            else stessoColore+=unPerColore[i-1];
            if (i==5) stessoColore+=unPerColore[0];
            else stessoColore+=unPerColore[i+1];
            if (stessoColore>0 && stessoColore*2>nUnicorni){
                possible=false;
                break;
            }
        }
        if (!possible){
            out<<"Case #"<<caso<<": "<<"IMPOSSIBLE"<<endl;
            cout<<"Case #"<<caso<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        stalla=calcola();
        if (stalla.size()!=nUnicorni){
            out<<"Case #"<<caso<<": "<<"IMPOSSIBLE"<<endl;
            cout<<"Case #"<<caso<<": "<<"IMPOSSIBLE"<<endl;
        } else {
            out<<"Case #"<<caso<<": ";
            for (int i=0;i<stalla.size();i++){
                int t=stalla.at(i);
                out<<(t==0?'R':t==1?'O':t==2?'Y':t==3?'G':t==4?'B':'V');
            }
            out<<endl;
            cout<<"Case #"<<caso<<": "<<endl;
        }
    }
    return 0;
}
