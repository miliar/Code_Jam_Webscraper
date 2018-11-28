#include<iostream>
#include<fstream>
using namespace std;

int main(){
    ifstream inStream ("C:\\Users\\techin philardluck\\Desktop\\code jam\\A-large.in");

    int n;
    inStream >> n;

    int s[n],c[n];
    string p[n];

    for(int i=0;i<n;i+=1)
        inStream >> p[i] >> s[i];
    inStream.close();

    for(int i=0;i<n;i+=1){
        c[i]=0;
        for(int j=0;j<p[i].size();j+=1){

            if(j+s[i]<=p[i].size() && p[i][j]=='-'){
                for(int k=0;k<s[i];k++)
                    p[i][j+k] = p[i][j+k]=='+'? '-':'+';
                c[i]+=1;
            }
        }
    }

    bool im[n];
    for(int i=0;i<n;i+=1){
        im[i]=true;
        for(int j=0;j<p[i].size();j+=1)
            if(p[i][j]=='-'){
                im[i] = false;
                break;
            }
    }

    ofstream outStream ("C:\\Users\\techin philardluck\\Desktop\\code jam\\A-large.out");

    for(int i=0;i<n;i+=1)
        if(im[i])   outStream << "CASE #" << i+1 <<": "<< c[i] << endl;
        else        outStream << "CASE #" << i+1 << ": IMPOSSIBLE\n";

    outStream.close();
}
