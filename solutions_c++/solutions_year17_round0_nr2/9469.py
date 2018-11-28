#include<bits/stdc++.h>

using namespace std;

bool check(long long num){
    //cout<<num<<" ";
    int arr[18],j=0;
    if(num>=1&&num<=9)
        return true;
    else{
        while(num>0){
        arr[j++]=num%10;
        num=num/10;
        }
        for(int x=j-1;x>0;x--){
            if(arr[x]>arr[x-1])
               return false;
        }
        return true;
    }
}



int main(){
freopen("B-small-attempt5.in","r",stdin);
freopen("output_file_name.out","w",stdout);

int t;
scanf("%d",&t);
    for(int b=1;b<=t;b++){
    long long n;
    scanf("%lld",&n);
    bool found=true;
    while(found){
        if(check(n)){
           cout<<"Case #"<<b<<":"<<" ";
           cout<<n<<endl;
            found=false;
            break;
        }
        else check(n--);
    }
    }
    return 0;
}
