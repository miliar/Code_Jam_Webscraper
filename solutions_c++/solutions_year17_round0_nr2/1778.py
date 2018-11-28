#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
ifstream in("B-small.in");
ofstream out("out.out");

using namespace std;

int main()
{
    int caso,ncasi,k;
    in>>ncasi;
    int cifra;
    vector<int> numero;
    in.get();
    for (caso=1;caso<=ncasi;caso++){
        numero.clear();
        cifra=in.get()-'0';
        numero.push_back(cifra);
        cifra=in.get()-'0';
        while (cifra>=0&&cifra<10){
            numero.push_back(cifra);
            cifra=in.get()-'0';
        }
        for (int i=numero.size()-1;i>0;i--){
            if (numero.at(i)<numero.at(i-1)){
                numero.at(i)=9;
                numero.at(i-1)--;
                for (int j=i;j<numero.size();j++) numero.at(j)=9;
            }
        }
        out<<"Case #"<<caso<<": ";
        if (numero.at(0)!=0){out<<numero.at(0);cout<<numero.at(0);}

        for (int i=1;i<numero.size();i++) {out<<numero.at(i);cout<<numero.at(i);}
        out<<endl; cout<<endl;
    }
    return 0;
}
