#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;
int main() {
    ifstream in ("cjA.in");
    ofstream out ("cjA.out");
    
    long cases;
    in >> cases;
    for(long q=1; q<=cases; q++){
        long dist;
        in >> dist;
        long n;
        in >> n;
        double maxi = -1.0;
        bool first = true;
        for(long i = 0; i<n; i++){
            long start, speed;
            in >> start >> speed;
            double t = (double)(dist-start)/(double)speed;
            if(first){
                maxi = (double)dist/(double)t;
                first =false;
            }
            maxi = min(maxi,(double)dist/(double)t); 
        }
        out << "Case #" << q << ": ";
        out << fixed << setprecision(6) << maxi << endl;
    }
    
    return 0;
}