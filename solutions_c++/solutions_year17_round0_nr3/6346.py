#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
//g++ -std=c++11 -o main *.cpp 
using namespace std;

//#define eps 0.001
#define dt unsigned long long int

dt max(dt a,dt b){
    return a>b?a:b;
}
pair< dt, dt> bathroomStalls(dt n, dt k){
    if(n == k){
        return pair<dt,dt>(0,0);
    }
    priority_queue<dt>pq;
    pq.push(n);
    dt m=n,ls,lr,d;
    dt i=1,j=0;
    for (i=1,j=0;i<=k;i+=1<<j++){
        d=m;
        m=m/2;
        k-=i;
        cout<<i<<" -> "<<k<<" "<<j<<" "<<m<<endl;
    }  
    if(k > 0 && k<i){
        d=m;
        m=m/2;
    }
    //cout<<i<<" -> "<<k<<endl;
    /*
    8
    1000000000000000000 100000000000000000
    */
    cout<<" m "<<m<<endl;
    ls=m;
    if( d%2 != 0){
        lr =m;
    }else{
        lr=max(m-1,0);
    }
    return pair<dt,dt>(ls,lr);
}

pair< dt, dt> bathroomStalls1(dt n, dt k){
    if(n == k){
        return pair<dt,dt>(0,0);
    }
    priority_queue<dt>pq;
    pq.push(n);
    dt m=0,ls,lr;
    
    for (dt i=0;i<k;i++){
        m = pq.top(); pq.pop();
        if(m%2!=0){
            ls=lr=m/2;
        }else{
            ls=m/2;
            lr=m/2-1;
            if(lr<0){
                lr=0;
            }
        }
        //cout<<(((double)m)/2.0-1.0)<<endl;
        pq.push(ls);
        pq.push(lr);
    }   
    return pair<dt,dt>(ls,lr);
}
int main(){
    
    ifstream cin("C-small-1-attempt1.in");
    ofstream cout("C-small-1-attempt1.out");
    //*/
    dt c,n,k;
    string number;
    pair<dt,dt> p;
    cin>>c;
    for (dt i=0;i<c;i++){
        cin>>n>>k;
        p = bathroomStalls1(n,k);
        cout<<"Case #"<<(i+1)<<": "<<p.first<<" "<<p.second<<endl;
    }
    return 0;
}