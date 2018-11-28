#include<iostream>
#include<string>
#include<iomanip>
#include<fstream>
using namespace std;
int main(){
    ofstream openfile ;
    int t ;
    cin >> t ;
    double V ;
    double MAX ;
    openfile.open("aa.txt");
    int l = 1 ;
    while(t--){
        int x , y;
        cin >> x >> y ;

        MAX = 0 ;
        while(y--){
            double L , M ;
            cin >> L >> M ;
            double time = (x - L) / M ;

            MAX = max(MAX , time );
        }


         V = x / MAX ;
         openfile << "Case #"<<l<<": "<< fixed << setprecision(6) << V << endl;

         l++;

    }
    openfile.close();

    return 0 ;
}
