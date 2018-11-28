#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t,a,b;
    ifstream cin2("A-large (1).in");
    ofstream cout2("salida2.out");
    cin2>>t;
    for(int u=1;u<=t;u++){
        cin2>>a>>b;
        char x;
        string tor[a];
        for(int i=0;i<a;i++)
            cin2>>tor[i];
        for(int i=0;i<a;i++){
            x='?';
            for(int j=0;j<b;j++){
                if(tor[i][j]!='?')x=tor[i][j];
                else tor[i][j]=x;
            }
        }
        for(int i=a-1;i>=0;i--){
            x='?';
            for(int j=b-1;j>=0;j--){
                if(tor[i][j]!='?')x=tor[i][j];
                else tor[i][j]=x;
            }
        }
        int c=0,ini=0;
        string aux;
        cout2<<"Case #"<<u<<":\n";
        for(int i=1;i<a;i++){
            if(i==0){}//cout<<tor[i];
            else{
                c=0;
                ini=0;
            string xx=tor[i];
            tor[i]="";
            for(int j=0;j<b;j++){
                if(xx[j]=='?')c++;
                else{

                    aux=tor[i-1].substr(ini,c);
                    ini=j;
                    //cout<<aux;
                    c=0;
                    tor[i]+=aux+xx[j];

                    //cout<<tor[i][j];
                }
            }
            if(c!=0){
                aux=tor[i-1].substr(ini,c);
                //cout<<aux;
                tor[i]+=aux;
            }
        }
        //cout<<endl;
        }
        for(int i=a-2;i>=0;i--){

                c=0;
                ini=0;
            string xx=tor[i];
            tor[i]="";
            for(int j=0;j<b;j++){
                if(xx[j]=='?')c++;
                else{

                    aux=tor[i+1].substr(ini,c);
                    ini=j;
                    //cout<<aux;
                    c=0;
                    tor[i]+=aux+xx[j];

                    //cout<<tor[i][j];
                }
            }
            if(c!=0){
                aux=tor[i+1].substr(ini,c);
                //cout<<aux;
                tor[i]+=aux;
            }

        //cout<<endl;
        }
        for(int i=0;i<a;i++){
            cout2<<tor[i]<<endl;
        }
    }
    return 0;
}
