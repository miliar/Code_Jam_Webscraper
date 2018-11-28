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
        string k;
        cin >> k >> ws;
        int i=0;
        for(; i < k.size()-1; i++){
            if(k[i] > k[i + 1]){
                k[i]--;
                k[i+1]=0x39;
                break;
            } 
        }

        for(i++; i < k.size(); i++) k[i]=0x39;

        for(i=k.size()-1; i>=0; i--){
            if(k[i] < k[i - 1]){
                k[i]=0x39;
                k[i-1]--;
            }
        }
        cout << "Case #" << c + 1 << ": " << stol(k) << endl;
    }
    return 0;
}