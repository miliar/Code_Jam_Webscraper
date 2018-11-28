#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    int i,j,l;
    int T;
    long long esq, dir;
    long long n, k;
    vector <int> bath;
    vector <long long> distl;
    vector <long long> distr;
    int chosen;
    cin >> T;
    for(i=1; i<=T; i++){
        cin >> n >> k;
        bath.resize(n+2);
        distl.resize(n+2);
        distr.resize(n+2);
        for(j=0; j<k; j++){
            //calcula esquerda
            for(esq=0, l=1; l<n+1; l++)
                if(bath[l] == 0)
                    distl[l] = l-esq-1;
                else
                    esq = l;
            //calcula direita
            for(dir=n+1, l=n; l>=1; l--)
                if(bath[l] == 0)
                    distr[l]=dir-l-1;
                else
                    dir =l;
            //ve max de min
            for(chosen=0, l=1; l<n+1; l++)
                if(bath[l]==0){
                    if(min(distl[chosen],distr[chosen]) < min(distl[l],distr[l]))
                        chosen = l;
                    else if(min(distl[chosen],distr[chosen]) == min(distl[l],distr[l]))
                        //ve max de max
                        if(max(distl[chosen],distr[chosen]) < max(distl[l],distr[l]))
                            chosen = l;
                        //ja escolhe o mais a esquerda
                }
            //ocupa o escolhido
            bath[chosen] = 1;
        }
        cout << "Case #" << i << ": " << max(distl[chosen],distr[chosen]) << " " << min(distl[chosen],distr[chosen]) << "\n";
        bath.clear();
        distl.clear();
        distr.clear();
    }
    return 0;
}
