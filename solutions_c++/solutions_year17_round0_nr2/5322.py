#include <fstream>
#include <string>
#include <iostream>
using namespace std;


int main(int argc, char **argv) {

    ifstream input("B-large.in");
    ofstream output("output.out");
    int T,j;
    string number;
    input >> T;

    for(int t=0; t<T; t++) {
        number.clear();

        input >> number;
        cout << number << endl;

        if (number.length()==1){

             output << "Case #" << t+1 << ": " << number << endl;
            continue;



        }

        for(int i=0;i<number.length()-1;i++){


            if(number.at(i)>number.at(i+1)){

                j=i;
                while(j>0){
                    if(number.at(j)==number.at(j-1)){

                        j--;

                    }
                    else break;

                }



                number.at(j)--;

                for(int z=j+1;z<number.length();z++){

                    number.at(z)='9';




                }

                break;
            }




        }

            while(number.at(0)=='0'){


                number.erase(0,1);


            }




        output << "Case #" << t+1 << ": " << number << endl;
















    }








}


