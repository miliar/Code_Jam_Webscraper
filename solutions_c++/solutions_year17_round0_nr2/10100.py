#include <iostream>
#include <fstream>
#define hatvany 4


using namespace std;

int main()
{
    int darab;
    int *szamok, *megoldas;
    int *jegyek;
    ifstream f;
    f.open("B-small-attempt6.in");
    f >> darab;
    szamok=new int[darab];
    megoldas=new int[darab];
    for(int i=0;i<darab;i++){
        f >> szamok[i];
    }
    f.close();
    ofstream s;
    s.open("B-small-attempt6.in");
    for(int i=0;i<darab;i++){
        s << i+1<<":"<< szamok[i];
    }
    s.close();
    for(int i=0;i<darab;i++){
        if(szamok[i]<10){
            megoldas[i]=szamok[i];
        }else{
            jegyek=new int[hatvany];
            for(int k=hatvany-1;k>=0;k--){
                jegyek[k]=szamok[i]%10;
                szamok[i]=szamok[i]/10;
            }
            bool kesz=false;
            while (!kesz) {
                int k=hatvany;
                while((k>0) && (jegyek[k-1]<=jegyek[k]))
                    k--;
                if(k==0){
                    kesz=true;
                }else{
                    if(jegyek[k-1]!=0){
                        jegyek[k-1]--;
                        for(int m=k;m<hatvany;m++)
                            jegyek[m]=9;
                    }else{
                        int m=k-1;
                        while((m>=0)&&(jegyek[m]==0))
                            m--;
                        if(m>=0){
                            jegyek[m]--;
                            for(int l=m;l<hatvany;l++)
                                jegyek[l]=9;
                        }
                    }
                }
            }
            megoldas[i]=jegyek[0];
            for(int k=1;k<hatvany;k++){
                megoldas[i]*=10;
                megoldas[i]+=jegyek[k];
        }
        }
    }
    ofstream g;
    g.open("ki.txt");
    for(int i=0;i<darab;i++){
        g <<"Case #"<<i+1<<": " <<megoldas[i]<<endl;
    }
    return 0;
}












