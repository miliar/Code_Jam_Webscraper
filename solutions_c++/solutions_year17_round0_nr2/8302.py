#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

char reduce(char num){
    switch(num){
//        case'1':    return '0';
        case'2':    return '1';
        case'3':    return '2';
        case'4':    return '3';
        case'5':    return '4';
        case'6':    return '5';
        case'7':    return '6';
        case'8':    return '7';
        case'9':    return '8';
//        case'0':    return '9';
    }
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin>>t;
    for (int x=1;x<t+1;x++){
        long long int num;
        cin>>num;
        bool print=true;
        int lastEqual=-1;
        ostringstream ss;
        ss << num;
        string stringNum=ss.str();
        for (int i=1;i<stringNum.length();i++){
            if (stringNum[i]==stringNum[i-1]){
                if (lastEqual==-1)lastEqual=i-1;
            }
            else if (stringNum[i]<stringNum[i-1]){
                 if (lastEqual==-1)lastEqual=i-1;
                 if (stringNum[lastEqual]=='1'){
                    cout<<"Case #"<<x<<": ";
                    for (int j=1;j<stringNum.length();j++)cout<<'9';
                    cout<<endl;
                    print=false;
                    break;
                 }
                 else{
                    stringNum[lastEqual]=reduce(stringNum[lastEqual]);
                    for (int j=lastEqual+1;j<stringNum.length();j++)stringNum[j]='9';
                    break;
                 }
            }
        }
        if (print==true)cout<<"Case #"<<x<<": "<<stringNum<<endl;
    }
    //stoi (str_dec,&sz);
    return 0;
}
