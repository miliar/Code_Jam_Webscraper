#include <bits/stdc++.h>
using namespace std;
stack<char> s1;
//int count1=0;
int get_result(string input,int inp_size,int l,int cases){
    int i=0,j,k,temp,temp1=0;
    int charcount=0;
    while(i < inp_size ){
        for(i=0; i< inp_size;i++){
            if(input[i]=='-'){
                if(i>=(inp_size-l+1)){
                    cout<<"Case #"<<cases<<":"<<" "<<"IMPOSSIBLE"<<endl;
                    temp1=1;
                    break;
                }
            j=i;
            while(j < i+l){
                if(input[j]=='+'){
                    input[j]='-';
                }
                else{
                    input[j]='+';
                }
                j++;
            }
            charcount++;
        }
    }
    if(temp1==1){
        break;
    }
    }
    if(temp1!=1){
    cout<<"Case #"<<cases<<":"<<" "<<charcount<<endl;
    }
    return 0;
}
int main(){
    freopen("inputlarge.in","r",stdin);
    freopen("outputlarge.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cases = 1;cases<=t;cases++){
        string input;
        int l;
        cin>>input;
        cin>>l;
        int inp_size = input.length();
        int result=get_result(input,inp_size,l,cases);
    }
    return 0;
}