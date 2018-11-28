#include <iostream>
#include <queue>

using namespace std;

int main(){

    priority_queue<unsigned long long > pq;
    unsigned int tatti;
    cin>>tatti;
    unsigned int spoofy=1;
    while(tatti--){
        unsigned long long a,b,t,k,n;
        cin>>k>>n;
        pq.push(k);
        while(n--){
            t= pq.top();
            pq.pop();
            t-=1;
            a=t/2;b=t/2;
            if(t%2){
                b+=1;
            }
            pq.push(a);pq.push(b);

        }
        cout<<"Case #"<<spoofy<<": "<<b<<" "<<a<<endl;
        pq = priority_queue <unsigned long long>();
        spoofy++;
    }
}
