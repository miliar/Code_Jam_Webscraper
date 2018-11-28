#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <stdio.h>
using namespace std;

int main() {
    fstream infile;
    FILE *outfile;
    infile.open("input.txt", ios::in);
    outfile = fopen("output.txt","w");
    int t,z=0;
    infile>>t;
    while(z<t){
        double ans,d;
        int n;
        infile>>d>>n;
        double horse[n][2];
        for(int i=0;i<n;i++){
            infile>>horse[i][0]>>horse[i][1];
        }
        double tyme=0;
        double t1,t2;
        if(n==0)
            tyme = d/10000;
        else if(n==1)
            tyme=(d-horse[0][0])/horse[0][1];
        for(int i=0;i<n-1;i++){
            t1=(d-horse[i][0])/horse[i][1];
            //outfile<<"t1 : "<<t1<<endl;
            t2=(d-horse[i+1][0])/horse[i+1][1];
            //outfile<<"t2 : "<<t2<<endl;
            if(t2<t1){
                if(t1>tyme)
                    tyme=t1;
            }
            else if(t2>tyme)
                tyme=t2;
        }
        ans = d/tyme;
        z++;
        //outfile<<"Case #"<<z<<": "<<ans<<"\n";
        fprintf(outfile,"Case #%d: %.6f\n",z,ans);
    }
    infile.close();
    fclose(outfile);
    return 0;
}