#include<iostream>
using namespace std;
int tidy(long long int n,int j1){
    int alpha=0,beta,temp,gamma;
    while(n>=0){
        temp=n;
        beta=10;
        gamma=0;
        while(temp!=0){
              //  cout<<"temp is 1 "<<temp<<endl;
            alpha=temp%10;
            if(alpha>beta){
                gamma=1;
                break;
            }
            else{
                beta=alpha;
            }
            temp=temp/10;
            //cout<<"alpha is "<<alpha<<endl;
            //cout<<"beta is "<<beta<<endl;
            //cout<<"temp is "<<temp<<endl;
        }
        if(gamma==0){
            cout<<"Case #"<<j1<<":"<<" "<<n<<endl;
            break;
        }
        //cout<<"gamma is "<<gamma<<endl;
        n--;
        //cout<<"!"<<endl;
    }
    return 0;
}
int main(){
    int t;
    cin>>t;
    int j1=1;
    while(t--){
        long long int n;
        cin>>n;
        int temp=tidy(n,j1);
        j1++;
    }
    return 0;
}
