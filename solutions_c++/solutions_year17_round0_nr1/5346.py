#include <fstream>
#include <string>
#include <iostream>
using namespace std;

void reverse (char& symbol) {
    if (symbol=='-') {
        symbol='+';
    } else symbol='-';

}
int main(int argc, char **argv) {

    ifstream input("A-large.in");
    ofstream output("output.out");
    int T;
    int width;
    int moves;
    int same;
    int all;
    string pancakes;
    input >> T;

    for(int t=0; t<T; t++) {
        moves = 0;
        pancakes.clear();
        width=0;
        same=0;
        all=1;

        input >> pancakes ;
        cout << pancakes << endl;

        input >> width;
        cout << "width = " << width << endl;


        for(int i=0; i<pancakes.length() - width + 1; i++) {

            if(pancakes.at(i)=='-') {

                for(int j=0; j<width; j++) {

                    reverse(pancakes.at(i+j));

                }
                moves++;


            }

        }

        for(int i=pancakes.length()-1 ; i >= 0 ; i--) {

            if(pancakes.at(i)=='-') {
                all=0;
                break;

            }


        }

        output << "Case #" << t+1<< ": ";
        if(all==1) {
            output << moves << endl;
        } else output <<"IMPOSSIBLE" << endl;

    }








}


