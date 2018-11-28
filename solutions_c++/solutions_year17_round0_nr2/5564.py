#include <fstream>
#include <string>
#include <sstream>
#include <iostream>


using namespace std;


string intToStr (int inp)
{
    ostringstream tempVar;
    tempVar<<inp;
    return tempVar.str();
}


int main(){
    ofstream fo;
    fo.open("B-small-outputLatest.txt");
    ifstream fi;
    fi.open("B-small-attempt0.in");

    if(fi){
        int testCase=0;
        fi >> testCase;

        for(int t=0;t<testCase;t++){

            unsigned long long greatestTidy=0;
            unsigned long long  topLimit=11111;
            bool notTidy=true;
            fi >> topLimit;
            //cout <<" upper limit is="<<topLimit<<"    ";
            while(notTidy==true){
                    string  number=intToStr(topLimit);
                   // cout <<  number<<"  len"<< number.length()<<"       ";

                    if( number[0]=='0'){
                                notTidy=true;
                    }
                    else if( number.length()==1){
                        notTidy=false;
                    }
                    else{
                        for(int n=0;n< number.length()-1;n++){
                            if( number[n]> number[n+1]){
                                notTidy=true;

                                break;
                            }
                            else{
                                notTidy=false;
                            }

                        }
                    }
                    if(notTidy==false){
                        greatestTidy=topLimit;

                        break;//
                    }
                    topLimit--;


            }
            fo <<  "Case #"  <<  t+1  <<  ": "  << greatestTidy  <<  endl;







        }
    }
    else{

    }
        fo.close();

        fi.close();



}
