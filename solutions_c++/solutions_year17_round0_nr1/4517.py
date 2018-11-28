#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

typedef struct{
    int d;
    int a;
} train;

int main(int argc, char** argv){
    int ncases;
    cin >> ncases >> ws;
    for(int c=0; c<ncases; c++){
        string p;
        int k=0, nf=0;
        cin >> p >> ws >> k >> ws;
        bool flip = true;
        while(flip){
            flip = false;
            for(int i=0; i + k <= p.size(); i++){
                int con=0;
                char c=p[i];
                for(int j=0; j < (k + k/2); j++){
                    if(i + j < p.size() && c == '-'){
                        con++;
                    } else{
                        con = 0;
                    }
                    if(con == k){
                        flip = true;
                        for(int j=0; j < k; j++){
                            p[i + j] = (p[i + j] == '+')? '-' : '+';
                        }
                        nf ++;
                    }
                }
            }
        }
        if(p.find('-') != string::npos){
            cout << "Case #" << c + 1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << c + 1 << ": " << nf << endl;
        }
        
    }
    return 0;
}