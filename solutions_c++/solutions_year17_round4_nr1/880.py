#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

int main(){
    ifstream infile("in.txt");
    ofstream outfile("out.txt");
    int t; infile>>t;
    for (int h=0; h<t; h++){
        outfile<<"Case #"<<h+1<<": ";
        int n; infile>>n;
        int p; infile>>p;
        vi g(p);
        for (int i=0; i<n; i++){
            int gin; infile>>gin;
            int gval=gin%p;
            g[gval]++;
        }
        int sat=g[0];
        int left=n-g[0];
        int runpc=0;
        if (p==2){
            sat+=((g[1]+1)/2);
        }
        else if (p==3){
            while (left>0){
                if (runpc==0){
                    if (g[2]>0){
                        g[2]--;
                        left--;
                        sat++;
                        runpc=2;
                    }
                    else {
                        g[1]--;
                        left--;
                        sat++;
                        runpc=1;
                    }
                }
                else if (runpc==1){
                    if (g[2]>0){
                        g[2]--;
                        left--;
                        runpc=0;
                    }
                    else {
                        g[1]--;
                        left--;
                        runpc=2;
                    }
                }
                else {
                    if (g[1]>0){
                        g[1]--;
                        left--;
                        runpc=0;
                    }
                    else {
                        g[2]--;
                        left--;
                        runpc=1;
                    }
                }
            }
        }
        else if (p==4){
            if (g[2]%2==0){
                sat+=((g[2])/2);
                left-=(g[2]);
                g[2]=0;
            }
            else {
                sat+=((g[2])/2);
                left-=(g[2]-1);
                g[2]=1;
            }
            while (left>0){
                //cout<<g[1]<<" "<<g[2]<<" "<<g[3]<<endl;
                //cout<<runpc<<" "<<sat<<endl;
                if (runpc==0){
                    if (g[3]>0){
                        g[3]--;
                        left--;
                        sat++;
                        runpc=3;
                    }
                    else if (g[2]>0){
                        g[2]--;
                        left--;
                        sat++;
                        runpc=2;
                    }
                    else {
                        g[1]--;
                        left--;
                        sat++;
                        runpc=1;
                    }
                }
                else if (runpc==1){
                    if (g[3]>0){
                        g[3]--;
                        left--;
                        runpc=0;
                    }
                    else if (g[2]>0){
                        g[2]--;
                        left--;
                        runpc=3;
                    }
                    else {
                        g[1]--;
                        left--;
                        runpc=2;
                    }
                }
                else if (runpc==2){
                    if (g[2]>0){
                        g[2]--;
                        left--;
                        runpc=0;
                    }
                    else if (g[1]>0){
                        g[1]--;
                        left--;
                        runpc=3;
                    }
                    else {
                        g[3]--;
                        left--;
                        runpc=1;
                    }
                }
                else {
                    if (g[1]>0){
                        g[1]--;
                        left--;
                        runpc=0;
                    }
                    else if (g[3]>0){
                        g[3]--;
                        left--;
                        runpc=2;
                    }
                    else {
                        g[2]--;
                        left--;
                        runpc=1;
                    }
                }
            }
        }
        outfile<<sat<<endl;
        cout<<sat<<endl;
    }
}











