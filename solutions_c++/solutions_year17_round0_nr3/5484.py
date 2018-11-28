#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int n;
        int k;
        cin >> n >> k;
        int occupied[n+2];
        occupied[0]=occupied[n+1]=1;
        for(int r=0;r<n;r++){
            occupied[r+1]=0;
        }
        int lmax =0;
        int rmax =0;
        for(int j=0;j<k;j++){           //insert k people
            lmax =0;
            rmax =0;
            int lcur =0;
            int rcur =0;
            for(int c=1;c<=n+1;c++){        //find biggest leftmost gap
                if(occupied[c]==1){
                    lcur=rcur;
                    rcur = c;
                    if(rcur-lcur>rmax-lmax){
                        rmax=rcur;
                        lmax=lcur;
                    }
                    
                }
            }
            occupied[lmax+(rmax-lmax)/2]=1;
        }
        if((rmax-lmax)%2==0){
            int x = ((rmax-lmax)/2)-1;
            cout << "Case #" << i+1 << ": " << x <<" "<< x <<endl;
            }
        else{
            int x = (rmax-lmax)/2;
            cout << "Case #" << i+1 << ": " << x <<" "<<x-1<<endl;
        }
        
    }
  return 0;
}
