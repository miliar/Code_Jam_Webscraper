#include<iostream>
#include<algorithm>
#include<fstream>
#include <iomanip>
#include <vector>
using namespace std;
int main(){
    ifstream cin("A-large.in");
    ofstream cout("result.txt");
    int m;
    cin >> m;
    for(int p = 0 ; p < m; p++){
        double D,N;
        cin >> D >> N;
        double maxx = -1;
        for(int i = 0 ; i < N; i++){
            double temp,temp1;
            cin >> temp >> temp1;
            maxx = max((D-temp)/temp1,maxx);


        }

        cout <<"Case #"<<p+1<<": ";
        cout << fixed;
        cout << setprecision(6) << D/maxx<< endl;


    }
}
