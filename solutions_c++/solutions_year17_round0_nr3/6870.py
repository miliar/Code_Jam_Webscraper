#include<vector>
#include<iostream>
#include<stdio.h>
#include<assert.h>
#include<algorithm>

using namespace std;

template<typename T>
void pop_front(vector<T>& vec)
{
    assert(!vec.empty());
    vec.erase(vec.begin());
}

bool myfunction (int i,int j) { return (i>j); }


int main(){
freopen("C-small-1-attempt1.in","r",stdin);
freopen("outhelo1.txt","w",stdout);
int test;
vector<long long> elist;
long long n,k,mina,maxa;
cin>>test;

for(int p=1;p<=test;p++){
cin>>n>>k;

if(n==k) {cout<<"Case #"<<p<<": 0 0\n"; continue;}
elist.clear();
if(n%2==0) {
    maxa = n/2 ;
    mina = maxa-1 ;
    elist.push_back(maxa);
    elist.push_back(mina);
}
else {
    maxa = n/2;
    mina = maxa;
    elist.push_back(maxa);
    elist.push_back(mina);
    }
for(int i=0;i<k-1;i++){
    sort(elist.begin(), elist.end(), myfunction);
    if(elist.front()%2==0){
        maxa = elist.front()/2 ;
        mina = maxa-1 ;
    }
    else {
        maxa = elist.front()/2;
        mina = maxa;
    }
    if(maxa!=0 ) elist.push_back(maxa);
    if(mina!=0 ) elist.push_back(mina);
    pop_front(elist);
    }
    cout<<"Case #"<<p<<": "<<maxa<<" "<<mina<<"\n";
}
}

