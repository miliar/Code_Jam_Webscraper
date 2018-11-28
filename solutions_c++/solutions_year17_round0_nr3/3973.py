#include <fstream>
#include <iostream>
using namespace std;


int main(int argc, char * argv[])
{
    if (argc != 2)
        return -1;
    
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    
    int T, t;
    long long int N, K;
    long long int minn, maxn;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> N >> K;
        
        minn = (N - 1) / 2;
        maxn = N / 2;
        K--;
        
        while (K > 0 && (minn != 0 || maxn != 0)) {
            N = (K % 2) ? maxn : minn;
            K = (K + 1) / 2;
            
            minn = (N - 1) / 2;
            maxn = N / 2;
            K--;
        }
        
        fout << "Case #" << t << ": " << maxn << ' ' << minn << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
