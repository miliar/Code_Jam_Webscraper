#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool caso1(string P){
    for(auto p:P){
        if(p!='1'|| p!='0')
            return true;
    }
    return false;
}

string char_1(char c){
    switch(c){
        case '1': return "";
        case '2': return "1";
        case '3': return "2";
        case '4': return "3";
        case '5': return "4";
        case '6': return "5";
        case '7': return "6";
        case '8': return "7";
        case '9': return "8";
}
}

string char_2(char c){
    switch(c){
        case '1': return "0";
        case '2': return "1";
        case '3': return "2";
        case '4': return "3";
        case '5': return "4";
        case '6': return "5";
        case '7': return "6";
        case '8': return "7";
        case '9': return "8";
}
}


string ordenar(string P){
    char c;
    string P_aux=P;
    sort(P_aux.begin(),P_aux.end());
    if(P_aux==P)
        return P;
    else{
        int i;
        for(i=0;i<P.size()-1;++i){
            if(P[i+1]<P[i])
                break;
        }
        if(i==0){
        c=P[i];
        P.replace(i,1,char_1(P[i]));
        if(c!='1')
        ++i;
        }
        else{
            P.replace(i,1,char_2(P[i]));
            ++i;
        }
        while (i<P.size()){
            P.replace(i,1,"9");
            i++;
        }
        return ordenar(P);
    }
}

int main()
{
    long test,caso=1;
    long long N;
    cin>>test;
    string P,P_aux;
    while(caso<=test){
        cin>>N;
        P=to_string(N);
        cout<<"Case #"<<caso<<": "<<ordenar(P)<<endl;
        caso++;
    }
    return 0;
}
