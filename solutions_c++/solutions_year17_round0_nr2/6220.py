#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
using namespace std;

int main(){
    ifstream inStream ("C:\\Users\\techin philardluck\\Desktop\\code jam\\2\\B-large.in");

    int n;
    inStream >> n;


    uint64_t ans[n];
    for(int c=0;c<n;c+=1){
        uint64_t z;
        inStream >> z;
        int len = floor(log10(z)+1);

        if(len==1) ans[c]=z;
        else{
            int nx = 0;
            int d[len];
            uint64_t z2=z;
            for(int i=0;i<len;i+=1){
                d[i]=z2%10;
                z2/=10;
            }
            int ln = 0;
            for(int i=0;i<len-1;i+=1){
                if(d[i]<d[i+1]){
                    d[i]=9;
                    d[i+1]-=1;
                    for(int j=i;j>=ln;j-=1)
                        d[j]=9;
                    ln = i; //lastnine
                }

            }
            z2 = 0;
            for(int i=len-1;i>=0;i-=1){
                z2*=10;
                z2+=d[i];
            }
            ans[c]=z2;
        }
    }

    inStream.close();



    ofstream outStream ("C:\\Users\\techin philardluck\\Desktop\\code jam\\2\\B-large.out");

    for(int i=0;i<n;i+=1)
        outStream << "CASE #" << i+1 <<": "<< ans[i] << endl;
    outStream.close();

}
