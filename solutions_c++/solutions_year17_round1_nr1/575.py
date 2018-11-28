#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(){
    ifstream infile("in.txt");
    ofstream outfile("out.txt");
    int t; infile>>t;
    for (int h=0; h<t; h++){
        outfile<<"Case #"<<h+1<<": ";
        int r; infile>>r;
        int c; infile>>c;
        vector<vector<char> > v(r,vector<char> (c));
        vector<vector<int> > rowpos(c);
        for (int i=0; i<r; i++){
            for (int j=0; j<c; j++){
                char c;
                infile>>c;
                v[i][j]=c;
                if (c != '?'){
                   rowpos[j].push_back(i);
                }
            }
        }
        vector<int> fullcols;
        for (int j=0; j<c; j++){
            bool emp=true;
            for (int i=0; i<r; i++){
                if (v[i][j] != '?'){
                    emp=false;
                }
            }
            if (!emp){
                fullcols.push_back(j);
            }
        }
        for (int j=0; j<c; j++){
            if (rowpos[j].size()>0){
                int srow=0;
                for (int k=0; k<rowpos[j].size(); k++){
                    char c=v[rowpos[j][k]][j];
                    for (int m=srow; m<rowpos[j][k]; m++){
                        v[m][j]=c;
                    }
                    srow=rowpos[j][k]+1;
                }
                char clast=v[rowpos[j][rowpos[j].size()-1]][j];
                for (int mlast=srow; mlast<r; mlast++){
                    v[mlast][j]=clast;
                }
            }
        }
        int scol=0;
        for (int k=0; k<fullcols.size(); k++){
            for (int m=scol; m<fullcols[k]; m++){
                for (int i=0; i<r; i++){
                    v[i][m]=v[i][fullcols[k]];
                }
            }
            scol=fullcols[k]+1;
        }
        int lastfull=fullcols[fullcols.size()-1];
        for (int j=lastfull+1; j<c; j++){
            for (int i=0; i<r; i++){
                v[i][j]=v[i][lastfull];
            }
        }

        for (int i=0; i<r; i++){
            outfile<<endl;
            for (int j=0; j<c; j++){
                outfile<<v[i][j];
            }
        }
        outfile<<endl;
    }
}











