#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef unsigned long long ull;

//C-large

struct cmpStruct {
    bool operator() (ull a, ull b)
    {
        return a > b;
    }
};

int main(){
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    int T; fin >> T;
    for(int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";
        ull N, K; fin >> N >> K;

        map<ull, ull> m;
        m[N] = 1;

        set<ull, cmpStruct> s;
        set<ull>::iterator it;
        s.insert(N);

        ull cur;

        while(s.size() > 0){
            it = s.begin();
            cur = *it;
            s.erase(it);
            if(cur > 1){
                if(cur % 2 == 0){
                    if(m.find(cur/2 - 1) != m.end()){
                        m[cur/2 - 1] += m[cur];
                    }else{
                        m[cur/2 - 1] = m[cur];
                        s.insert(cur/2 - 1);
                    }
                    if(m.find(cur/2) != m.end()){
                        m[cur/2] += m[cur];
                    }else{
                        m[cur/2] = m[cur];
                        s.insert(cur/2);
                    }
                }else{
                    if(m.find((cur-1)/2) != m.end()){
                        m[(cur-1)/2] += 2*m[cur];
                    }else{
                        m[(cur-1)/2] = 2*m[cur];
                        s.insert((cur-1)/2);
                    }
                }
            }
        }

        ull soFar = 0, fi, se;
        bool found = false;
        for(map<ull,ull>::reverse_iterator it = m.rbegin(); it != m.rend(); ++it){
            fi = it->first;
            se = it->second;

            //cout << fi << " : " << se << "\n";

            if(soFar + se >= K){
                if(fi % 2 == 0){
                    fout << fi/2 << " " << (fi-1)/2 << "\n";
                }else{
                    fout << (fi-1)/2 << " " << (fi-1)/2 << "\n";
                }
                found = true;
                break;
            }
            soFar += se;
        }
    }
    return 0;
}
