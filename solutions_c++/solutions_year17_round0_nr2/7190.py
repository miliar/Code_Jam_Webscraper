#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<cmath>
#include<set>
#include<map>

using namespace std;

bool check(int x){
    int l = 10;
    while(x) {
        if( (x%10)>l) return false;
        l=x%10;
        x/=10;
    }
    return true;
}
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,k,n;

    cin>>T;
    for(int t=1; t<=T; t++) {
        cin>>n;
        while(!check(n))
            n--;

        cout<<"Case #"<<t<<": ";
        cout<<n<<endl;
    }
}
