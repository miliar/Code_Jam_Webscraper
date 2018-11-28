#include<iostream>
#include<cstring>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        char a[20];
        for(int z=0;z<20;z++){
            a[z]='\0';
        }
        cin>>a;
        int j=strlen(a);
        int m=0;
        int p=0;
        while(a[m]<=a[m+1]){
            if(a[m]==a[m+1]){
                p++;
            }
            m++;
        }
        if(m!=j-1){
            m=m-p;
            a[m]=a[m]--;
        }
        for(int k=m+1;k<j;k++){
            a[k]='9';
        }
        int cu=0;
        while(a[cu]=='0'){
            cu++;
        }
        cout<<"Case #"<<i<<": ";
        for(int l=cu;l<j;l++){
            cout<<a[l];
        }
        cout<<endl;
    }
return 0;
}
