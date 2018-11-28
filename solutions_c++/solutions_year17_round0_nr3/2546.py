#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
long long minLR, maxLR;

void solve(long long N, long long K)
{
    long long pot2 = 1;
    long long placed = 0;
    while(1){
        K -= pot2;
        if (K <= 0) {
            K += pot2;
            pot2 /= 2;
            break;
        }
        placed += pot2;
        pot2 = pot2 * (long long)2;

    }
    long long totalPlaces = N - placed;
    long long totalDivisions = pot2*2>0?pot2*2:1;
    long long spaces = totalPlaces / totalDivisions;
    long long amountSpacesPlus1 = totalPlaces - spaces*totalDivisions;
    if (amountSpacesPlus1 >= K) {
        if (K > 0) {
            minLR = maxLR = (spaces) / 2;
        }
        else {
            minLR = maxLR = spaces;
        }
        if ((spaces + 1) % 2 == 0) maxLR++;
    }
    else {
        if (K > 0) {
            minLR = maxLR = (spaces - 1) / 2;
        }
        else {
            minLR = maxLR = (spaces - 1);
        }
        if ((spaces) % 2 == 0) maxLR++;
    }
}

int Calc(int right, int pos, vector<bool> &used) {
    int ret = 0;
    if (right) {
        for (int i = pos+1; i < used.size(); i++) {
            if (used[i] == true) return ret;
            ret++;
        }
    }
    else {
        for (int i = pos-1; i >= 0; i--) {
            if (used[i] == true) return ret;
            ret++;
        }
    }

}

pair<int,int> solveBrute(int N, int K) {
    vector<bool> used(N+2, false);
    used[0] = used[N + 1] = true;
    int bestMinLR, bestMaxLR, bestIndex;
    bestMinLR = -1; bestMaxLR = -1;

    while (K > 0) {

        bestMinLR = 0; bestMaxLR = 0;
        for (int i = 0; i < N; i++) {
            if (used[i] == false) {
                int Ls = Calc(0, i, used);
                int Rs = Calc(1, i, used);
                if (min(Ls, Rs) > bestMinLR || (min(Ls,Rs)==bestMinLR && max(Ls,Rs) > bestMaxLR)) {
                    bestMinLR = min(Ls, Rs);
                    bestMaxLR = max(Ls, Rs);
                    bestIndex = i;
                }
            }
        }
        used[bestIndex] = true;
        K--;
    }

    return make_pair(bestMaxLR, bestMinLR);
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");;
    int T;
    fin >> T;
    for (int test = 0; test < T; test++)
    {
        long long N,K;
        fin >> N >> K;
        solve(N,K);

        /*pair<int,int> res = solveBrute(N, K);
        fout2 << "Case #" << test + 1 << ": ";
        fout2 << res.first << " " << res.second << endl;
        */
        fout << "Case #" << test + 1 << ": ";
        fout << maxLR << " " << minLR << endl;

        //cout << "Case #" << test + 1 << ": " << "Brute Force = " << res.first << " " << res.second;
        cout << " -- " << test + 1 << ": " << "Fast way = " << maxLR << " " << minLR << endl;

    }
    return 0;
}

