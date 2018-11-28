#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;


int main() {
    ofstream cout("/Users/leslie/testcode/google/result.txt");
    ifstream cin("/Users/leslie/testcode/google/A-large.in");
  //  ifstream cin("/Users/leslie/testcode/google/testdata.txt");

    int T,t,pos = 0;
    //int base = 0;
    long long N, K;
    char d;
    cin >> T;
    string line;
    string kline;
   // cout<<'test'<<endl;
    bool first = true;
    while (t++ != T){

        line.clear();

        if(!first){
        line +=d;}
        first = false;
        while(1)
        {
            cin >> d;
            if(d != '+' && d != '-'){
                break;
            }
            line +=d;
        }
        kline.clear();
        while((int)d>= 48 && (int)d <= 57){
            //K = int(d) -48;
            //cout<<(int)d<<endl;

            if(!cin.eof()){
                kline += d;
                cin >> d;
            }else{
                break;
            }
        }
       // cout<<11111<<endl;
        K =0;
        for(int j =kline.length() ;j> 0 ;j--){
            //cout<<K<<endl;
            K +=((int)kline[j-1]-48)*pow(10,(kline.length()-j));
        }
   //     cout<<kline<<endl;
    //    cout<<K<<endl;
        int times = 0;
        while(1){
            if(line.find('-') == -1){
                cout << "Case #" << t << ": " <<times<< endl;
                break;
            }
            else{
                pos = 0;
                pos = line.find_first_of('-', 0);
                if(line.length()-pos < K)
                {
                    cout << "Case #" << t << ": " << "IMPOSSIBLE"<< endl;
                    break;
                }else{
                    times ++;
                   // cout<<times<<endl;
                    for(int j =0 ;j < K;j++){
                        if(line[j+pos] == '+'){
                            line[j+pos] = '-';
                        }else{
                            line[j+pos] = '+';
                        }

                    }
                    continue;
                }
            }
        }
    }
    return 0;

}