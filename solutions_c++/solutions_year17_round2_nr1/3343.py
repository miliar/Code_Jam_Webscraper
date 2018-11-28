#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int cases;

    cin>>cases;

    double myS=0.0;
    int distance=0;
    int horses=0;
    int kofH = 0;
    int sofH = 0;
    double maxcomp =0.0;
    double max=0.0;
    

    for(int i=0; i<cases; i++){
       // cout<<i;
        myS=0;
        distance=0;
        horses=0;
        maxcomp = 0.0;
        max=0.0;
        
        cin>>distance;
        cin>>horses;

        //cout  << distance<<" "<<horses<<endl;

        for(int y=0;y<horses;y++){
            cin>>kofH>>sofH;

            if (y==0){
                max = double(distance-kofH)/double(sofH);
            }
            else{
                maxcomp = double(distance-kofH)/double(sofH);
                if(maxcomp>max){
                    max=maxcomp;
                }
            }
            //cout<<max<<endl;
        }
        myS= double(distance)/double(max);
        cout<<setprecision(6)<<fixed;
        cout<<"Case #"<<i+1<<": "<<myS<<endl;
    }
}