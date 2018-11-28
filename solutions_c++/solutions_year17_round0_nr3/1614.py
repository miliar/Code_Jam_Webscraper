#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <climits>
#include <queue>
#include <iomanip>
#include <cstdio>
#define lli long long int
#include<fstream>

using namespace std;

int main()
{

        ifstream cin("C-large.in");
	ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){

    lli n,o=0,e=0,on,en,sum=1L,k;
    cin>>n>>k;
    if(n%2==0)
        e=1,en=n;
    else o=1,on=n;
    lli psum=0;
    while(sum<k){
        lli te=0,to=0,ten=0,ton=0;
        psum=sum;
        if(e!=0&&en!=0){
            lli temp=en/2;

            ten=temp;
            ton=ten-1;

            if(temp%2!=0)
                swap(ten,ton);
            if(en!=2)
            te=e;
            to=e;
        }
        //1000000000000000000
        if(o!=0&&on!=1){
            lli temp=on/2;
            if(temp%2==0)
                te+=2*o,ten=temp;
            else to+=2*o,ton=temp;
        }
        on=ton;
        en=ten;
        e=te;
        o=to;
        sum+=te+to;

    //    cout<<on<<" "<<o<<"  "<<en<<" "<<e<<"    "<<sum<<endl;
    }

    lli index=k-psum;
    lli f,s;
    if((en>on&&index<=e)||(en<on&&index>o)){
        f=en/2;
        s=f-1;
    }else{
    f=on/2;
    s=f;
    }



     cout<<"Case #"<<tt<<": "<<f<<" "<<s<<endl;}
}
