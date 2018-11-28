#include <bits/stdc++.h>
using namespace std;

int main() {  
    int test,pq=1;
    cin>>test;
    while(test){
        test--;
    long double total,k,pp;
    vector<long double> v1;
    vector<long double> v2;
    cin>>total>>k;
    for(int i=0;i<k;i++){
        cin>>pp;
        v1.push_back(pp);
        cin>>pp;
        v2.push_back(pp);
    }
    for(long double i=0;i<k;i++){
        for(long double j=0;j<k;j++){
            if(v1[i]<v1[j]){
                pp=v1[i];
                v1[i]=v1[j];
                v1[j]=pp;
                pp=v2[i];
                v2[i]=v2[j];
                v2[j]=pp;
            }
        }
    }
    long double left,t_time,final_time,flag=0;
    for(long double i=0;i<k;i++){
        left=total-v1[i];
        t_time=left/v2[i];
        if(flag==0){
            flag=1;
            final_time=t_time;
        }else{
            if(final_time<t_time){
                final_time=t_time;
            }
        }
       // cout<<v1[i]<<" "<<v2[i]<<" "<<final_time<<endl;
        
    }
    pp=total/final_time;
    cout<<"Case #"<<pq<<": ";
    pq++;
    cout<<fixed<<setprecision(6)<<pp<<endl;
    }
	return 0;
}
