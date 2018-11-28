#include <bits/stdc++.h>
using namespace std;

bool check(long long n){
    vector<int> v;

    while(n){
        v.push_back(n%10);
        n/=10;
    }

    if(v.size()==1)
        return true;

    for(int i=0; i<v.size()-1; i++)
        if(v[i]<v[i+1])
            return false;

    return true;    
}

int main(){

      #ifndef ONLINE_JUDGE
     freopen("input.txt","r",stdin);
     freopen("output.txt","w",stdout);
   #endif

    int t,p=1;
    cin>>t;

    while(t--){
      
        long long n;
        cin>>n;
        //cout<<n;

        
        while(1){

            if(check(n))
                break;
            n--;
        }

        cout<<"Case #"<<p++<<": ";
        cout<<n<<endl;

       

    }


}