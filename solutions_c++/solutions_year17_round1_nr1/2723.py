#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string.h>
#include <fstream>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <bitset>
#define ull unsigned long long
#define ll long long
#define inf 10000000000000
#define bil 1000000000

using namespace std;

ifstream input;
ofstream output;

bool ppsort(pair<int, int>a, pair<int, int>b){
    if (a.first == b.first) return a.second < b.second;
    else return a.first < b.first;
}



int main(int argc, char *argv[]){
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    input.sync_with_stdio(false);
    output.sync_with_stdio(false);
    input.open("/users/jihan/Academic/Algorithmic Programming/Codeforces/CFTemplate/in.txt");
    output.open("/users/jihan/Academic/Algorithmic Programming/Codeforces/CFTemplate/out.txt");
    
    int tests;
    input>>tests;
    
    int r, w;
    string s;
    char c[30][30];
    vector<pair<int, int>> index[27];
    
    for (int test=1;test<=tests;test++){
        output<<"Case #"<<test<<": ";
        
        input>>r>>w;
        for (int i=0;i<27;i++) index[i].clear();
        for (int i=0;i<r;i++){
            input>>s;
            for (int j=0;j<s.size();j++){
                c[i][j] = s[j];
                if (c[i][j] != '?'){
                    index[c[i][j]-'A'].push_back(make_pair(i, j));
                }
            }
        }
        for (int i=0;i<26;i++){
            sort(index[i].begin(), index[i].end(), ppsort);
            if (index[i].size() == 0) continue;
            for (int j=index[i][0].first;j<index[i][index[i].size()-1].first;j++){
                for (int k=index[i][0].second;k<index[i][index[i].size()-1].second;k++){
                    c[j][k] = 'A' + i;
                }
            }
        }
        bool flag = false;
        for (int i=0;i<26;i++){
            sort(index[i].begin(), index[i].end(), ppsort);
            flag = false;
            if (index[i].size() == 0) continue;
            if (index[i][0].second != 0){
                for (int j=index[i][0].first;j<=index[i][index[i].size()-1].first;j++){ //test left
                    if (c[j][index[i][0].second-1] != '?') break;
                    if (j == index[i][index[i].size()-1].first) flag = true;
                }
                if (flag){
                    for (int j=index[i][0].first;j<=index[i][index[i].size()-1].first;j++){ //test left
                        c[j][index[i][0].second-1] = 'A' + i;
                    }
                    index[i].push_back(make_pair(index[i][0].first, index[i][0].second-1));
                    i--;
                    continue;
                }
            }
            if (index[i][index[i].size()-1].second < w-1){
                for (int j=index[i][0].first;j<=index[i][index[i].size()-1].first;j++){ //test right
                    if (c[j][index[i][index[i].size()-1].second+1] != '?') break;
                    if (j == index[i][index[i].size()-1].first) flag = true;
                }
                if (flag){
                    for (int j=index[i][0].first;j<=index[i][index[i].size()-1].first;j++){ //test right
                        c[j][index[i][index[i].size()-1].second+1] = 'A' + i;
                    }
                    index[i].push_back(make_pair(index[i][index[i].size()-1].first, index[i][index[i].size()-1].second+1));
                    i--;
                    continue;
                }
            }
        }
        for (int i=0;i<26;i++){
            sort(index[i].begin(), index[i].end(), ppsort);
            flag = false;
            if (index[i].size() == 0) continue;
            if (index[i][0].first > 0){
                for (int j=index[i][0].second;j<=index[i][index[i].size()-1].second;j++){ //test up
                    if (c[index[i][0].first-1][j] != '?') break;
                    if (j == index[i][index[i].size()-1].second) flag = true;
                }
                if (flag){
                    for (int j=index[i][0].second;j<=index[i][index[i].size()-1].second;j++){ //test up
                        c[index[i][0].first-1][j] = 'A' + i;
                    }
                    index[i].push_back(make_pair(index[i][0].first-1, index[i][0].second));
                    i--;
                    continue;
                }
            }
            if (index[i][index[i].size()-1].first < r-1){
                for (int j=index[i][0].second;j<=index[i][index[i].size()-1].second;j++){ //test up
                    if (c[index[i][index[i].size()-1].first+1][j] != '?') break;
                    if (j == index[i][index[i].size()-1].second) flag = true;
                }
                if (flag){
                    for (int j=index[i][0].second;j<=index[i][index[i].size()-1].second;j++){ //test up
                        c[index[i][index[i].size()-1].first+1][j] = 'A' + i;
                    }
                    index[i].push_back(make_pair(index[i][index[i].size()-1].first+1, index[i][index[i].size()-1].second));
                    i--;
                    continue;
                }
            }
        }
        output<<"\n";
        for (int i=0;i<r;i++){
            for (int j=0;j<w;j++){
                output<<c[i][j];
            }
            output<<"\n";
        }
        
        
        output<<"\n";
    }
    
    return 0;
}
