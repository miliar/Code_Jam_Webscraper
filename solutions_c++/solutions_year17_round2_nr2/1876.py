#include <iostream>
#include<algorithm>
#include<cmath>
#include<iomanip>
using namespace std;

int main() {
    int n,t,r,o,y,g,b,v,i,maxx,midd,minn;
    char max,mid,min;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>n>>r>>o>>y>>g>>b>>v;
        if(r>y && r>b){
            max='R';
            maxx=r;
            if(y>b){
                mid='Y';
                midd=y;
                min='B';
                minn=b;
            }
            else{
                mid='B';
                midd=b;
                min='Y';
                minn=y;
            }
        }
        else if(y>r && y>b){
            max='Y';
            maxx=y;
            if(r>b){
                mid='R';
                midd=r;
                min='B';
                minn=b;
            }
            else{
                mid='B';
                midd=b;
                min='R';
                minn=r;
            }
        }
        else{
            max='B';
            maxx=b;
            if(y>r){
                mid='Y';
                midd=y;
                min='R';
                minn=r;
            }
            else{
                mid='R';
                midd=r;
                min='Y';
                minn=y;
            }
        }
        if(maxx<=(n/2)){
        while(maxx+midd+minn){
      
            if(maxx>0){
                if(midd>=minn){
                    cout<<max<<mid;
                    maxx--;midd--;
                }
                else{
                    cout<<max<<min;
                    maxx--;minn--;
                }
            }
            else{
                if(midd==minn){
                    while(midd+minn){
                        cout<<mid<<min;
                        midd--;minn--;
                    }
                }
                else{
                    cout<<min;minn--;
                    while(midd+minn){
                        cout<<mid<<min;
                        midd--;minn--;
                }
            }
        }
        }
             cout<<endl;
    }
       
        else{
            cout<<"IMPOSSIBLE"<<endl;
        }
    }
	return 0;
}
