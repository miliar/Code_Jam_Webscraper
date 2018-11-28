#include<bits/stdc++.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("output.in");
char a[1000];
int main(){
int t;
fin>>t;
int z=t;
while(t--){

    fin>>a;
    int ps;
    fin>>ps;
    int sum=0;
    int l=strlen(a);
    for(int i=0;i<=l-ps;i++){
        if(a[i]=='-'){
            sum++;
            for(int j=0;j<ps;j++){
                if(a[i+j]=='-')
                    a[i+j]='+';
                else
                    a[i+j]='-';
            }
        }
    }
    int flag=0;
    for(int i=0;i<l;i++){
        if(a[i]=='-'){
            fout<<"Case #"<<z-t<<": "<<"IMPOSSIBLE\n";
            flag=1;
            break;
        }
    }
    if(flag==0)
        fout<<"Case #"<<z-t<<": "<<sum<<endl;
    }
    return 0;
}
