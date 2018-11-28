#include <iostream>
#include <fstream>
#include <set>
#define MAX 25
using namespace std;
ifstream in("A-small.in");
ofstream out("out.out");

char cake[MAX][MAX];
char ccopy[MAX][MAX];

int main()
{
    int caso,ncasi,r,c;
    in>>ncasi;
    for (caso=1;caso<=ncasi;caso++){
        set<char> giaUsati;
        in>>r>>c;
        in.get();
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                cake[i][j]=in.get();
                ccopy[i][j]=cake[i][j];
            }
            in.get();
        }
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                if (cake[i][j]!='?' && giaUsati.find(cake[i][j])==giaUsati.end()){
                    giaUsati.insert(cake[i][j]);
                    int inizio,fine,z;
                    for (z=i-1;z>=0;z--){
                        if (cake[z][j]!='?'){
                            break;
                        } else
                            cake[z][j]=cake[i][j];
                    }
                    inizio=z+1;
                    for (fine=i+1;fine<r;fine++){
                        if (cake[fine][j]!='?'){
                            break;
                        } else
                            cake[fine][j]=cake[i][j];
                    }
                    for (int k=j-1;k>=0;k--){
                        bool toAdd=true;
                        for (int h=inizio;h<fine;h++){
                            if (cake[h][k]!='?'){
                                toAdd=false; break;
                            }
                        }
                        if (toAdd){
                            for (int h=inizio;h<fine;h++)
                                cake[h][k]=cake[i][j];
                        } else break;
                    }
                    for (int k=j+1;k<c;k++){
                        bool toAdd=true;
                        for (int h=inizio;h<fine;h++){
                            if (cake[h][k]!='?'){
                                toAdd=false; break;
                            }
                        }
                        if (toAdd){
                            for (int h=inizio;h<fine;h++)
                                cake[h][k]=cake[i][j];
                        } else break;
                    }
                }
            }
        }
        for (int y=0;y<r;y++){
            for (int x=0;x<c;x++){
                if (cake[y][x]=='?'){
                    giaUsati.clear();
                    for (int i=0;i<r;i++)
                        for (int j=0;j<c;j++)
                            cake[i][j]=ccopy[i][j];
                    for (int i=r-1;i>=0;i--){
                        for (int j=c-1;j>=0;j--){
                            if (cake[i][j]!='?' && giaUsati.find(cake[i][j])==giaUsati.end()){
                                giaUsati.insert(cake[i][j]);
                                int inizio,fine,z;
                                for (z=i-1;z>=0;z--){
                                    if (cake[z][j]!='?'){
                                        break;
                                    } else
                                        cake[z][j]=cake[i][j];
                                }
                                inizio=z+1;
                                for (fine=i+1;fine<r;fine++){
                                    if (cake[fine][j]!='?'){
                                        break;
                                    } else
                                        cake[fine][j]=cake[i][j];
                                }
                                for (int k=j-1;k>=0;k--){
                                    bool toAdd=true;
                                    for (int h=inizio;h<fine;h++){
                                        if (cake[h][k]!='?'){
                                            toAdd=false; break;
                                        }
                                    }
                                    if (toAdd){
                                        for (int h=inizio;h<fine;h++)
                                            cake[h][k]=cake[i][j];
                                    } else break;
                                }
                                for (int k=j+1;k<c;k++){
                                    bool toAdd=true;
                                    for (int h=inizio;h<fine;h++){
                                        if (cake[h][k]!='?'){
                                            toAdd=false; break;
                                        }
                                    }
                                    if (toAdd){
                                        for (int h=inizio;h<fine;h++)
                                            cake[h][k]=cake[i][j];
                                    } else break;
                                }

                            }
                        }
                    }
                }
            }
        }
        out<<"Case #"<<caso<<":"<<endl;
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                out<<cake[i][j];
            }
            out<<endl;
        }
    }
    return 0;
}
