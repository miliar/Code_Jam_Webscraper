#include <bits/stdc++.h>

using namespace std;

int arr[1005];

void flip(int index, int k){
    for(int i=index;i<index+k;i++){
        arr[i]=(arr[i]+1)%2;
    }
}

int main(){
    freopen("A-large.in","r",stdin); freopen("A-large-output.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        string s;
        int k;
        cin>>s>>k;
        int len=s.length();
        for(int i=0;i<len;i++){
            if (s[i]=='+')
                arr[i]=1;
            else arr[i]=0;
        }

        int counter=0;
        for(int i=0;i<=len-k;i++){
            if (arr[i]==0){
                flip(i,k);
                counter++;
            }
        }
        bool found=true;
        for(int i=0;i<len;i++){
            if (arr[i]==0)
                found=false;
        }

        if (found){
            cout<<"Case #"<<tc<<": "<<counter<<endl;
        }
        else {
            cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
        }

    }
}
