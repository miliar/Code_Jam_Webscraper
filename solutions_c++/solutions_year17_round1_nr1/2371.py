#define lli unsigned long long int
#include <stdio.h>
#include <bits/stdc++.h>

#include <string.h>
#include <math.h>
#include <stdlib.h>

using namespace std;
int main() {
    freopen ("myoutput.txt","w",stdout);
    
    lli t;cin>>t;
    lli testcase=1;
    
    while(t--){
        lli r,c;
        cin>>r>>c;
        vector<vector<char> > n(r);
        char o[r][c],out[r][c];
        lli num[r];
        lli minr=0,maxr=0;
        
        for(lli i=0;i<r;i++){
            num[i]=0;
            for(lli j=0;j<c;j++){
                cin>>o[i][j];
                out[i][j]='?';
                if(o[i][j]!='?'){
                    if(minr==0)minr=i;
                    maxr=i;
                    num[i]++;
                    n[i].push_back(o[i][j]);
                }
            }
        }
        
        for(lli i=0;i<r;i++){
            if(num[i]==0){continue;}
            char curr=n[i][0];
            for(lli j=0;j<c;j++){
                if(o[i][j]!='?' && o[i][j]!=curr){
                    curr=o[i][j];
                }
                out[i][j]=curr;
            }
        }

        lli currRow=minr;        
        for(lli i=0;i<r;i++){
            if(num[i]==0){
                for(lli j=0;j<c;j++){
                        if(out[i][j]=='?'){
                            out[i][j]=out[currRow][j];
                        }
                }
            }
            else{
                currRow=i;
            }
        }
        
        /*
        for(lli i=0;i<r;i++){
            cout<<num[i];
            for(vector<char>::iterator itr=n[i].begin();itr!=n[i].end();itr++){
                cout<<*itr<<" ";
            }
            cout<<endl;
        }
        */
        
        cout<<"Case #"<<testcase++<<": "<<endl;
        for(lli i=0;i<r;i++){
            for(lli j=0;j<c;j++){
                cout<<out[i][j];
            }
            cout<<endl;
        }

        

    }
    return 0;
}