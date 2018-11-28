#include<iostream>
#include<cmath>

using namespace std;

int main(){
    int cases;
    cin>>cases;
    long int N;//the last number counted
    int digits;// gigits of N

    //cout<<123%10;

    int res;


    //cout<< (unsigned long int)(log10(111111111111111110)+1)<<endl;

    for(int index=0;index<cases;index++){
        cin>>N;
        digits = ( long int)(log10(N))+1;
        res=0;

        //cout<< digits<<endl;

        for(int d=1;d<digits;d++){
            //cout<< "comparacion"<<d<<endl;
            //cout<< (N% (long int)pow(10,d+1))/ (long int)pow(10,d)<<">"<<(N% (long int)pow(10,d))/(long int)(pow(10,d-1))<<endl;

            if((N% (long int)pow(10,d+1))/ (long int)pow(10,d)   > (N% (long int)pow(10,d))/(long int)(pow(10,d-1))){

                //cout<<"-"<<((N% (long int)pow(10,d)) / (long int)(pow(10,d-1)) + 1)*(long int)(pow(10,d-1))<<endl;
                //cout<<"-"<<((N% (long int)pow(10,d)) +1)<<endl;
                //N= N - ((N% (long int)pow(10,d)) / (long int)(pow(10,d-1)) + 1)*(long int)(pow(10,d-1));
                N= N - ((N% (long int)pow(10,d)) +1); 
            }
        }
        //cout<<endl;
        cout<<"Case #"<<index+1<<": "<<N<<endl;
        //cout<<N<<endl;
    }

    return 0;
} 