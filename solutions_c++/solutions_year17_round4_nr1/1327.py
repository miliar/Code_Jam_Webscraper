#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T; fin >> T;
    for(int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";
        int N, P; fin >> N >> P;
        int rem[] = {0,0,0,0};
        for(int n = 0; n < N; n++){
            int input; fin >> input;
            rem[input % P]++;
        }
        int ans = rem[0];
        if(P == 2){
            ans += (rem[1]+1)/2;
        }else if(P == 3){
            ans += min(rem[1], rem[2]);
            ans += (max(rem[1],rem[2]) - min(rem[1], rem[2])+2)/3;
        }else if(P == 4){
            ans += rem[2]/2;
            ans += min(rem[1], rem[3]);
            int x = max(rem[1],rem[3]) - min(rem[1],rem[3]);
            if(rem[2] % 2 == 1){
                if(x >= 2){
                    ans += 1;
                    x -= 2;
                    ans += (x+3)/4;
                }else{
                    ans += 1;
                }
            }else{
                ans += (x+3)/4;
            }
        }
        fout << ans << "\n";
    }
}
