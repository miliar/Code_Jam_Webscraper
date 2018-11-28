#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <algorithm>
#include <fstream>
#include <utility>
#define MAX 987654321
using namespace std;
typedef long long ll;

int main() {
    int T;
    ifstream input("/Users/ahnzeus/Desktop/input.in");
    ofstream output("/Users/ahnzeus/Desktop/output.txt");
    
    //cin >> T;
    input >> T;
    for(int t=0;t<T;t++){
        int r,c;
        //cin >> r >> c;
        input >> r >> c;
        char letter[25][25];
        vector<pair<int,int>> v;
        
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                //cin >> letter[i][j];
                input >> letter[i][j];
                if(letter[i][j]!='?'){
                    v.push_back(make_pair(i, j));
                }
            }
        }
        
        sort(v.begin(),v.end());
        
        for(int i=0;i<(int)v.size();i++){
            if(i==0){
                if((int)v.size()==1){
                    for(int x=0;x<r;x++){
                        for(int y=0;y<c;y++){
                            letter[x][y] = letter[v[i].first][v[i].second];
                        }
                    }
                    break;
                } else {
                    if(v[i+1].first==v[i].first){
                        int acceptedX = v[i].first;
                        for(int j=i;j<(int)v.size();j++){
                            if(v[j].first>v[i].first){
                                acceptedX = v[j].first - 1;
                                break;
                            } else if(j==(int)v.size()-1){
                                acceptedX = r - 1;
                            }
                        }
                        for(int x=0;x<=acceptedX;x++){
                            for(int y=0;y<v[i+1].second;y++){
                                letter[x][y] = letter[v[i].first][v[i].second];
                            }
                        }
                    } else {
                        for(int x=0;x<v[i+1].first;x++){
                            for(int y=0;y<c;y++){
                                letter[x][y] = letter[v[i].first][v[i].second];
                            }
                        }
                    }
                }
            } else if(i==(int)v.size()-1){
                if(v[i].first==v[i-1].first){
                    int acceptedX = v[i].first;
                    for(int j=i;j>=0;j--){
                        if(v[j].first<v[i].first){
                            acceptedX = v[j].first + 1;
                            break;
                        } else if(j==0){
                            acceptedX = 0;
                        }
                    }
                    for(int x=acceptedX;x<r;x++){
                        for(int y=v[i-1].second+1;y<c;y++){
                            letter[x][y] = letter[v[i].first][v[i].second];
                        }
                    }
                } else {
                    for(int x=v[i-1].first+1;x<r;x++){
                        for(int y=0;y<c;y++){
                            letter[x][y] = letter[v[i].first][v[i].second];
                        }
                    }
                }
            } else{
                if(v[i].first != v[i-1].first){
                    if(v[i].first != v[i+1].first){
                        for(int x=v[i-1].first+1;x<v[i+1].first;x++){
                            for(int y=0;y<c;y++){
                                letter[x][y] = letter[v[i].first][v[i].second];
                            }
                        }
                    } else {
                        int minX = v[i-1].first + 1;
                        int maxX = v[i].first;
                        
                        for(int j=i;j<(int)v.size();j++){
                            if(v[j].first>v[i].first){
                                maxX = v[j].first - 1;
                                break;
                            } else if (j==(int)v.size()-1){
                                maxX = r - 1;
                            }
                        }
                        
                        for(int x=minX;x<=maxX;x++){
                            for(int y=0;y<v[i+1].second;y++){
                                letter[x][y] = letter[v[i].first][v[i].second];
                            }
                        }
                    }
                } else {
                    int minX = v[i].first;
                    
                    for(int j=i;j>=0;j--){
                        if(v[j].first!=v[i].first){
                            minX = v[j].first + 1;
                            break;
                        } else if (j==0){
                            minX = 0;
                        }
                    }
                    
                    if(v[i].first != v[i+1].first){
                        for(int x=minX;x<v[i+1].first;x++){
                            for(int y=v[i].second;y<c;y++){
                                letter[x][y] = letter[v[i].first][v[i].second];
                            }
                        }
                    } else {
                        int maxX = v[i].first;
                        
                        for(int j=i;j<(int)v.size();j++){
                            if(v[j].first>v[i].first){
                                maxX = v[j].first - 1;
                                break;
                            } else if (j==(int)v.size()-1){
                                maxX = r - 1;
                            }
                        }

                        for(int x=minX;x<=maxX;x++){
                            for(int y=v[i].second;y<v[i+1].second;y++){
                                letter[x][y] = letter[v[i].first][v[i].second];
                            }
                        }
                    }
                }
            }
        }
        output << "Case #" << t+1 << ": "<<endl;
        for(int x=0;x<r;x++){
            for(int y=0;y<c;y++){
                //cout << letter[x][y];
                output << letter[x][y];
            }
            //cout <<'\n';
            output << '\n';
        }
    }
}
