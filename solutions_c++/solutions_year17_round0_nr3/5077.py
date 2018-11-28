//
// Created by brian on 4/7/2017.
//
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

long bitReverse(long value);
class duo{

public:
    long x, y;
    duo(long a, long b){x=a;y=b;}
    bool diff(){return x!=y;}
    duo * result(int i){
        if(x == 0 && (y == 1 || y == 0)){
                duo *res = new duo(0,0);
                return res;
        }
        else {
            if (i == 0) {
                duo *res = (x % 2 == 0) ? new duo((x - 1) / 2, (x - 1) / 2 + 1) : new duo((x - 1) / 2, (x - 1) / 2);
                return res;
            } else {
                duo *res = (y % 2 == 1) ? new duo((y - 1) / 2, (y - 1) / 2) : new duo((y - 1) / 2, (y - 1) / 2 + 1);
                return res;
            }
        }
    }
};

int main() {
    long T, N, K, Ncopy, Kcopy, digitsN(0), digitsK(0), Xor, a, b;
    int path;
    duo * start;
    ifstream fin ("C-small-2-attempt0.in");
    ofstream fout ("outputC.txt");
    fin >> T;
    for(int i = 0; i < T; i++){
        fin >> N >> K;

        Ncopy = N;
        Kcopy = K;
        for (digitsK = 0; Kcopy > 0; Kcopy >>= 1)
            digitsK++;
        for (digitsN = 0; Ncopy > 0; Ncopy >>= 1)
        digitsN++;
        Ncopy = N;
        start = (N % 2 != 0) ? new duo((N - 1) / 2, (N - 1) / 2) : new duo((N - 1) / 2, (N - 1) / 2 + 1);

        a = 0; b = 1;

        for(int j = 0; j < digitsK-1; j++) {
            if (N % 2 == 0) {
                a = 2*a + b;
            } else {
                 b = 2*b + a;
            }
            N >>= 1;
        }
        for(int j = 0; j < digitsK-1; j++){
            start = start->result(1);
        }
        if(K >= (1 << (digitsK-1))+b){
            if(start->x < start->y) start->y--;
            else start->x--;
        }
        fout << "Case #" << i+1 << ": " << start->y << " " << start->x << endl;
    }
}
