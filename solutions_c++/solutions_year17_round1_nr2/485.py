#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int minserve(int amt, int perserve){
    int ans = (int) (amt / (perserve*1.1)) + 5;
    while(ans*perserve*1.1 >= amt-0.001){
        ans--;
    }
    return ans+1;
}

int maxserve(int amt, int perserve){
    int ans = (int) (amt / (perserve*0.9)) - 5;
    while(ans*perserve*0.9 <= amt+0.001){
        ans++;
    }
    return ans-1;
}

int main(){
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T; fin >> T;
    for(int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";
        int N, P; fin >> N >> P;
        int ngrams[N];
        vector<int> packs[N];
        for(int n = 0; n < N; n++){
            fin >> ngrams[n];
        }
        vector<int> line;
        for(int n = 0; n < N; n++){
            line.clear();
            for(int p = 0; p < P; p++){
                int temp; fin >> temp;
                line.push_back(temp);
            }
            sort(line.begin(), line.end());
            packs[n] = line;
        }

        int index[N];
        for(int n = 0; n < N; n++){
            index[n] = 0;
        }
        int ans = 0;

        /*
        for(int n = 0; n < N; n++){
            cout << n << " " << ngrams[n] << " " << packs[n][0] << " " << minserve(packs[n][0], ngrams[n]) << " " << maxserve(packs[n][0], ngrams[n]) << "\n";
        }
        */
        int curserve = 0;
        bool cont = true;
        while(cont){
            for(int n = 0; n < N; n++){
                if(index[n] >= P){
                    cont = false;
                    break;
                }
            }
            if(cont){
                //check if cur works
                int cmin = minserve(packs[0][index[0]], ngrams[0]);
                int cmax = maxserve(packs[0][index[0]], ngrams[0]);
                for(int n = 1; n < N; n++){
                    cmin = max(cmin, minserve(packs[n][index[n]], ngrams[n]));
                    cmax = min(cmax, maxserve(packs[n][index[n]], ngrams[n]));
                }
                if(cmin <= cmax && cmax > 0){
                    ans += 1;
                    for(int n = 0; n < N; n++){
                        index[n]++;
                    }
                }else{
                    //find indexes to increase

                    for(int n = 0; n < N; n++){
                        int tmin = minserve(packs[n][index[n]], ngrams[n]);
                        int tmax = maxserve(packs[n][index[n]], ngrams[n]);
                        if(tmin > tmax){
                            index[n]++;
                        }else if(tmax < cmin){
                            index[n]++;
                        }
                    }
                }
            }
        }

        fout << ans << "\n";
    }

    //cout << minserve(100, 1) << " " << maxserve(100,1) << "\n";

    fin.close();
    fout.close();
    return 0;
}

