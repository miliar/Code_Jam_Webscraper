#include <bits/stdc++.h>
#define ull unsigned long long int

using namespace std;

vector<ull> tidy;

int arr[25];


void func(int pos){
    ull num=0;
    for(int i=0;i<=pos;i++){
        num+=arr[i];
        if (i<pos)
            num*=10;
    }
    tidy.push_back(num);
    return;
}

void backTrack(int num, int pos){
    if (pos==19)
        return;
    arr[pos]=num;
    func(pos);

    for(int i=num;i<=9;i++){
        backTrack(i,pos+1);
    }

}

int main(){

    freopen("B-large.in","r",stdin); freopen("B-large-output.txt","w",stdout);

    for(int i=1;i<=9;i++){
        backTrack(i,0);
    }

    sort(tidy.begin(),tidy.end());

    /*cout<<tidy.size()<<endl;

    for(int i=0;i<tidy.size();i+=10000){
        cout<<" i = "<<i<<" "<<tidy[i]<<endl;
    }*/


    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        ull n;
        cin>>n;

        ull last=1;
        for(int i=0;i<tidy.size();i++){
            if (tidy[i]>n){
                last=tidy[i-1];
                 break;
            }
        }
        cout<<"Case #"<<tc<<": "<<last<<endl;

    }
}

