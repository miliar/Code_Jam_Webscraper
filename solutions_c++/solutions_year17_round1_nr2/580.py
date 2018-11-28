#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

struct range {
    int lb;
    int ub;
};

bool operator<(const range & a, const range & b){
    if (a.lb<b.lb){
        return true;
    }
    if (a.lb>b.lb){
        return false;
    }
    return (a.ub<b.ub);
}

int n;
int p;

bool solve(int i, vector<vector<range > > & vr, int rlb, int rub, vector<int> & rowpos, vector<int> & fixedpos){
    //cout<<"Solving for "<<i<<" with "<<rlb<<"-"<<rub<<endl;
    if (i==n){
        for (int ii=0; ii<n; ii++){
            fixedpos[ii]=rowpos[ii]+1;
        }
        return true;
    }
    rowpos[i]=fixedpos[i];
    while (rowpos[i]<p){
        int j=rowpos[i];
        int tlb=max(rlb,vr[i][j].lb);
        int tub=min(rub,vr[i][j].ub);
        //cout<<"tlb tub "<<tlb<<" "<<tub<<endl;
        if (tlb<=tub){
            if (solve(i+1,vr,tlb,tub,rowpos,fixedpos)){
                return true;
            }
        }
        rowpos[i]++;
    }
    return false;
}

int main(){
    ifstream infile("in.txt");
    ofstream outfile("out.txt");
    int t; infile>>t;
    for (int h=0; h<t; h++){
        outfile<<"Case #"<<h+1<<": ";
        infile>>n;
        infile>>p;
        vector<int> v(n);
        for (int i=0; i<n; i++){
            infile>>v[i];
        }
        vector<vector<int> > q(n, vector<int> (p));
        vector<vector<range> > vr(n, vector<range> (p));
        for (int i=0; i<n; i++){
            for (int j=0; j<p; j++){
                infile>>q[i][j];
                q[i][j]*=10;
                int ld=v[i]*11;
                int ud=v[i]*9;
                if (q[i][j] % ld == 0){
                    vr[i][j].lb=q[i][j]/ld;
                }
                else {
                    vr[i][j].lb=q[i][j]/ld+1;
                }
                vr[i][j].ub=q[i][j]/ud;
            }
            sort(vr[i].begin(),vr[i].end());
        }
        /*
        for (int i=0; i<n; i++){
            for (int j=0; j<p; j++){
                cout<<vr[i][j].lb<<"-"<<vr[i][j].ub<<" ";
            }
            cout<<endl;
        }
        */
        int kits=0;
        vector<int> rowpos(n,0);
        vector<int> fixedpos(n,0);
        while (true){
            int i=0;
            int rlb=0;
            int rub=1000000000;
            /*for (int ii=0; ii<n; ii++){
                rowpos[ii]=fixedpos[ii];
            }*/
            if (solve(i,vr,rlb,rub,rowpos,fixedpos)){
                kits++;
            }
            else {
                break;
            }
        }
        //cout<<kits<<endl;
        outfile<<kits<<endl;

    }
}












