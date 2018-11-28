#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

void debug(vi & v){
    for (int i=0; i<v.size(); i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

int main(){
    ifstream infile("in.txt");
    ofstream outfile("out.txt");
    int t; infile>>t;
    for (int h=0; h<t; h++){
        outfile<<"Case #"<<h+1<<": ";
        int n; infile>>n;
        int c; infile>>c;
        int m; infile>>m;
        vvi v(c);
        vi ap(n);
        for (int i=0; i<m; i++){
            int p; infile>>p; p--;
            int b; infile>>b; b--;
            v[b].push_back(p);
            ap[p]++;
        }
        for (int i=0; i<c; i++){
            sort(v[i].begin(),v[i].end());
        }
        vvi ar;
        while (m>0){
            vi r;
            vi pct(n,0);
            for (int i=0; i<c; i++){
                for (int j=0; j<v[i].size(); j++){
                    if (v[i][j]!=(-1)){
                        int pj=v[i][j];
                        if (pct[pj]<=(pj)){
                            pct[pj]++;
                            r.push_back(pj);
                            m--;
                            v[i][j]=-1;
                            break;
                        }
                    }
                }
            }
            ar.push_back(r);
        }
        int z=ar.size();
        int ct=0;
        for (int i=0; i<n; i++){
            if (ap[i]>z){
                ct+=(ap[i]-z);
            }
        }
        outfile<<z<<" "<<ct<<endl;
        cout<<z<<" "<<ct<<endl;
    }
}








