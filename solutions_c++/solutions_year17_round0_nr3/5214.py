#include<iostream>
#include<queue>
using namespace std;
long long n,k;
int t;
long long res;

int main(){
    cin>>t;
    for(int tt=0;tt<t;tt++){
        cin>>n>>k;
        priority_queue<int> kol;
        kol.push(n);
        k--;
        while(k>0){
            int x=kol.top();
            kol.pop();
            kol.push((x-1)/2);
            kol.push((x)/2);
            k--;
        }
        cout<<"Case #"<<tt+1<<": ";
        int x=kol.top();
        cout<<x/2<<" "<<(x-1)/2<<endl;
    }
}