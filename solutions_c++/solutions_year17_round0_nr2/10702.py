#include <iostream>
#include <string>
#include <sstream>
using namespace std;
#include <fstream>


string IntToString (int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}


int main(){

    ifstream fin;
    fin.open("B-small-attempt1.in");

    ofstream fout;
    fout.open("B-small-output.txt");

    if(fin){
        int testCases=0;
        fin >> testCases;
        //cout << testCases;

        for(int t=0;t<testCases;t++){




            unsigned long long tidyNum=0;
            unsigned long long  upperLimit=11111110;

            fin >> upperLimit;
            for(unsigned long long i=upperLimit;i>=0;i--){
                string num=IntToString(i);
               // cout << num;
                bool notTidy=false;

                if(num[0]=='0'){
                    //cout <<"not tidy1"<<endl;
                            notTidy=true;
                            break;
                }
                else{
                    for(int n=0;n<num.length()-1;n++){
                        if(num[n]>num[n+1]){
         //                  cin >> num;
                          //  cout <<num<<  "is not tidy"<<endl;
                            notTidy=true;
                            break;
                        }
                    }
                    if(notTidy==false){
                        //cout <<num<<  "is tidy"<<endl;
                        tidyNum=i;
                        break;
                    }

                }
            }

            cout << "Case #"<<t+1<<": "<< tidyNum<<endl;
            fout << "Case #"<<t+1<<": "<< tidyNum<<endl;







        }
    }
    else{

    }
    fin.close();
    fout.close();


}
